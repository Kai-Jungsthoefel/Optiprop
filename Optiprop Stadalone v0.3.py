# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:47:12 2020

@author: Kai Jungsthöfel & Lars Schröder
"""
import vtkplotlib as vpl
from stl.mesh import Mesh
import numpy as np
import stl
from stl import mesh
import numpy
import math
from tabulate import tabulate
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButtonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(40, 210, 75, 23))
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        
        self.pushButtonExport = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExport.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.pushButtonExport.setObjectName("pushButtonExport")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(32, 42, 209, 151))
        self.widget.setObjectName("widget")
        
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        
        self.labelPropellerVariablen = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPropellerVariablen.setFont(font)
        self.labelPropellerVariablen.setObjectName("labelPropellerVariablen")
        
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelPropellerVariablen)
        self.labelL = QtWidgets.QLabel(self.widget)
        self.labelL.setObjectName("labelL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelL)
        
        self.spinBoxL = QtWidgets.QSpinBox(self.widget)
        self.spinBoxL.setMinimum(20)
        self.spinBoxL.setMaximum(1000)
        self.spinBoxL.setSingleStep(10)
        self.spinBoxL.setProperty("value", 100)
        self.spinBoxL.setObjectName("spinBoxL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxL)
        
        self.labelLg = QtWidgets.QLabel(self.widget)
        self.labelLg.setObjectName("labelLg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelLg)
        
        self.spinBoxLg = QtWidgets.QSpinBox(self.widget)
        self.spinBoxLg.setMaximum(1000)
        self.spinBoxLg.setProperty("value", 10)
        self.spinBoxLg.setObjectName("spinBoxLg")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBoxLg)
        
        self.labelKv = QtWidgets.QLabel(self.widget)
        self.labelKv.setObjectName("labelKv")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelKv)
        
        self.spinBoxKv = QtWidgets.QSpinBox(self.widget)
        self.spinBoxKv.setMinimum(100)
        self.spinBoxKv.setMaximum(10000)
        self.spinBoxKv.setSingleStep(100)
        self.spinBoxKv.setProperty("value", 2200)
        self.spinBoxKv.setObjectName("spinBoxKv")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBoxKv)
        
        self.labelU = QtWidgets.QLabel(self.widget)
        self.labelU.setObjectName("labelU")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelU)
        
        self.spinBoxU = QtWidgets.QDoubleSpinBox(self.widget)
        self.spinBoxU.setDecimals(1)
        self.spinBoxU.setMinimum(1.0)
        self.spinBoxU.setMaximum(100.0)
        self.spinBoxU.setSingleStep(3.7)
        self.spinBoxU.setProperty("value", 11.1)
        self.spinBoxU.setObjectName("spinBoxU")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBoxU)
        
        self.labelA = QtWidgets.QLabel(self.widget)
        self.labelA.setObjectName("labelA")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelA)
        
        self.spinBoxA = QtWidgets.QDoubleSpinBox(self.widget)
        self.spinBoxA.setDecimals(1)
        self.spinBoxA.setMinimum(1.0)
        self.spinBoxA.setMaximum(20.0)
        self.spinBoxA.setProperty("value", 5.0)
        self.spinBoxA.setObjectName("spinBoxA")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBoxA)
        
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(270, 40, 701, 400))
        self.widget1.setObjectName("widget1")
        
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.widget2 = QtWidgets.QWidget(self.widget1)
        self.widget2.setObjectName("widget2")
        
        self.gridLayout.addWidget(self.widget2, 0, 0, 1, 1)
        
        self.widget_2 = QtWidgets.QWidget(self.widget1)
        self.widget_2.setObjectName("widget_2")
        
        self.bild = vpl.QtFigure("bild")
        self.gridLayout.addWidget(self.bild, 0, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.labelX = QtWidgets.QLabel(MainWindow)
        self.labelX.setGeometry(QtCore.QRect(20, 440, 600, 16))
        self.labelX.setObjectName("labelX")
        
        self.table = QtWidgets.QTableWidget(MainWindow)
        self.table.setGeometry(QtCore.QRect(20, 240, 256, 192))
        
        
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButtonGenerate.clicked.connect(self.Code)
        self.pushButtonExport.clicked.connect(self.Export)
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OptiProp v0.3"))
        self.pushButtonGenerate.setText(_translate("MainWindow", "Generate"))
        self.pushButtonExport.setText(_translate("MainWindow", "Export"))
        self.labelPropellerVariablen.setText(_translate("MainWindow", "Propeller Variablen:"))
        self.labelL.setText(_translate("MainWindow", "Propellerlänge in mm:"))
        self.labelLg.setText(_translate("MainWindow", "Luftzuggeschwindigkeit in m/s:"))
        self.labelKv.setText(_translate("MainWindow", "Motor Kv:"))
        self.labelU.setText(_translate("MainWindow", "Batterie Stärke in V:"))
        self.labelA.setText(_translate("MainWindow", "Achens Durchmesser in mm:"))
        
        
 
    
    
    
    
    
        
    def Code(self):
                
                # -*- coding: utf-8 -*-
        """
        Created on Mon Mar 30 12:47:12 2020
        
        @author: Kai Jungsthöfel & Lars Schröder
        """
        
        
        
        
        
        
        
        
                # Variablen:
        
        L = float(self.spinBoxL.value())                     # in mm          #Propeller Länge
        self.L = L
        LGeschwindigkeit = float(self.spinBoxLg.value())        # in m/s         #Luftzug Geschwindikeit
        self.LGeschwindigkeit = LGeschwindigkeit
        Kv = float(self.spinBoxKv.value())                  # Kv             #Kv rating Motor
        self.Kv = Kv
        V = float(self.spinBoxU.value())                   # Volt           #Batterie
        self.V = V
        Achse = float(self.spinBoxA.value())   +0.8                     #in mm         #Achsen größe + Sicherheitsabstand # Standard = 5
        self.Achse = Achse
         
        
        
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
        Ringabstand = 0.8
        
        
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
            Gamma[i] = -math.radians(math.degrees(math.atan(LGeschwindigkeit / v[i])) + Alpha)
        
            # Profilbreite
            B[i] = ((k * L - c * L) / (L - d * L) ** 2 * (x * (i + 1) - d * L) ** 2 + c * L)
        
        
        
        
        
        #////// UI \\\\\\\
        UI = []
        for i in range(1, n+1):
            UI.append([int(v[i]),round(math.degrees(Gamma[i])*(-1),2)])
        
        self.UI = UI
        self.labelX.setText("")
        
        
        
        
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
                Eckfolge.append([0+f+(len(X)*2),1+f,0+f])
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
                DoppelProfilHulle = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
                for i, f in enumerate(Eckfolge):
                    for j in range(3):
                        DoppelProfilHulle.vectors[i][j] = np.array(Kord)[f[j],:]
                Propeller.append(DoppelProfilHulle.data)
            
         
        #//////End Schließung\\\\\\\
        Eckfolge = []
        f = 0                       #Halb so größe eckfolge da nur ein Profil untereinander Verbunden wird
        for i in range(len(X)*2):
            if i % 2 == 0:
                Eckfolge.append([0-f+(len(X)*2-1),1+f,0+f])
            else:
                Eckfolge.append([1+f,1-f+(len(X)*2-2),0-f+(len(X)*2-2)])
                f += 1
        
        DoppelProfilHulle = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                DoppelProfilHulle.vectors[i][j] = np.array(Kord)[f[j],:]
        Propeller.append(DoppelProfilHulle.data)
        
                
                
                
                
        
                
            
            
            
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
               
        
        Eckfolge = []   #Eckfolge für Oberen  Halbkreis
        f = 0    
        for i in range(18*2):
            if i % 2 == 0:
                Eckfolge.append([0-f+(18*2),1+f,0+f])
            else:
                Eckfolge.append([0+f,1-f+(18*2),0-f+(18*2)])
                f += 1
          
        
        Hub = []
        
        # Unteren und Oberen Halbkreis Erstellen      
        Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Hubmesh.vectors[i][j] = np.array(HubTopIn)[f[j],:]
                
        Eckfolge = []   #Eckfolge für  Unteren Halbkreis
        f = 0    
        for i in range(18*2):
            if i % 2 == 0:
                Eckfolge.append([0+f,1+f,0-f+(18*2)])
            else:
                Eckfolge.append([0-f+(18*2),1-f+(18*2),0+f])
                f += 1
        
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
                Eckfolge.append([2-f+(18*4),1+f,0+f])
            else:
                Eckfolge.append([0+f,3-f+(18*4),2-f+(18*4)])
                f += 1
        # Zum Schließen der Form 
        Eckfolge.append([0,38,75])
        Eckfolge.append([0,37,38])
        
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
        
        
        Eckfolge = []   #Eckfolge für Oberen  Halbkreis
        f = 0    
        for i in range(18*2):
            if i % 2 == 0:
                Eckfolge.append([0-f+(18*2),1+f,0+f])
            else:
                Eckfolge.append([0+f,1-f+(18*2),0-f+(18*2)])
                f += 1
          
        
        
        
        # Unteren und Oberen Halbkreis Erstellen      
        Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Hubmesh.vectors[i][j] = np.array(HubTop)[f[j],:]
                
        Eckfolge = []   #Eckfolge für  Unteren Halbkreis
        f = 0    
        for i in range(18*2):
            if i % 2 == 0:
                Eckfolge.append([0+f,1+f,0-f+(18*2)])
            else:
                Eckfolge.append([0-f+(18*2),1-f+(18*2),0+f])
                f += 1
        
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
                Eckfolge.append([2-f+(18*4),1+f,0+f])
            else:
                Eckfolge.append([0+f,3-f+(18*4),2-f+(18*4)])
                f += 1
        # Zum Schließen der Form 
        Eckfolge.append([0,38,75])#
        Eckfolge.append([0,37,38])#
        Eckfolge.append([56,19,18])#
        Eckfolge.append([18,57,56])#
        
        # Körper wird Erstellt   
        Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Hubmesh.vectors[i][j] = np.array(HubComplete)[f[j],:]    
        Hub.append(Hubmesh.data)       
            
        
        
        
        
        #////////HubRim\\\\\\\\\
        
        Eckfolge = []
        f = 0    
        for i in range(14*2-2):     #Eckfolge für den Oberen  Rand
            if i % 2 == 0:
                Eckfolge.append([1+f+(15),1+f,0+f])
            else:
                Eckfolge.append([1+f+(14),2+f+(14),0+f])
                f += 1
                
        #Rand wird dem Mesh hinzugefügt
        Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Hubmesh.vectors[i][j] = np.array(HubRimTop)[f[j],:]    
        Hub.append(Hubmesh.data)
        
        Eckfolge = []
        f = 0    
        for i in range(14*2-2):     #Eckfolge für den  Unteren Rand
            if i % 2 == 0:
                Eckfolge.append([0+f,1+f,1+f+(15)])
            else:
                Eckfolge.append([0+f,2+f+(14),1+f+(14)])
                f += 1
                
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
                Eckfolge.append([0+f,2+f+(18*2),1+f+(18*2)])
                f += 1
        Eckfolge.append([36,37,38])
        Eckfolge.append([36,38,73])
        
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
                Eckfolge.append([1+g,0+g,36+f])
                
                g += 1
                h -= 3
                if g == 36:
                    g = 0
        Eckfolge.append([0, 35, 157])
            
                
        Hubmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Hubmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
        Hub.append(Hubmesh.data)    
        
        
        
        #//////////////Propeller Ring\\\\\\\\\\\\\\\
        
        
        RingTopIn = []
        RingBottomIn = []
        Achse3 = Achse + InnerRingBreite*2 + Ringabstand
        
        
        for i in range(36): #Koordinaten Liste für Oberen und Unteren kreis
            i -= 9
            i = i*10
            
            RingTopIn.append(      [math.cos(math.radians(i))*(Achse3/2)+xO,   math.sin(math.radians(i))*(Achse3/2)+yO       ,2])
            
            RingBottomIn.append(   [math.cos(math.radians(i))*(Achse3/2)+xO,   math.sin(math.radians(i))*(Achse3/2)+yO       ,0])
        
        
        Kord = RingTopIn + RingBottomIn
        
        
        Eckfolge = []   #Eckfolge für Oberen und Unteren Kreis
        f = 0    
        for i in range(36*2-1):
            if i % 2 == 0:
                Eckfolge.append([0+f,1+f,0+f+(36)])
            else:
                Eckfolge.append([0+f+(36-1),0+f,1+f+(36-1)])
                f += 1
        
        Eckfolge.append([35,71,70])
        
        
        
        
        Ring = []
        
        Ringmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Ringmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
        Ring.append(Ringmesh.data) 
        
        
        
        
        
        RingTop = []
        RingBottom = []
        Achse3 = Achse + InnerRingBreite*2 + Ringabstand + RingbreiteAussen*2
        
        
        for i in range(36): #Koordinaten Liste für Oberen und Unteren kreis
            i -= 9
            i = i*10
            
            RingTop.append(      [math.cos(math.radians(i))*(Achse3/2)+xO,   math.sin(math.radians(i))*(Achse3/2)+yO       ,2])
            
            RingBottom.append(   [math.cos(math.radians(i))*(Achse3/2)+xO,   math.sin(math.radians(i))*(Achse3/2)+yO       ,0])
        
        
        
        
         
        Kord = RingTop + RingTopIn
        
        Ringmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Ringmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
        Ring.append(Ringmesh.data) 
        
        
        Eckfolge = []   #Eckfolge für Oberen und Unteren Kreis
        f = 0    
        for i in range(36*2-1):
            if i % 2 == 0:
                Eckfolge.append([0+f+(36),1+f,0+f])
            else:
                Eckfolge.append([1+f+(36-1),0+f,0+f+(36-1)])
                f += 1
        
        Eckfolge.append([70,71,35])
        
        Kord = RingTop + RingBottom
        
        Ringmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Ringmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
        Ring.append(Ringmesh.data)
        
       
        Kord = RingBottom + RingBottomIn
        
        Ringmesh = mesh.Mesh(np.zeros(np.array(Eckfolge).shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(Eckfolge):
            for j in range(3):
                Ringmesh.vectors[i][j] = np.array(Kord)[f[j],:]    
        Ring.append(Ringmesh.data)      
        
        
        
        
        Ring = mesh.Mesh(numpy.concatenate(Ring))
        self.Ring = Ring
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            #///////Export\\\\\\
        
        
        Propeller = Propeller+Hub    
            
                    
        Propeller = mesh.Mesh(numpy.concatenate(Propeller))
       








        #3D Render anzeigen
        self.bild = vpl.QtFigure("bild")
        self.gridLayout.addWidget(self.bild, 0, 0, 1, 1)
        
                                         
        vpl.mesh_plot(Propeller)
        
        self.bild.update()                                   
                                         
        self.Propeller = Propeller
                   
         
        self.Table()
            
            
            
    def Table(self):
        #Erstellung der Tabelle für die Geschwindigkeit und Winkel werte
        self.table.setRowCount(len(self.UI))
        self.table.setColumnCount(len(self.UI[0]))
        self.table.setHorizontalHeaderLabels(["Profil v in m/s", "Profil Winkel"])
        for i,row in enumerate(self.UI):
            for j,val in enumerate(row):
                self.table.setItem(i,j,QtWidgets.QTableWidgetItem(str(val)))
            
    
    
    

    def Export(self):
        #Propeller Export
        self.Propeller.save("PropellerL" + str(int(self.L)) + "Kv" + str(int(self.Kv)) + "Lg" + str(int(self.LGeschwindigkeit)) + "D" +str(self.Achse-0.8) +  ".stl") 
        #Confirmation
        self.labelX.setText("Export Complete Directory: " + str(os.path.dirname(os.path.realpath(__file__))))
        #Ring Export
        self.Ring.save("Ring_D_"+str(self.Achse-0.8)+"mm.stl")
    
    
    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





    
    
    
    