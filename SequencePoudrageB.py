homogeneisation = """
;HOMOGENEISATION
;Circle, center
G3 X116.5 Y58.5 F10000.0 R5.0
G3 X116.5 Y38.5 F10000.0 R10.0
G3 X116.5 Y68.5 F10000.0 R15.0
G3 X116.5 Y28.5 F10000.0 R20.0
G3 X116.5 Y78.5 F10000.0 R25.0
G3 X116.5 Y18.5 F10000.0 R30.0
G3 X116.5 Y88.5 F10000.0 R35.0
G3 X116.5 Y8.5 F10000.0 R40.0
G3 X116.5 Y98.5 F10000.0 R45.0
G3 X116.5 Y-1.5 F10000.0 R50.0
G3 X116.5 Y108.5 F10000.0 R55.0
G3 X116.5 Y-11.5 F10000.0 R60.0
G3 X116.5 Y118.5 F10000.0 R65.0
G3 X116.5 Y-21.5 F10000.0 R70.0
;Half of a circle, edges
G1 X126.5 Y-21.5 F10000.0
G3 X126.5 Y118.5 F10000.0 R70.0
G1 X106.5 Y118.5 F10000.0
G3 X106.5 Y-21.5 F10000.0 R70.0
G1 X136.5 Y-21.5 F10000.0
G3 X136.5 Y118.5 F10000.0 R70.0
G1 X96.5 Y118.5 F10000.0
G3 X96.5 Y-21.5 F10000.0 R70.0
G1 X146.5 Y-21.5 F10000.0
G3 X146.5 Y118.5 F10000.0 R70.0
G1 X86.5 Y118.5 F10000.0
G3 X86.5 Y-21.5 F10000.0 R70.0
;Quarter of a circle, corners
G1 X166.5 Y-21.5 F10000.0
G3 X216.5 Y28.5 F10000.0 R50.0
G1 X216.5 Y68.5 F10000.0
G3 X166.5 Y118.5 F10000.0 R50.0
G1 X66.5 Y118.5 F10000.0
G3 X16.5 Y68.5 F10000.0 R50.0
G1 X16.5 Y28.5 F10000.0
G3 X66.5 Y-21.5 F10000.0 R50.0
;Quarter of a circle, corners
G1 X166.5 Y-21.5 F10000.0
G3 X216.5 Y28.5 F10000.0 R50.0
G1 X216.5 Y68.5 F10000.0
G3 X166.5 Y118.5 F10000.0 R50.0
G1 X66.5 Y118.5 F10000.0
G3 X16.5 Y68.5 F10000.0 R50.0
G1 X16.5 Y28.5 F10000.0
G3 X66.5 Y-21.5 F10000.0 R50.0
;Quarter of a circle, corners
G1 X166.5 Y-21.5 F10000.0
G3 X216.5 Y28.5 F10000.0 R50.0
G1 X216.5 Y68.5 F10000.0
G3 X166.5 Y118.5 F10000.0 R50.0
G1 X66.5 Y118.5 F10000.0
G3 X16.5 Y68.5 F10000.0 R50.0
G1 X16.5 Y28.5 F10000.0
G3 X66.5 Y-21.5 F10000.0 R50.0
M400 
G4 S2"""

poudrageA = """;Mise en position de non securite
G1 Y120.0 F10000.0
G1 X15.0 F10000.0
; ------ End Deplacement hauteur snippet
M400 
M42 P3 S0.2
G92 U0 V0 W0 A0
G1 V200.0 A300.0 F1000.0
G92 U0 V0 W0 A0
G1 U1000 V1575 W125 A2300 F3000
; ------ After powdering snippet
M400 
M42 P4 S0
G92 U0 V0 W0 A20
G1 A0.0
; ------ End After powdering snippet
M42 P3 S0.0
G4 S1
M42 P5 S1"""

