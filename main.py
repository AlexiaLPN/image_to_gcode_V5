import streamlit as st
import fullcontrol as fc
import lab.fullcontrol as fclab
from math import *
import numpy as np
from Configs import configMonstre2mm
from SequencePoudrage import *
from motifs_bords import *
import cv2
from fullcontrol.visualize.plot_data import PlotData
from fullcontrol.visualize.state import State
from fullcontrol.visualize.controls import PlotControls
from fullcontrol.visualize.plotly import plot

# Motifs bords:

def tartelette_contour_cv(image_cv, longueur, hauteur, pas, pas_bord, e_fond, e_bord, v_fond, v_bord, type_bord):

    ### 1. Extraction et simplification du contour ###
    image = image_cv
    _, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        return []
    fruit_contour = max(contours, key=cv2.contourArea)
    epsilon = 0.5
    fruit_contour = cv2.approxPolyDP(fruit_contour, epsilon, True)
    coords = np.array([pt[0] for pt in fruit_contour])

    # Mise à l’échelle
    x, y, w, h = cv2.boundingRect(fruit_contour)
    scale = longueur / max(w, h)
    scaled_coords = coords * scale

    # Centrage
    min_x, min_y = np.min(scaled_coords, axis=0)
    centered_coords = scaled_coords - np.array([min_x, min_y])
    x_coords, y_coords = centered_coords[:, 0], centered_coords[:, 1]

    # retournement de l'image car c'était à l'envers
    max_y = np.max(y_coords)
    y_coords = max_y - y_coords

    ### 2. Matrice binaire alignée avec le contour ###
    t_matrice_x = round(longueur / pas * 3)
    t_matrice_y = round(longueur / pas * 3)

    xs = np.linspace(x_coords.min(), x_coords.max(), t_matrice_x)
    ys = np.linspace(y_coords.min(), y_coords.max(), t_matrice_y)
    xv, yv = np.meshgrid(xs, ys)
    grid_points = np.column_stack((xv.ravel(), yv.ravel()))

    from matplotlib.path import Path
    contour_path = Path(np.column_stack((x_coords, y_coords)))
    mask = contour_path.contains_points(grid_points)
    binary_matrix = mask.reshape(t_matrice_y, t_matrice_x).astype(int)

    ### 3. Remplissage fond (lignes verticales) ###
    remplissage_fond = []
    for j in range(0, t_matrice_x, 3):
        colonne = range(t_matrice_y) if j % 2 == 0 else range(t_matrice_y - 1, -1, -1)
        dehors = True
        for i in colonne:
            if binary_matrix[i, j] == 1:
                pt = fc.Point(x=xs[j], y=ys[i], z=0)
                if dehors:
                    remplissage_fond.extend(fc.travel_to(pt))
                else:
                    remplissage_fond.append(pt)
                dehors = False
            else:
                dehors = True
    
    ### 4. Bord vertical ###
    contour_pts = [fc.Point(x=x, y=y, z=0) for x, y in zip(x_coords, y_coords)]
    bord = []
    z = 0

    if type_bord == "Bord plein":
        while z <= hauteur:
            bord.extend(fc.move(contour_pts, fc.Vector(z=z)))
            z += pas_bord

    elif type_bord in ["Dentelle petites mailles", "Dentelle maille haute"]:

        l = 0
                   
        points = [[x_coords[0], y_coords[0], l]]
        for i in range(1, len(x_coords)):
            x1, y1 = x_coords[i - 1], y_coords[i - 1]
            x2, y2 = x_coords[i], y_coords[i]
            l += np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            points.append([x2, y2, l])
        perimetre = l

        pointsbis = []
        for i in range(len(points) - 1):
            x1, y1, l1 = points[i]
            x2, y2, l2 = points[i + 1]
            ds = 0.1
            n = int((l2 - l1) / ds)
            for k in range(n):
                x = x1 + k * (x2 - x1) / n
                y = y1 + k * (y2 - y1) / n
                l = l1 + np.sqrt((x - x1)**2 + (y - y1)**2)
                pointsbis.append([x, y, l])                                    

        motif = (
                                                 
            quadrillage(perimetre, hauteur)

            if type_bord == "Dentelle petites mailles"
            else bosseshautessolides(perimetre, hauteur)
        )

        for element in motif:
            if type(element).__name__ == 'Point':
                i = min(int(element.x/perimetre*len(pointsbis)),len(pointsbis)-1)
                bord.append(fc.Point(x=pointsbis[i][0],y=pointsbis[i][1],z=element.z))
            else:
                bord.append(element)

    ### 5. Assemblage final ###
    forme = []
    forme.append(fc.ManualGcode(text=f'M221 S{e_fond}'))
    forme.append(fc.ManualGcode(text=f'M220 S{v_fond}'))
    forme.extend(remplissage_fond)

    if remplissage_fond:
        last_fill = remplissage_fond[-1]
        for el in bord:
            if isinstance(el, fc.Point):
                pointinitialbord = el
                break
        forme.extend(fc.travel_to(fc.Point(x=last_fill.x, y=last_fill.y, z=10)))
        forme.extend(fc.travel_to(fc.Point(x=pointinitialbord.x, y=pointinitialbord.y, z=10)))
        forme.extend(fc.travel_to(fc.Point(x=pointinitialbord.x, y=pointinitialbord.y, z=0)))

    forme.append(fc.ManualGcode(text=f'M221 S{e_bord}'))
    forme.append(fc.ManualGcode(text=f'M220 S{v_bord}'))
    forme.extend(bord)                   

    ### 6. Points de transition ###
    maxX = max((el.x for el in forme if isinstance(el, fc.Point)), default=0)
    maxY = max((el.y for el in forme if isinstance(el, fc.Point)), default=0)
    maxZ = max((el.z for el in forme if isinstance(el, fc.Point)), default=0)

    for el in forme:
        if isinstance(el, fc.Point):
            pointinitial = el
            break
    forme = (
        fc.travel_to(fc.Point(x=pointinitial.x, y=pointinitial.y, z=maxZ + 20))
        + fc.travel_to(fc.Point(x=pointinitial.x, y=pointinitial.y, z=0))
        + forme
    )

    for i in range(1, len(forme)):
        if isinstance(forme[-i], fc.Point):
            pointfinal = forme[-i]
            break
    forme.extend(fc.travel_to(fc.Point(x=pointfinal.x, y=pointfinal.y, z=maxZ + 20)))

    ### 7. Décalage dans le bac ###
    for el in forme:
        if isinstance(el, fc.Point):
            el.x += -1
            el.y += -30
            el.z += 2

    return forme, maxX, maxY, maxZ
    
