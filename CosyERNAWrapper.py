from sys import platform
import enum

try:
    import pexpect as expect
except ImportError:
    import wexpect as expect

import os
import shutil
import pyERNACosy.Wrapper.PlotCosyOutput as CosyOutput
import numpy as np
from scipy.optimize import minimize
from pyERNACosy.Wrapper.HelperClasses import *
import sys


class System(enum.Enum):
    windows = 1
    linux = 2
    macos = 3

if platform == "linux" or platform == "linux2":
    system = System.linux
elif platform == "darwin":
    system = System.macos
elif platform == "win32":
    system = System.windows

terminalSeparator = '>' if system == System.windows else ('$' if system == System.linux else '%')


class ERNA:
    mainMenu = 'simulator ---'
    child = None
    defaultTimeout: int
    debug: bool
    cosyDir: str
    isRunning = False
    saveIndex = 0
    logfile = None
    outputdir: str
    outputExtensions = tuple([".ps", ".fields", ".geometry", ".map", ".rstart", ".rstop"])
    nullCode = ""
    initialDir = "./"

    def __init__(self, cosyDirectory, debugMode=False, defTimeout=20, logFile='mylog.txt', output='./output'):
        self.cosyDir = cosyDirectory
        self.defaultTimeout = defTimeout
        self.logfile = open(logFile, 'wb')
        self.debug = debugMode
        self.outputdir = os.path.join(os.path.abspath(os.path.curdir), output)

        if system == System.windows:
            self.child = expect.spawn('cmd.exe')
            self.child.sendline('cd ' + self.cosyDir)
            self.child.sendline('dir')
            self.child.timeout = defTimeout
            self.child.expect(terminalSeparator)
            self.child.sendline('cosy')
        else:
            self.initialDir = os.path.abspath(os.path.curdir)
            os.chdir(self.cosyDir)
            self.child = expect.spawn('cosy', logfile=self.logfile)
            self.child.timeout = defTimeout

        self.child.logfile_send = self.logfile
        self.child.logfile = sys.stdout.buffer
        self.isRunning = True


#   Init procedures

    def startWithCentralBeam(self, primaryBeam):
        CosyOutput.removeOutputs(self.cosyDir + 'output')

        self.startERNAScript(primaryBeam.mass,
                             primaryBeam.energy,
                             primaryBeam.charge)

    def startAndCreateBeams(self, beams, numOfRays=2000):
        self.startWithCentralBeam(beams[0])
        self.createColorCodedBeamClaudioMode(beams, numOfRays)

    def startERNAScript(self, ionMass, ionEnergy, ionCharge, script='erna_v2_2'):
        self.sendCommandAfter(script, '.FOX')
        self.sendCommandAfter(ionMass, 'enter ion mass')
        self.sendCommandAfter(ionEnergy, 'enter ion energy')
        self.sendCommandAfter(ionCharge, 'enter ion charge')
        self.sendCommandAfter('', timeout=1)

    def exit(self):
        self.sendCommandAfter(99, self.mainMenu)
        self.child.close()
        self.logfile.close()
        os.chdir(self.initialDir)

#   I/O interactions
    def getMeanRadiusOnLastOutput(self):
        df = CosyOutput.dataFrameFromCosyFile(self.cosyDir + self.getOutputName('rstop'))
        return df['radius'].mean()

    def saveEverything(self):
        self.sendCommandAfter(10, self.mainMenu)
        self.sendCommandAfter('a', 'output filename')
        self.sendCommandAfter('', self.mainMenu, 120)

        for sourcepath in [os.path.curdir, os.path.join(os.path.curdir, "output")]:
            sourcefiles = os.listdir(sourcepath)

            if not os.path.exists(self.outputdir):
                os.mkdir(self.outputdir)

            for file in sourcefiles:
                if file.endswith(self.outputExtensions):
                    shutil.move(os.path.join(sourcepath, file), os.path.join(self.outputdir, file))


        self.saveIndex += 1

    def getOutputName(self, extension, index=None):
        actualIndex = index
        if index is None:
            actualIndex = self.saveIndex
        return 'output/{0:03d}_a.'.format(actualIndex) + extension

    def showGraphics(self):
        self.sendCommandAfter(3, self.mainMenu)

    def showTuning(self):
        self.sendCommandAfter(12, self.mainMenu)
        self.sendCommandAfter(self.nullCode, self.mainMenu, forcePrint=True)

#   Main Menu Interactions

