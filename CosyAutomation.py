import Wrapper.PlotCosyOutput as CosyOutput
from .CosyERNAWrapper import Beam
from .CosyERNAWrapper import Element
import Wrapper.CosyERNAWrapper as ERNA
import matplotlib.pyplot as plt
import math

def startWithCentralBeam(primaryBeam, cosyDir='', debug=False):
    ERNA.debug = debug
    ERNA.cosyDir = cosyDir
    CosyOutput.removeOutputs(cosyDir + 'output')
    ERNA.runCosy()

    ERNA.startERNAScript(primaryBeam.mass,
                         primaryBeam.energy,
                         primaryBeam.charge)

def startAndCreateBeams(beams, cosyDir='', debug=False, numOfRays = 2000):
    startWithCentralBeam(beams[0], cosyDir, debug)

    ERNA.createColorCodedBeamClaudioMode(beams, numOfRays)

def setTuning(elementsTuning):
    if elementsTuning is None:
        print('No tuning specified, I\'ll use JERES TUNING')
        ERNA.sendCommandAfter(21, ERNA.mainMenu)  # JERES TUNING
    else:
        print('Tuning specified but this function is not implemented yet, I\'ll use JERES TUNING')
        ERNA.sendCommandAfter(21, ERNA.mainMenu)  # JERES TUNING


#def fineTuning(startElement, stopElement):

#def checkMeanRayForElementFields(fields):


# returns last stopping element dataframe
def runSimulation(beams,
            startElement=Element.GASTARGET,
            stopElements=[Element.ICT],
            stopElementsCostraints=[],
            elementsTuning=None,
            cosyDir='',
            debug=False,
            shouldPlot=False):

    numPlots = math.ceil(len(stopElements) / 2.)
    fig, axs = plt.subplots(numPlots, 2)

    if ERNA.isRunning is False:
        startAndCreateBeams(beams, debug, cosyDir)
        ERNA.isRunning = True

    setTuning(elementsTuning)

    dataframes = []

    index = 0
    for stopElement in stopElements:
        ERNA.changeElementRange(startElement, stopElement)
        #ERNA.showGraphics()
        ERNA.saveEverything()

        df = CosyOutput.dataFrameFromCosyFile(cosyDir + ERNA.getOutputName(index + 1, 'rstop'))
        dataframes.append(df)
        row = int(index / 2)
        col = index % 2
        plot = None
        if numPlots > 1:
            plot = axs[row, col]
        else:
            plot = axs[row]

        plot.scatter(df['x'], df['y'], c=df['color'], marker='.', s=1)
        plot.set_title(Element().nameFromIndex(stopElement))
        index += 1

    fig.tight_layout(pad=1.0)

    if shouldPlot:
        plt.show()

    return dataframes

def stopBeamsWithSlits(slits, inDataFrame, previousStopped=[]):
    print('Implement me')