def generer_gcode(image_bytes, longueur, hauteur, type_bord, type_impression):
    
    pas = 1.5 # pas pour le fond
    pas_bord = 1.5 # pas pour le bord
    if type_impression == "Poudre blé luxe et appareil sucré luxe":
        e_fond = 50 # multiplicateur d'extrusion 
        v_fond = 100 # vitesse d'impression
        e_bord = 50 # multiplicateur d'extrusion 
        v_bord = 100 # vitesse d'impression
    elif type_impression == "Poudre blé luxe et appareil salé":
        e_fond = 50 # multiplicateur d'extrusion 
        v_fond = 100 # vitesse d'impression
        e_bord = 50 # multiplicateur d'extrusion 
        v_bord = 100 # vitesse d'impression
    elif type_impression == "Poudre blé luxe et appareil vegan":
        e_fond = 50 # multiplicateur d'extrusion 
        v_fond = 100 # vitesse d'impression
        e_bord = 50 # multiplicateur d'extrusion 
        v_bord = 100 # vitesse d'impression
    elif type_impression == "Poudre sans gluten et appareil sans gluten":
        e_fond = 50 # multiplicateur d'extrusion 
        v_fond = 100 # vitesse d'impression
        e_bord = 50 # multiplicateur d'extrusion 
        v_bord = 100 # vitesse d'impression
    elif type_impression == "Poudre blé cacao et appareil sucré luxe":
        e_fond = 50 # multiplicateur d'extrusion 
        v_fond = 100 # vitesse d'impression
        e_bord = 50 # multiplicateur d'extrusion 
        v_bord = 100 # vitesse d'impression
    elif type_impression == "Poudre de macaron et appareil macaron":
        e_fond = 50 # multiplicateur d'extrusion 
        v_fond = 100 # vitesse d'impression
        e_bord = 50 # multiplicateur d'extrusion 
        v_bord = 100 # vitesse d'impression                                                                    
    
    liste = []
    liste.append(fc.ManualGcode(text=';PARAMÈTRES UTILISÉS :'))
    liste.append(fc.ManualGcode(text='G28'))
    liste.append(fc.ManualGcode(text='M42 P5 S1'))
    liste.append(fc.ManualGcode(text=poudrage_initial()))

    # Lire l'image depuis les bytes
    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    image_cv = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    if image_cv is None:
        raise ValueError("L'image n'a pas pu être lue. Vérifiez qu'il s'agit bien d'un fichier .jpg valide.")

    # Sauver temporairement si nécessaire pour la compatibilité (à éviter si possible)
    # cv2.imwrite("temp_image.jpg", image_cv)

    # Appeler la fonction principale avec cette image OpenCV directement
    forme, maxX, maxY, maxZ = tartelette_contour_cv(image_cv, longueur, hauteur, pas, pas_bord, e_fond, e_bord, v_fond, v_bord, type_bord)

    if maxZ <= 28:
        Dx = maxX + 20 # Décalage entre 2 pièces sur l'axe x
        Dy = maxY + 20 # Décalage entre 2 pièces sur l'axe y
    elif maxZ <= 50:
        Dx = maxX + 30 # Décalage entre 2 pièces sur l'axe x
        Dy = maxY + 30 # Décalage entre 2 pièces sur l'axe y
    else:
        Dx = maxX + 40 # Décalage entre 2 pièces sur l'axe x
        Dy = maxY + 40 # Décalage entre 2 pièces sur l'axe y
    
    
    Dz = hauteur + 5 # Décalage entre 2 pièces sur l'axe z
    Nx = 0 # Nombre de pièces sur l'axe x
    Ny = 0 # Nombre de pièces sur l'axe y
    Nz = 0 # Nombre de pièces sur l'axe z
    dimX = -5
    dimY = -30
    dimZ = 1
    if dimX + maxX <= 235 and dimY + maxY <= 146 and dimZ + maxZ <= 100: # on vérifie que la pièce passe dans le bac
        Nx += 1
        Ny += 1
        Nz += 1
        dimX += maxX
        dimY += maxY
        dimZ += maxZ
    while dimX < 235: # on ajuste les valeurs maximales pour Nx, Ny et Nz
        dimX += Dx
        if dimX <= 235:
            Nx += 1    
    while dimY < 146:
        dimY += Dy
        if dimY <= 146:
            Ny += 1   
    while dimZ < 100:
        dimZ += Dz
        if dimZ <= 100:
            Nz += 1
    
    Dx2 = maxY + 20 # Décalage entre 2 pièces sur l'axe x
    Dy2 = maxX + 20 # Décalage entre 2 pièces sur l'axe y
    Dz2 = hauteur + 15 # Décalage entre 2 pièces sur l'axe z
    Nx2 = 0 # Nombre de pièces sur l'axe x
    Ny2 = 0 # Nombre de pièces sur l'axe y
    Nz2 = 0 # Nombre de pièces sur l'axe z
    dimX = -5
    dimY = -30
    dimZ = 1
    if dimX + maxY <= 235 and dimY + maxX <= 146 and dimZ + maxZ <= 100: # on vérifie que la pièce passe dans le bac
        Nx2 += 1
        Ny2 += 1
        Nz2 += 1
        dimX += maxY
        dimY += maxX
        dimZ += maxZ
    while dimX < 235: # on ajuste les valeurs maximales pour Nx, Ny et Nz
        dimX += Dx2
        if dimX <= 235:
            Nx2 += 1   
    while dimY < 146:
        dimY += Dy2
        if dimY <= 146:
            Ny2 += 1  
    while dimZ < 100:
        dimZ += Dz2
        if dimZ <= 100:
            Nz2 += 1
    if Nx2*Ny2*Nz2 > Nx*Ny*Nz:
        Nx = Nx2
        Ny = Ny2
        Dx = Dx2
        Dy = Dy2
        forme = fc.move(fclab.rotate(forme,fc.Point(x=-1,y=-30,z=2),'z',-pi/2),fc.Vector(y=maxX))

    if Nx*Ny*Nz < 0.5: # si pas de pièce rentre dans le bac
        return 0

    etage = fc.move(fc.move(forme,fc.Vector(x=Dx),True,Nx),fc.Vector(y=Dy),True,Ny) # Création de 1 étage de Nx*Ny pièces

    for i in range(Nz):
        Z = i*Dz + 1
        if i!=0:
            liste.append(fc.ManualGcode(text=poudrage_z(Z,Nz,i)))
        liste.extend(fc.move(etage,fc.Vector(z=Z),False))

    liste.append(fc.ManualGcode(text='M221 S100'))
    liste.append(fc.ManualGcode(text='M220 S100'))
    liste.append(fc.ManualGcode(text='G28'))
    return configMonstre2mm.getGcode(liste), liste


