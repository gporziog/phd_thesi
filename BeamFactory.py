import math
import random
import time

def polar2cart(r, theta, phi):
    return [
        r * math.sin(theta) * math.cos(phi),
        r * math.sin(theta) * math.sin(phi),
        r * math.cos(theta)
    ]


def formatFloat(fmt, val):
    ret = fmt.format(val)
    if ret.startswith("-0."):
        return "-" + ret[2:]
    return ret


def formatCosyFloat(val):
    return formatFloat("{:.5f}", val) + " "


class BeamFactory:
    outputFile: str
    numberOfBeams: int = 0
    beamString: str = ""

    # default constructor
    def __init__(self, filename):
        self.outputFile = filename
        self.open()

    def addRay(self, x, xp, y, yp, time, energy, mass, charge, color):
        """_summary_

        Parameters
        ----------
        x : float
            x displacement from center in m
        xp : float
            horizontal angle with the optical axis in radians
        y : float
            y displacement from center in m
        yp : float
            vertical angle with the optical axis in radians
        time : float
            difference from reference ray
        energy : float
            energy relative change from reference beam
        mass : float
            mass relative change from reference beam
        charge : float
            relative change from reference beam
        color : int
            1 to 9 color code
        """
        self.beamString += " " + "{:6d}".format(self.numberOfBeams + 1) + " "
        self.beamString += formatCosyFloat(x)
        self.beamString += formatCosyFloat(xp)
        self.beamString += formatCosyFloat(y)
        self.beamString += formatCosyFloat(yp)
        self.beamString += formatCosyFloat(time)
        self.beamString += formatCosyFloat(energy)
        self.beamString += formatCosyFloat(mass)
        self.beamString += formatCosyFloat(charge)
        self.beamString += str(color) + "\n"
        self.numberOfBeams += 1
        self.write()
        self.beamString = ""

    def open(self):
        out_file = open(self.outputFile, "w")
        out_file.write("")
        out_file.close()

    def write(self):
        out_file = open(self.outputFile, "a")
        out_file.write(self.beamString)
        out_file.close()

    def close(self):
        out_file = open(self.outputFile, "a")
        out_file.write("#\n")
        out_file.close()
        time.sleep(2)

    def addBeamFromFile(self, filename):
        print("**** ADDING BEAM FROM FILE ERASES CURRENT BEAM IN BEAMFACTORY ****")
        print("**** You may want to add before from file and then add other rays ****")
        beamFile = open(filename, "r")
        out_file = open(self.outputFile, "w")
        beamFileString = beamFile.read().replace("#\n", "")
        out_file.write(beamFileString)
        out_file.close()
        self.numberOfBeams = beamFileString.count("\n")
        beamFile.close()

    def addBeamFromDF(self, dataframe):
        df = dataframe.reset_index()  # make sure indexes pair with number of rows
        cols = ["n", "x", "xp", "y", "yp", "time", "energy", "mass", "charge", "color"]
        for index, row in df.iterrows():
            self.addRay(row["x"], row["xp"], row["y"], row["yp"], row["time"], row["energy"], row["mass"], row["charge"], row["color"])

    def addPolarRay(self, r, divergence, phi, time, energy, mass, charge, color):
        """_summary_

        Parameters
        ----------
        r : float
            distance from center in mm
        divergence : float
            angle with the optical axis in mradians
        phi : float
            about optical axis rotation in radians
        time : float
            difference from reference ray
        energy : float
            energy relative change from reference beam
        mass : float
            mass relative change from reference beam
        charge : float
            relative change from reference beam
        color : int
            1 to 9 color code
        """

        self.addRay(
            r * math.cos(phi) / 1000,
            divergence * math.cos(phi) / 1000,
            r * math.sin(phi) / 1000,
            divergence * math.sin(phi) / 1000,
            time,
            energy,
            mass,
            charge,
            color
        )

    def addGaussianBeam(self, beam, nRays, centralEnergy=-1, centralCharge=-1, centralMass=-1, color=1, offsetDiv=0):
        mmDiameter = beam.diameter/1000
        mmDivergence = beam.divergence/1000

        #random.gauss(0, mmDivergence)
        #random.uniform(-mmDivergence, mmDivergence)
        for i in range(nRays):
            divR = random.uniform(0, mmDivergence) + offsetDiv/1000
            divPhi = random.uniform(0, 2*math.pi)
            self.addRay(random.gauss(0, mmDiameter),
                        divR*math.cos(divPhi),
                        random.gauss(0, mmDiameter),
                        divR*math.sin(divPhi),
                        0,
                        0 if centralEnergy < 0 else 0.5 * (beam.energy - centralEnergy) / centralEnergy,
                        0 if centralMass < 0 else 0.5 * (beam.mass - centralMass) / centralMass,
                        0 if centralCharge < 0 else 0.5 * (beam.charge - centralCharge) / centralCharge,
                        color
                        )


    def addCircularBeam(self, beam, nRays, centralEnergy=-1, centralCharge=-1, centralMass=-1, color=1):
        r = beam.diameter / 2
        fullCircle = 2 * math.pi
        increment = fullCircle / nRays
        currentAngle = 0
        while currentAngle <= fullCircle:
            self.addPolarRay(r,
                             beam.divergence,
                             currentAngle,
                             0,
                             0 if centralEnergy < 0 else 0.5*(beam.energy - centralEnergy)/centralEnergy,
                             0 if centralCharge < 0 else 0.5*(beam.charge - centralCharge)/centralCharge,
                             0 if centralMass < 0 else 0.5*(beam.mass - centralMass)/centralMass,
                             color
                             )
            currentAngle += increment
