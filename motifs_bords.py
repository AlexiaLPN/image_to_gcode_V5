import fullcontrol as fc 
from math import *

# -------------------------- MOTIFS -------------------------------

def quadrillage(perimetre: float, hauteur: float):
    
    motif = []
    taille_motif = 12
    N = round(perimetre/taille_motif) # nombre de motifs selon x
    a = perimetre/N # taille du motif réelle
    H = round(hauteur/a) # nombre de motifs selon z

    motif.extend(fc.travel_to(fc.Point(x=0,y=0,z=0)))

    for h in range(H):
        for n in range(N):
            motif.append(fc.Point(x=a*n,y=0,z=a*h))
            motif.append(fc.Point(x=a*(n+1/2),y=0,z=a*(h+1/2)))
        motif.append(fc.Point(x=a*N,y=0,z=a*h))
        motif.extend(fc.travel_to(fc.Point(x=0,y=0,z=a*(h+1))))
        for n in range(N):
            motif.append(fc.Point(x=a*n,y=0,z=a*(h+1)))
            motif.append(fc.Point(x=a*(n+1/2),y=0,z=a*(h+1/2)))
        motif.append(fc.Point(x=a*N,y=0,z=a*(h+1)))
        if h<H-1:
            motif.extend(fc.travel_to(fc.Point(x=a*N,y=0,z=a*(h+1)+10)))
            motif.extend(fc.travel_to(fc.Point(x=0,y=0,z=a*(h+1)+10)))
            motif.extend(fc.travel_to(fc.Point(x=0,y=0,z=a*(h+1))))
    
    maxZ = max([element.z for element in motif if type(element).__name__ == 'Point'])

    for element in  motif:
        if  type(element).__name__ == 'Point':
            element.z *= hauteur/maxZ

    return motif

def bosseshautessolides(perimetre: float, hauteur: float):
    
    motif = []

    taille_motif = 20
    etirement = 0.75 # étirement selon z, 1 sinon
    N = round(perimetre/taille_motif) # nombre de motifs selon x
    a = perimetre/N # taille du motif
    s = 20 # nombre de segments des arcs de cercle
    imax = round(hauteur/(a*etirement)-1)

    motif.extend(fc.travel_to(fc.Point(x=0, y=0 ,z=0)))
    
    for i in range(0,imax+1):

        if i != 0:

            motif.extend(fc.travel_to(fc.Point(x=perimetre,y=a*i+10,z=0)))
            motif.extend(fc.travel_to(fc.Point(x=0,y=a*i+10,z=0)))
            motif.extend(fc.travel_to(fc.Point(x=0,y=a*i,z=0))) 

        for n in range(N): #!
            arc1 = fc.arcXY(fc.Point(x=a*(n+1/2),y=a*i,z=0),a/2,-pi,-pi,s)
            if i!=0:
                for element in arc1:
                    y = (element.y-a*i)/(a/2)*(a/2+a/20)+a*i-a/20 #!
                    element.y=y
            motif.extend(arc1)
        
        motif.extend(fc.travel_to(fc.Point(x=0,y=a*(i+1),z=0)))

        for n in range(N): #!
            arc2 = fc.arcXY(fc.Point(x=a*n,y=a*(1/2+i),z=0),a/2,pi/2,-pi/2,s)+fc.arcXY(fc.Point(x=a*(n+1),y=a*(1/2+i),z=0),a/2,pi,-pi/2,s)
            for element in arc2:
                    y = (element.y-a*(1/2+i))/(a/2)*(a/2+a/20)+a*(i+1/2)-a/20 #!
                    element.y=y
            motif.extend(arc2)

    for element in  motif:
        if  type(element).__name__ == 'Point':
            element.z = etirement*element.y
            element.y = 0

    maxZ = max([element.z for element in motif if type(element).__name__ == 'Point'])

    for element in  motif:
        if  type(element).__name__ == 'Point':
            element.z *= hauteur/maxZ
    
    return motif