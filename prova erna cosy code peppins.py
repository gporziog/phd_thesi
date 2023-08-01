from pyERNACosy.Wrapper.CosyERNAWrapper import ERNA, Beam
from pyERNACosy.Wrapper.HelperClasses import Tuning
from pyERNACosy.Wrapper.PlotCosyOutput import dataFrameFromCosyFile
from pyERNACosy.Wrapper.HelperClasses import Element
import pandas as pd

#newTuning = {
#
#            Element.PME: [0.00001, 0.0001],
#            Element.CSSM:[594.164],
#            Element.TRIPLET: [-0.10786, 0.13090],
#            Element.SEPWF1: [40],
#            Element.SINGLET1: [0.070],
#            Element.DOUBLET: [0.0997, -0.161],
#            Element.SEPWF2: [40]            
#        }

erna=ERNA("..\erna-cosy-code-SC_Development\erna-cosy-code-SC_Development/", debugMode=True)

primaryBeam= Beam(16.0,8.470,6,2,3)

erna.startWithCentralBeam(primaryBeam)
erna.createGaussianBeam(primaryBeam, 500)
erna.setTuningFromFile("..\peppins001_..fields")
erna.showTuning()
#erna.setTuning(newTuning)
erna.saveEverything()

DataFrameStart=dataFrameFromCosyFile("C:\\Users\\Giuseppe Porzio\\Desktop\\dottorato\\DB Ulisse sviluppo\\erna-cosy-code-SC_Development\\erna-cosy-code-SC_Development\\output\\001_a.rstop")
print(DataFrameStart)
radius=DataFrameStart['radius']
#print (radius)
i=0
inner=0
for n in radius:
    #print(n)
    i=i+1
    if(n<0.02):
        inner=inner+1
percentage=(inner/i)*100
print(str(percentage)+"%")