poudrageB = """;Mise en position de non securite
G1 Y120.0 F10000.0
G1 X15.0 F10000.0
; ------ End Deplacement hauteur snippet
M400 
M42 P3 S0.2
G92 U0 V0 W0 A0
G1 V200.0 A300.0 F3000.0
G92 U0 V0 W0 A0
G1 U800 V1187.5 W82.5 A1650 F3000
; ------ After powdering snippet
M400 
M42 P4 S0
G92 U0 V0 W0 A20
G1 A0.0
; ------ End After powdering snippet
M42 P3 S0.0
G4 S1
M42 P5 S1"""

poudrageC = """;Mise en position de non securite
G1 Y120.0 F10000.0
G1 X15.0 F10000.0
; ------ End Deplacement hauteur snippet
M400 
M42 P3 S0.2
G92 U0 V0 W0 A0
G1 V200.0 A300.0 F3000.0
G92 U0 V0 W0 A0
G1 U1800 V2762.5 W207.5 A3950 F3000
; ------ After powdering snippet
M400 
M42 P4 S0
G92 U0 V0 W0 A20
G1 A0.0
; ------ End After powdering snippet
M42 P3 S0.0
G4 S1
M42 P5 S1"""

def poudrage_initialB ():

    gCode_poudrage_initial = """ 
; DEBUT DU CODE INITIAL ALEXANDRE
;LAYER_CHANGE
;Z:0.6
;HEIGHT:0.6
G1 F2400.0 E-1.0
;Pour le Z = 0.6
; ------ Pump off snippet
M42 P5 S0
; ------ End Pump off snippet
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U100 B100 P10 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R0 U0 B0 P0 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F1
M150 R255 U100 B0 P10 S1 F0
;sequence d'initialisation
; ------ Homing snippet
;sequence Homing
G92 U0 V0 W0 A0
G28 Z
G28 X
G28 Y
; ------ End Homing snippet
; ------ Deplacement normal snippet
;Mise en position de securite
G1 Y-10.0 F5000.0
G1 X380.0 F5000.0
; ------ End deplacement normal snippet
G1 Z-20.0
M400 
M42 P3 S0.04
G92 U0 V0 W0 A0
G1 V200.0 A300.0 F1000.0
G92 U0 V0 W0 A0
G1 U2900 V4567.5 W362.5 A6700 F3000 ##################################################################
; ------ After powdering snippet
M400 
M42 P4 S0
G92 U0 V0 W0 A20
G1 A0.0
; ------ End After powdering snippet
G28 Z
M400 
M42 P3 S0.0
G1 X30.0 Y30.0 F10000.0
M400 
M42 P3 S0
G1 Z50 F5000
G92 Z0
G1 Z5.0 F10000.0 E1.0
;Circle, center
G3 X116.5 Y58.5 F10000.0 R5.0
G3 X116.5 Y38.5 F10000.0 R10.0
G3 X116.5 Y68.5 F10000.0 R15.0
G3 X116.5 Y28.5 F10000.0 R20.0
G3 X116.5 Y78.5 F10000.0 R25.0
G3 X116.5 Y18.5 F10000.0 R30.0
G3 X116.5 Y88.5 F10000.0 R35.0
G3 X116.5 Y8.5 F10000.0 R40.0
G3 X116.5 Y98.5 F10000.0 R45.0
G3 X116.5 Y-1.5 F10000.0 R50.0
G3 X116.5 Y108.5 F10000.0 R55.0
G3 X116.5 Y-11.5 F10000.0 R60.0
G3 X116.5 Y118.5 F10000.0 R65.0
G3 X116.5 Y-21.5 F10000.0 R70.0
;Half of a circle, edges
G1 X126.5 Y-21.5 F10000.0
G3 X126.5 Y118.5 F10000.0 R70.0
G1 X106.5 Y118.5 F10000.0
G3 X106.5 Y-21.5 F10000.0 R70.0
G1 X136.5 Y-21.5 F10000.0
G3 X136.5 Y118.5 F10000.0 R70.0
G1 X96.5 Y118.5 F10000.0
G3 X96.5 Y-21.5 F10000.0 R70.0
G1 X146.5 Y-21.5 F10000.0
G3 X146.5 Y118.5 F10000.0 R70.0
G1 X86.5 Y118.5 F10000.0
G3 X86.5 Y-21.5 F10000.0 R70.0
;Quarter of a circle, corners
G1 X166.5 Y-21.5 F10000.0
G3 X216.5 Y28.5 F10000.0 R50.0
G1 X216.5 Y68.5 F10000.0
G3 X166.5 Y118.5 F10000.0 R50.0
G1 X66.5 Y118.5 F10000.0
G3 X16.5 Y68.5 F10000.0 R50.0
G1 X16.5 Y28.5 F10000.0
G3 X66.5 Y-21.5 F10000.0 R50.0
G1 Z3.0 F10000.0 E1.0
;Quarter of a circle, corners
G1 X166.5 Y-21.5 F10000.0
G3 X216.5 Y28.5 F10000.0 R50.0
G1 X216.5 Y68.5 F10000.0
G3 X166.5 Y118.5 F10000.0 R50.0
G1 X66.5 Y118.5 F10000.0
G3 X16.5 Y68.5 F10000.0 R50.0
G1 X16.5 Y28.5 F10000.0
G3 X66.5 Y-21.5 F10000.0 R50.0
;Quarter of a circle, corners
G1 X166.5 Y-21.5 F10000.0
G3 X216.5 Y28.5 F10000.0 R50.0
G1 X216.5 Y68.5 F10000.0
G3 X166.5 Y118.5 F10000.0 R50.0
G1 X66.5 Y118.5 F10000.0
G3 X16.5 Y68.5 F10000.0 R50.0
G1 X16.5 Y28.5 F10000.0
G3 X66.5 Y-21.5 F10000.0 R50.0
M400 
G4 S2
; ------ Pump on snippet
M42 P5 S1
; ------ End Pump on snippet
G92 E0
G1 X79.16 Y30.195 F3000.0
G1 Z0.6 F1800.0
G1 F2400.0 E2.0
;TYPE:External perimeter
;WIDTH:0.999999
G1 F6000.0
; FIN DU CODE INITIAL ALEXANDRE
"""
    
    return gCode_poudrage_initial