# -------------------- Interface Streamlit -------------------- #

st.set_page_config(page_title="GCODE Images", page_icon="🖨️")

st.title("🖨️ Générateur de GCODE - Tartelettes à la forme de votre image")

image_upload = st.file_uploader("Envoyez une image .jpg, .jpeg ou .png (fond blanc, forme noire)", type=["jpg", "jpeg","png"])
longueur = st.text_input("📏 Longueur (=dimension maximale) de la tartelette (mm)", value="100")
hauteur = st.text_input("📐 Hauteur du bord (mm)", value="20")
type_bord = st.selectbox("🎨 Type de bord :", ["Bord plein", "Dentelle petites mailles", "Dentelle maille haute"])
type_impression = st.selectbox("🍰 Appareil et poudre utilisés :", ["Poudre blé luxe et appareil sucré luxe", "Poudre blé luxe et appareil salé", "Poudre blé luxe et appareil vegan", "Poudre sans gluten et appareil sans gluten", "Poudre blé cacao et appareil sucré luxe", "Poudre de macaron et appareil macaron"])


if st.button("Générer et visualiser le GCODE"):
    if not image_upload or not longueur or not hauteur:
        st.warning("Veuillez remplir toutes les cases")
    else:
        try:
            # Convertir longueur et hauteur en float
            longueur_num = float(longueur)
            hauteur_num = float(hauteur)

            gcode, forme = generer_gcode(image_upload, longueur_num, hauteur_num, type_bord, type_impression)

            if gcode == 0:
                st.warning("Veuillez choisir des dimensions plus petites, la taille maximale est longueur: 236mm, largeur: 176mm, hauteur: 99mm")
            
            else :

                st.success("✅ GCODE généré avec succès !")

                steps = [el for el in forme if isinstance(el, fc.Point)]
                plot_controls = PlotControls(style="line", color_type="print_sequence")
                state = State(steps, plot_controls)
                plot_data = PlotData(steps, state)

                for step in steps:
                    step.visualize(state, plot_data, plot_controls)
                plot_data.cleanup()

                fig = plot(plot_data, plot_controls)
                st.plotly_chart(fig, use_container_width=True)

                st.download_button("💾 Télécharger le GCODE", gcode, file_name="Tartelette.gcode")

        except Exception as e:
            st.error(f"Erreur lors de la génération : {e}")