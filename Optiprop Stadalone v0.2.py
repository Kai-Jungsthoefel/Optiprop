# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:47:12 2020

@author: Kai Jungsthöfel & Lars Schröder
"""
import numpy as np
import stl
from stl import mesh
import numpy
import math
from tabulate import tabulate



print('OptiProp Standalone v0.1')



        # Variablen:
print('Propeller Länge: ')
L = float(input())                     # in mm          #Propeller Länge
print('Luftzug Geschwindigkeit: ')
LGeschwindikeit = float(input())        # in m/s         #Luftzug Geschwindikeit
print('Motor Kv: ')
Kv = float(input())                  # Kv             #Kv rating Motor
print('Batterie Stärke: ')
V = float(input())                   # Volt           #Batterie
print('Achsen Größe: ')
Achse = 5   +0.8                     #in mm         #Achsen größe + Sicherheitsabstand # Standard = 5
print(Achse -0.8)
 


# Konstanten
c = 1 / 6   # Maximalbreite des Propellers
d = 1 / 3   # Entfernung des breitesten Punkt
k = 1 / 20  # Minimalbreite des Propellers
n = 15      # Anzahl der Profilflächen
x = L / n   # Profil Abstand
Alpha = 7   # Optimalwinkel
#Hub Konstanten
InnerRingBreite = 1.6
RingbreiteAussen = 2.5



Gamma = []
v = []
B = []


rps = Kv * V

# Profilgeschwindikeits Liste
for i in range(n+1):
    v[i] = v.append(0)
    Gamma[i] = Gamma.append(0)
    B[i] = B.append(0)

for i in range(1, n+1):
    # Profilgeschwindikeit Rechnung
    v[i] = 2 * math.pi * (rps / 60) * ((x / 1000) * i)

    # Winkel
    Gamma[i] = -math.radians(math.degrees(math.atan(LGeschwindikeit / v[i])) + Alpha)

    # Profilbreite
    B[i] = ((k * L - c * L) / (L - d * L) ** 2 * (x * (i + 1) - d * L) ** 2 + c * L)





#////// UI \\\\\\\
UI = []
for i in range(1, n+1):
    UI.append([int(v[i]),round(math.degrees(Gamma[i])*(-1),2)])
print(tabulate(UI, headers=['Profil Geschwindigkeit in m/s','Profil Winkel']))






# Standart Airfoil
X = [
                0, 0.0005, 0.001, 0.002, 0.004, 0.008, 0.012, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16,
                0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48, 0.5, 0.52,
                0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88,
                0.9, 0.92, 0.94, 0.96, 0.97, 0.98, 0.99, 1
            ]

YO = [
                0, 0.0023390, 0.0037271, 0.0058025, 0.0089238, 0.0137350, 0.0178581, 0.0253735, 0.0330215, 0.0391283,
                0.0442753, 0.0487571, 0.0564308, 0.0629981, 0.0686204, 0.0734360, 0.0775707, 0.0810687, 0.0839202,
                0.0861433, 0.0878308, 0.0890840, 0.0900016, 0.0906804, 0.0911857, 0.0915079, 0.0916266, 0.0915212,
                0.0911712, 0.0905657, 0.0897175, 0.0886427, 0.0873572, 0.0858772, 0.0842145, 0.0823712, 0.0803480,
                0.0781451, 0.0757633, 0.0732055, 0.0704822, 0.0676046, 0.0645843, 0.0614329, 0.0581599, 0.0547675,
                0.0512565, 0.0476281, 0.0438836, 0.0400245, 0.0360536, 0.0319740, 0.0277891, 0.0235025, 0.0191156,
                0.0146239, 0.0100232, 0.0076868, 0.0053335, 0.0029690, 0
            ]

YU = [
                0, -.0046700, -.0059418, -.0078113, -.0105126, -.0142862, -.0169733, -.0202723, -.0226056, -.0245211,
                -.0260452, -.0271277, -.0284595, -.0293786, -.0299633, -.0302404, -.0302404, -.0300490, -.0296656,
                -.0296656, -.0285181, -.0278164, -.0270696, -.0263079, -.0255565, -.0248176, -.0240870, -.0233606,
                -.0226341, -.0219042, -.0211708, -.0204353, -.0196986, -.0189619, -.0182262, -.0174914, -.0167572,
                -.0160232, -.0152893, -.0145551, -.0138207, -.0130862, -.0123515, -.0116169, -.0108823, -.0101478,
                -.0094133, -.0086788, -.0079443, -.0072098, -.0064753, -.0057408, -.0050063, -.0042718, -.0035373,
                -.0028028, -.0020683, -.0017011, -.0013339, -.0009666, 0
            ]


 #Sekundäre Koordinatenliste
XO2 = []
XO3 = []
for i in range(len(X)):
    XO2[i] = XO2.append(0)
    XO3[i] = XO3.append(0)
    
XU2 = []
XU3 = []
for i in range(len(X)):
    XU2[i] = XU2.append(0)
    XU3[i] = XU3.append(0)


YO2 = []
YO3 = []
for i in range(len(YO)):
    YO2[i] = YO2.append(0)
    YO3[i] = YO3.append(0)
    
YU2 = []
YU3 = []
for i in range(len(YU)):
    YU2[i] = YU2.append(0)
    YU3[i] = YU3.append(0)









# Die Reihenfolge der Kordinaten Wird Definiert um zwei Profile mit einander zu Verbinden
Eckfolge = []
f = 0
for i in range(len(X)*4):
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,0+f+(len(X)*2)])
    else:
        Eckfolge.append([0+f+(len(X)*2),1+f+(len(X)*2),1+f])
        f += 1

Eckfolge[-1].insert(2,0)
Eckfolge[-1].remove(244)







Propeller = []

KordC = []



for p in range(1,n+1): #Zum Testen nur ein Profil berechnen standard = (1,n+1)

    
    Kord = []       #Kord wird Erstellt bzw. Alle kordinaten werden bei jedem p Gelöscht.
    
    # Koordinaten Skalieren und in die Zweittabellen Übertragen
    for i in range(len(X)):
        XO2[i] = (X[i] * math.cos(Gamma[p]) - YO[i] * math.sin(Gamma[p])) * B[p]
        if p <= n-1:
            XO3[i] = (X[i] * math.cos(Gamma[p+1]) - YO[i] * math.sin(Gamma[p+1])) * B[p+1]
    for i in range(len(X)):
        XU2[i] = (X[i] * math.cos(Gamma[p]) - YU[i] * math.sin(Gamma[p])) * B[p]
        if p <= n-1:
            XU3[i] = (X[i] * math.cos(Gamma[p+1]) - YU[i] * math.sin(Gamma[p+1])) * B[p+1]
            
    for i in range(len(YO)):
        YO2[i] = (X[i] * math.sin(Gamma[p]) + YO[i] * math.cos(Gamma[p])) * B[p]
        if p <= n-1:
            YO3[i] = (X[i] * math.sin(Gamma[p+1]) + YO[i] * math.cos(Gamma[p+1])) * B[p+1]
    for i in range(len(YU)):
        YU2[i] = (X[i] * math.sin(Gamma[p]) + YU[i] * math.cos(Gamma[p])) * B[p]
        if p <= n-1:
            YU3[i] = (X[i] * math.sin(Gamma[p+1]) + YU[i] * math.cos(Gamma[p+1])) * B[p+1]
    
   
    for i in range(len(X)):
        
        #Kordinaten Array für Numpy-STL für ein Profil 
        # [[x,y,z]
        #  [x,y,z]...]
        
        xk = XO2[i]
        yk = YO2[i]
        zk = x*(p)
       
        Kordin = [zk,xk,yk] 
        Kord.append(Kordin)
        
        
    XU2.reverse()           #Damit die Koordinaten im Kreis um die airfoil gehen werden die Unteren Listen Rückwärts abglesen.
    YU2.reverse()
    for i in range(len(X)):
        xk = XU2[i]
        yk = YU2[i]
        zk = x*(p)
       
        Kordin = [zk,xk,yk]
        Kord.append(Kordin)
    
    if p == 2:              #2tes Profil Speichen zum Verpinden mit dem Hub
        KordC = Kord
    for i in range(len(X)):  
        # Es werden zwei Profile benötigt um Dreiecke zu bilden. Das Zweite Profil muss noch erstellt werden und in die gleiche liste hinter dem Ersten Profil Geschrieben werden.
        xk = XO3[i]
        yk = YO3[i]
        zk = x*(p+1)
       
        Kordin = [zk,xk,yk]
        Kord.append(Kordin)
        
        
    XU3.reverse()           #Damit die Koordinaten im Kreis um die airfoil gehen werden die Unteren Listen Rückwärts abglesen.
    YU3.reverse()
    for i in range(len(X)):
        xk = XU3[i]
        yk = YU3[i]
        zk = x*(p+1)
       
        Kord.append([zk,xk,yk])
    
    
    

   
    if p <= n-1 and p != 1:
        DoppelProfilHülle = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                DoppelProfilHülle.vectors[i][j] = np.array(Kord)[f[j],:]
        Propeller.append(DoppelProfilHülle.data)
    
 
#//////End Schließung\\\\\\\
Eckfolge = []
f = 0                       #Halb so größe eckfolge da nur ein Profil untereinander Verbunden wird
for i in range(len(X)*2):
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,0-f+(len(X)*2-1)])
    else:
        Eckfolge.append([0-f+(len(X)*2-2),1-f+(len(X)*2-2),1+f])
        f += 1

DoppelProfilHülle = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        DoppelProfilHülle.vectors[i][j] = np.array(Kord)[f[j],:]
Propeller.append(DoppelProfilHülle.data)

        
        
        
        

        
    
    
    
#//////  HUB \\\\\\\#

#HubOffset
xO = 0
yO = (Achse/2)+InnerRingBreite+RingbreiteAussen
zO = -3
    
    
    #///// Innerer Kreis \\\\\

Achse2 = 0
HubTopIn = []
HubBottomIn = []
HubRimTop = []
HubRimBottom = []
for i in range(19): #Koordinaten Liste für Oberen und Unteren Halbkreis
    i -= 4
    i = i*10
    
    HubTopIn.append(    [math.cos(math.radians(i))*(Achse/2)+xO,    math.sin(math.radians(i))*(Achse/2)+yO,   5+zO])
    
    HubBottomIn.append( [math.cos(math.radians(i))*(Achse/2)+xO,    math.sin(math.radians(i))*(Achse/2)+yO,  -5+zO])
    
Achse2 = Achse + InnerRingBreite*2    
for i  in range(19): # Umgedrehtehälfte der Kordinaten liste
    p = 140-i*10
    
    HubTopIn.append(    [math.cos(math.radians(p))*(Achse2/2)+xO,    math.sin(math.radians(p))*(Achse2/2)+yO,   5+zO])
    
    HubBottomIn.append( [math.cos(math.radians(p))*(Achse2/2)+xO,    math.sin(math.radians(p))*(Achse2/2)+yO,  -5+zO])
    if p <= 100:        #Koordinaten liste für den Oberen und Unteren Rand
        HubRimTop.append(   [math.cos(math.radians(p))*(Achse2/2)+xO,    math.sin(math.radians(p))*(Achse2/2)+yO,   5+zO])    
        HubRimBottom.append([math.cos(math.radians(p))*(Achse2/2)+xO,    math.sin(math.radians(p))*(Achse2/2)+yO,  -5+zO])
       


Eckfolge = []   #Eckfolge für Oberen und Unteren Halbkreis
f = 0    
for i in range(18*2):
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,0-f+(18*2)])
    else:
        Eckfolge.append([0-f+(18*2),1-f+(18*2),0+f])
        f += 1
  

Hub = []

# Unteren und Oberen Halbkreis Erstellen      
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubTopIn)[f[j],:]

Hub.append(Hubmesh.data)
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubBottomIn)[f[j],:]    
Hub.append(Hubmesh.data)
              

# Koordinaten liste aus der Ober und Unterhälfte für die Hülle
HubTopIn.reverse() #HubTop wird umgedreht eingesetzt

HubCompleteIn = HubBottomIn+ HubTopIn



#Eckfolge für die Hülle
Eckfolge = []
f = 0    
for i in range(18*2+12):
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,2-f+(18*4)])
    else:
        Eckfolge.append([2-f+(18*4),3-f+(18*4),0+f])
        f += 1
# Zum Schließen der Form 
Eckfolge.append([0,38,75])
Eckfolge.append([38,37,0])

# Körper wird Erstellt   
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubCompleteIn)[f[j],:]    
Hub.append(Hubmesh.data)     





        
        #//// Äußere Kreis \\\\\\
HubRimTop.reverse()
HubRimBottom.reverse()
HubTop = []
HubBottom = []
for i in range(19): #Koordinaten Liste für Oberen und Unteren Halbkreis
    i -= 9
    i = i*10
    
    HubTop.append(      [math.cos(math.radians(i))*(Achse2/2)+xO,   math.sin(math.radians(i))*(Achse2/2)+yO       ,3+zO])
    
    HubBottom.append(   [math.cos(math.radians(i))*(Achse2/2)+xO,   math.sin(math.radians(i))*(Achse2/2)+yO       ,-3+zO])
    if i >= -40:        #Koordinaten liste für den Oberen und Unteren Rand
        HubRimTop.append([math.cos(math.radians(i))*(Achse2/2)+xO,   math.sin(math.radians(i))*(Achse2/2)+yO       ,3+zO])
        HubRimBottom.append([math.cos(math.radians(i))*(Achse2/2)+xO,   math.sin(math.radians(i))*(Achse2/2)+yO       ,-3+zO])
        
Kord = []     
Achse2 += RingbreiteAussen*2    
for i  in range(19): # Umgedrehtehälfte der Kordinaten liste
    p = 90-i*10
    
    HubTop.append(      [math.cos(math.radians(p))*(Achse2/2)+xO,   math.sin(math.radians(p))*(Achse2/2)+yO       ,3+zO])
    
    HubBottom.append(   [math.cos(math.radians(p))*(Achse2/2)+xO,   math.sin(math.radians(p))*(Achse2/2)+yO       ,-3+zO])
    
    #Koordinaten zum verbinden mit dem Kreis
    Kord.append(        [math.cos(math.radians(p))*(Achse2/2)+xO,   math.sin(math.radians(p))*(Achse2/2)+yO       ,3+zO])
Kord.reverse()
for i  in range(19): 
    p = 90-i*10
    Kord.append(        [math.cos(math.radians(p))*(Achse2/2)+xO,   math.sin(math.radians(p))*(Achse2/2)+yO       ,-3+zO])  


Eckfolge = []   #Eckfolge für Oberen und Unteren Halbkreis
f = 0    
for i in range(18*2):
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,0-f+(18*2)])
    else:
        Eckfolge.append([0-f+(18*2),1-f+(18*2),0+f])
        f += 1
  



# Unteren und Oberen Halbkreis Erstellen      
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubTop)[f[j],:]

Hub.append(Hubmesh.data)
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubBottom)[f[j],:]    
Hub.append(Hubmesh.data)
              

# Koordinaten liste aus der Ober und Unterhälfte für die Hülle
HubTop.reverse() #HubTop wird umgedreht eingesetzt

HubComplete = HubBottom + HubTop



#Eckfolge für die Hülle
Eckfolge = []
f = 0    
for i in range(10):
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,2-f+(18*4)])
    else:
        Eckfolge.append([2-f+(18*4),3-f+(18*4),0+f])
        f += 1
# Zum Schließen der Form 
Eckfolge.append([0,38,75])
Eckfolge.append([38,37,0])
Eckfolge.append([18,19,56])
Eckfolge.append([18,57,56])

# Körper wird Erstellt   
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubComplete)[f[j],:]    
Hub.append(Hubmesh.data)       
    




#////////HubRim\\\\\\\\\

Eckfolge = []
f = 0    
for i in range(14*2-2):     #Eckfolge für den Oberen und Unteren Rand
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,1+f+(15)])
    else:
        Eckfolge.append([1+f+(14),2+f+(14),0+f])
        f += 1
        
#Rand wird dem Mesh hinzugefügt
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubRimTop)[f[j],:]    
Hub.append(Hubmesh.data)  
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(HubRimBottom)[f[j],:]    
Hub.append(Hubmesh.data) 




    #/////// Verbindungs Stück \\\\\\\\ 
   
Kord.reverse()
for i in range(18*2):   #Koordinaten für einen Kreis zum verbinden mit dem Hub
    i -= 18
    i = i*10
    Kord.append(    [Achse2/2+xO,  (math.cos(math.radians(i))*6)+yO,    (math.sin(math.radians(i))*3)+zO])
 
    
    
Eckfolge = []
f = 0    
for i in range(18*4):     #Für den Kreis mit dem Hub
    if i % 2 == 0:
        Eckfolge.append([0+f,1+f,2+f+(18*2)])
    else:
        Eckfolge.append([1+f+(18*2),2+f+(18*2),0+f])
        f += 1
Eckfolge.append([36,37,38])
Eckfolge.append([73,38,36])

# Körper wird Erstellt   
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
Hub.append(Hubmesh.data)    
 


#Kreis an die Airfoil besfestigen


Kord = []
for i in range(18*2):   #Koordinaten für einen Kreis zum verbinden mit dem Hub
    i -= 18
    i = i*10
    Kord.append(    [Achse2/2+xO,  (math.cos(math.radians(i))*6)+yO,    (math.sin(math.radians(i))*3)+zO])
Kord.reverse()    
Kord = Kord+KordC


Eckfolge = []
f = 0
g = 0
h = 0
for i in range(158-1):
    if h <= 3.38888:
        Eckfolge.append([36+f,37+f,0+g])
        f += 1
        h += 0.9
        
    else:
        Eckfolge.append([36+f,0+g,1+g])
        
        g += 1
        h -= 3
        if g == 36:
            g = 0
Eckfolge.append([157, 35, 0])
    
        
Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(Eckfolge):
    for j in range(3):
        Hubmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
Hub.append(Hubmesh.data)    
 
    
    #///////Export\\\\\\


Propeller = Propeller+Hub    
    
            
Propeller = mesh.Mesh(numpy.concatenate(Propeller))
                                        
                                    
                         

        
Propeller.save('Propeller.stl')  
    
    
    
    
input('Press ENTER to exit')    
Propeller.save("PropellerL" + str(int(L)) + "Kv" + str(int(Kv)) + "Lg" + str(int(LGeschwindigkeit)) + ".stl")  
    
    
    
    