##  Tunings
    def setTuningFromFile(self, filename):
        self.sendCommandAfter(11, self.mainMenu)
        self.sendCommandAfter(filename, "filename", timeout=4)

    def setExplicitTuning(self,
                        B_PME_1=.00001, B_PME_2=.00001,
                        B_trip_ex=.00001, B_trip_in=.00001,
                        U_SEPWF1=.00001,
                        B_singl1=.00001,
                        B_SEPdoublet_1=.00001,
                        B_SEPdoublet_2=.00001,
                        U_SEPWF2=.00001):
        tuning = Tuning()

        tuning.B_PME_1 = B_PME_1
        tuning.B_PME_2 = B_PME_2
        tuning.B_tripl_ex = B_trip_ex
        tuning.B_tripl_in = B_trip_in
        tuning.U_SEPWF1 = U_SEPWF1
        tuning.B_SEPsinglet1 = B_singl1
        tuning.B_SEPdoublet_1 = B_SEPdoublet_1
        tuning.B_SEPdoublet_2 = B_SEPdoublet_2
        tuning.U_SEPWF2 = U_SEPWF2

        self.setTuning(tuning.toDict())

    def fineTuning(self, startElement, stopElement):
        print("To be implemented!")
        return

        def objective_proxy(x):
            self._setExplicitTuning(*x)
            self.saveEverything()
            radius = self.getMeanRadiusOnLastOutput()
            print('Index =', self.saveIndex, ' Radius =', radius)
            return radius

        self.changeElementRange(startElement, stopElement)
        self.fitField(-1)
        self.saveEverything()

        x0 = np.array(Tuning(self.cosyDir + self.getOutputName('fields')).toArray())
        result = minimize(objective_proxy, x0)

    def setTuning(self, elementsTuning):
        if elementsTuning is None:
            print('No tuning specified, I\'ll use JERES TUNING')
            self.sendCommandAfter(21, self.mainMenu)  # JERES TUNING
        else:
            print('Setting tuning:', elementsTuning)
            for element in elementsTuning:
                self.setField(element, elementsTuning[element])

    def sendCommandAfter(self, command, waitingString=None, timeout=None, forcePrint=False):
        if waitingString is None:
            waitingList = [expect.TIMEOUT]
        else:
            waitingList = [waitingString, expect.TIMEOUT]

        if timeout is None:
            self.child.expect(waitingList)
        else:
            self.child.expect(waitingList, timeout=timeout)

        self.child.sendline(str(command))
        if self.debug or forcePrint:
            print(self.child.before, end='')
            try:
                print(self.child.match.group(0), end='')
            except:
                print("TimedOut?")
            print("command = " + str(command))

## Beams
    def createBeamFromFile(self, filename):
        self.sendCommandAfter(4, self.mainMenu)
        self.sendCommandAfter(1, 'main menu')
        self.sendCommandAfter(filename,"misspelled")

    def createConeBeam(self, beam, numOfRays=800):
        self.sendCommandAfter(4, self.mainMenu)
        self.sendCommandAfter(7, 'main menu')

        # Set primary beam properties
        self.sendCommandAfter(beam.divergence, 'enter divergence', 1)
        self.sendCommandAfter(beam.diameter, 'enter beam diameter', 1)
        numRays = numOfRays
        if numRays > 899:
            numOfRays = 899
        self.sendCommandAfter(numRays, 'number of rays')

    def createGaussianBeam(self, beam, numOfRays=1000):
        self.sendCommandAfter(4, self.mainMenu)
        self.sendCommandAfter(2, 'Return to main menu')

        # Set primary beam properties
        self.sendCommandAfter(beam.diameter, 'enter beam diameter')
        self.sendCommandAfter(beam.divergence, 'enter divergence')
        numRays = numOfRays
        if numRays > 149999:
            numOfRays = 149999
        self.sendCommandAfter(numRays, 'number of rays')

    def createColorCodedBeamClaudioMode(self, beams, numOfRays=2000):
        numberOfBeams = len(beams)

        self.sendCommandAfter(4, self.mainMenu)
        self.sendCommandAfter(4, 'Return to main menu')
        self.sendCommandAfter(6, 'up to 8 other beams')

        # Set primary beam properties
        primaryBeam = beams[0]
        self.sendCommandAfter(primaryBeam.diameter, 'enter beam diameter')
        self.sendCommandAfter(primaryBeam.divergence, 'enter divergence')

        self.sendCommandAfter(numberOfBeams - 1, 'how many beam do you want to add')

        # Add secondary beams
        for i in range(1, numberOfBeams):
            beam = beams[i]
            self.sendCommandAfter(beam.diameter, 'diameter of beam')
            self.sendCommandAfter(beam.divergence, 'divergence of beam')
            self.sendCommandAfter(beam.mass, 'mass of beam')
            self.sendCommandAfter(beam.energy, 'energy of beam')
            self.sendCommandAfter(beam.charge, 'charge state of beam')
            self.sendCommandAfter((100.0 / numberOfBeams), 'relative abundance')

        # Set number of rays
        if numOfRays < 501:
            numOfRays = 501
        if numOfRays > 149999:
            numOfRays = 149999

        self.sendCommandAfter(numOfRays, 'number of rays')

## Elements
    def changeElementRange(self, first_element=24, last_element=66, inFirstElementPosition_cm=-1.0, inLastElementPosition_cm=-1.0):
        self.sendCommandAfter(8, self.mainMenu)
        if inFirstElementPosition_cm > 0:
            self.sendCommandAfter(-1*first_element, 'first element')
            self.sendCommandAfter(inFirstElementPosition_cm, 'length')
        else:
            self.sendCommandAfter(first_element, 'first element')

        if inLastElementPosition_cm > 0:
            self.sendCommandAfter(-1*last_element, 'last element')
            self.sendCommandAfter(inLastElementPosition_cm, 'length')
        else:
            self.sendCommandAfter(last_element, 'last element')

    def fitField(self, index):
        command = Element().fitFieldNameFromIndex(index)
        if command is not None:
            self.sendCommandAfter(1, self.mainMenu)
            self.sendCommandAfter(command, 'BACK TO MENU')
        else:
            print('No element with index ' + str(index))

    def setField(self, element, fields):
        command = Element().setFieldNameFromIndex(element)
        if command is not None:
            self.sendCommandAfter(2, self.mainMenu)
            self.sendCommandAfter(command, 'BACK TO MENU')

            for field in fields:
                setField = field
                if field == 0.0:
                    setField = 0.00000001

                self.sendCommandAfter(setField, 'now is')

        else:
            print('No element with index ' + str(element))