def poudrage_zB(Z,nombre_etages:int,numero_etage:int):
    """
    nombre_etages = nombre d'étages de pièces, fonctionne jusqu'à 5 étages \n
    numero_etage = numéro de l'étage qui vient d'être fait
    """
    # Poudrage Initial I : G1 U2900 V4567.5 W362.5 A6700 F3000
    # Poudrage A : G1 U1000 V1575 W125 A2300 F3000
    # Poudrage B : G1 U800 V1187.5 W82.5 A1650 F3000
    # Poudrage C (=A + B) : G1 U1800 V2762.5 W207.5 A3950 F3000 (= A + B)
    # pour 2 étages de pièces : I - 1 - A+B - 2
    # pour 3 étages de pièces : I - 1 - A - 2 - B - 3
    # pour 4 étages de pièces : I - 1 2 - A - 3 - B - 4
    # pour 5 étages de pièces : I - 1 2 - A - 3 - B - 4 5
    # pour 6 étages de pièces : I - 1 2 - A - 3 4 - B - 5 6
    # pour 7 étages de pièces : I - 1 2 3 - A - 4 5 - B - 6 7
    
    gCode_poudrage_z = """; Pas de poudrage à cet étage"""

    if nombre_etages == 2 and numero_etage == 1:
        gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageC + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation
        
    elif nombre_etages == 3:
        if numero_etage == 1:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageA + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation
        
        elif numero_etage == 2:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageB + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation

    elif nombre_etages == 4:
        if numero_etage == 2:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageA + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation
        
        elif numero_etage == 3:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageB + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation

    elif nombre_etages == 5:
        if numero_etage == 2:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageA + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation
        
        elif numero_etage == 3:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageB + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation

    elif nombre_etages == 6:
        if numero_etage == 2:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageA + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation
        
        elif numero_etage == 4:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageB + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation

    elif nombre_etages == 7:
        if numero_etage == 3:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageA + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation
        
        elif numero_etage == 5:
            gCode_poudrage_z = """
;-------Move head up
G1 Z""" + str(Z+10) + poudrageB + """
G0 F2000 Z""" +str(Z)+ """
""" + homogeneisation

    return gCode_poudrage_z