import pandas as pd

class Element:

    STARTPOINT = 1; DL_STARTPOINT_HEFC = 2; HEFC = 3; DL_HEFC_OBJECTSLITS = 4; OBJECTSLITS = 5;
    DL_OBJSLITS_ANALYSINGMAGNET = 6; ANALYSINGMAGNET_IN = 7; ANALYSINGMAGNET_OUT = 8;
    DL_ANALYSINGMAGNET_IMAGESLITS = 9; IMAGESLITS = 10; DL_IMAGESLITS_IMAGEFC = 11; IMAGEFC = 12;
    DL_IMAGEFC_ESA_A = 13; ESA_A = 14; DL_ESA_A_ESA_B = 15; ESA_B = 16;
    DL_ESA_B_SWITCHINGMAGNET = 17; SWITCHINGMAGNET = 18; DL_SWITCHINGMAGNET_GSISLITS = 19;
    GSISLITS = 20; DL_GSISLITS_FOCTRIPLET = 21; FOCTRIPLET = 22; DL_FOCTRIPLET_GASTARGET = 23;
    GASTARGET = 24; DL_GASTARGET_PME = 25; PME = 26; DL_PME_CSSM = 27; CSSM = 28;
    DL_CSSM_TRIP = 29; TRIPLET = 30; DL_TRIP_SLIT1 = 31; SLIT1 = 32; DL_SLIT1_FC1 = 33; FC1 = 34;
    DL_FC1_SEPWF1 = 35; SEPWF1 = 36; DL_SEPWF1_SFCIN = 37; SLIT_SFCIN = 38; DL_SFCIN_SHUTTER = 39;
    SHUTTER = 40; DL_SHUTTER_SLIT2 = 41; SLIT2 = 42; DL_SLIT2_SINGLET1 = 43; SINGLET1 = 44;
    DL_SINGLET1_DIPOLE = 45; DIPOLE = 46; DL_DIPOLE_SLITDIPOLE = 47; SLIT_DIPOLE = 48;
    DL_SLITDIPOLE_DIPOLEEXIT = 49; SLIT_DIPOLE_EXIT = 50; DL_DIPOLEEXIT_DOUBLET = 51; DOUBLET = 52;
    DL_DOUBLET_SLIT3 = 53; SLIT3 = 54; DL_SLIT3_SEPWF2 = 55; SEPWF2 = 56; DL_SEPWF2_SLIT4 = 57;
    SLIT4 = 58; DL_SLIT4_MCP = 59; MCP = 60; DL_MCP_Si = 61; Si = 62; DL_Si_SLIT5 = 63;
    SLIT5 = 64; SLIT5_FC4_ICTIN = 65; ICT = 66

    def nameFromIndex(self, index):
        switcher = {1: 'STARTPOINT', 2: 'DL_STARTPOINT_HEFC', 3: 'HEFC', 4: 'DL_HEFC_OBJECTSLITS', 5: 'OBJECTSLITS',
                    6: 'DL_OBJSLITS_ANALYSINGMAGNET', 7: 'ANALYSINGMAGNET_IN', 8: 'ANALYSINGMAGNET_OUT',
                    9: 'DL_ANALYSINGMAGNET_IMAGESLITS', 10: 'IMAGESLITS', 11: 'DL_IMAGESLITS_IMAGEFC', 12: 'IMAGEFC',
                    13: 'DL_IMAGEFC_ESA_A', 14: 'ESA_A', 15: 'DL_ESA_A_ESA_B', 16: 'ESA_B',
                    17: 'DL_ESA_B_SWITCHINGMAGNET', 18: 'SWITCHINGMAGNET', 19: 'DL_SWITCHINGMAGNET_GSISLITS',
                    20: 'GSISLITS', 21: 'DL_GSISLITS_FOCTRIPLET', 22: 'FOCTRIPLET', 23: 'DL_FOCTRIPLET_GASTARGET',
                    24: 'GASTARGET', 25: 'DL_GASTARGET_PME', 26: 'PME', 27: 'DL_PME_CSSM', 28: 'CSSM',
                    29: 'DL_CSSM_TRIP', 30: 'TRIPLET', 31: 'DL_TRIP_SLIT1', 32: 'SLIT1', 33: 'DL_SLIT1_FC1', 34: 'FC1',
                    35: 'DL_FC1_SEPWF1', 36: 'SEPWF1', 37: 'DL_SEPWF1_SFCIN', 38: 'SLIT_SFCIN', 39: 'DL_SFCIN_SHUTTER',
                    40: 'SHUTTER', 41: 'DL_SHUTTER_SLIT2', 42: 'SLIT2', 43: 'DL_SLIT2_SINGLET1', 44: 'SINGLET1',
                    45: 'DL_SINGLET1_DIPOLE', 46: 'DIPOLE', 47: 'DL_DIPOLE_SLITDIPOLE', 48: 'SLIT_DIPOLE',
                    49: 'DL_SLITDIPOLE_DIPOLEEXIT', 50: 'SLIT_DIPOLE_EXIT', 51: 'DL_DIPOLEEXIT_DOUBLET', 52: 'DOUBLET',
                    53: 'DL_DOUBLET_SLIT3', 54: 'SLIT3', 55: 'DL_SLIT3_SEPWF2', 56: 'SEPWF2', 57: 'DL_SEPWF2_SLIT4',
                    58: 'SLIT4', 59: 'DL_SLIT4_MCP', 60: 'MCP', 61: 'DL_MCP_Si', 62: 'Si', 63: 'DL_Si_SLIT5',
                    64: 'SLIT5', 65: 'SLIT5_FC4_ICTIN', 66: 'ICT'}
        return switcher.get(index, "Invalid Element")

    def indexFromName(self, name):
        for i in range(0, 66):
            if name == self.nameFromIndex(i):
                return i

    def setFieldNameFromIndex(self, index):
        switcher = {Element.FOCTRIPLET: 'ft',
                    Element.PME: 'pm',
                    Element.TRIPLET: 'tt',
                    Element.SEPWF1: 'w1',
                    Element.SINGLET1: 's1',
                    Element.DOUBLET: 'do',
                    Element.SEPWF2: 'w2'}
        return switcher.get(index, None)

    def fitFieldNameFromIndex(self, index):
        switcher = {-1: 'al',
                    Element.SINGLET1: 's1',
                    Element.TRIPLET: 't',
                    Element.DOUBLET: 'do',
                    Element.SEPWF1: 'w1',
                    Element.SEPWF2: 'w2'
                    }
        return switcher.get(index, None)


class Beam:
    mass: float
    energy: float
    charge: int
    divergence: float
    diameter: float

    # default constructor
    def __init__(self, mass, energy, charge, divergence, diameter):
        self.mass = mass
        self.energy = energy
        self.charge = charge
        self.divergence = divergence
        self.diameter = diameter


class Tuning:
    B_PME_1: float
    B_PME_2: float
    B_tripl_ex: float
    B_tripl_in: float
    U_SEPWF1: float
    B_SEPsinglet1: float
    B_SEPdoublet_1: float
    B_SEPdoublet_2: float
    U_SEPWF2: float

    @classmethod
    def JeresTuning(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.00001
        tuning.B_PME_2 = 0.00001
        tuning.B_tripl_ex = 147.0
        tuning.B_tripl_in = 167.8
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 76.9
        tuning.B_SEPdoublet_1 = 141.1
        tuning.B_SEPdoublet_2 = 152.5
        tuning.U_SEPWF2 = 50.0

        return tuning

    @classmethod
    def JeresTuningWithPME(cls):
        tuning = Tuning.JeresTuning()
        tuning.B_PME_2 = -800
        return tuning

    @classmethod
    def PME_8MeV_Tuning(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.00001
        tuning.B_PME_2 = -1000.0
        tuning.B_tripl_ex = 120.0
        tuning.B_tripl_in = 170.8
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = -45.0
        tuning.B_SEPdoublet_1 = 120.0
        tuning.B_SEPdoublet_2 = 130.0
        tuning.U_SEPWF2 = 50.0

        return tuning

    @classmethod
    def PME_3MeV_Tuning(cls):
        tuning = Tuning()

        tuning.B_PME_1 = -0.5
        tuning.B_PME_2 = -1000.0
        tuning.B_tripl_ex = 124.0
        tuning.B_tripl_in = 156.7
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = -22.0
        tuning.B_SEPdoublet_1 = 130.0
        tuning.B_SEPdoublet_2 = 147.0
        tuning.U_SEPWF2 = 40.0

        return tuning

    @classmethod
    def At_3MeV_Tuning_Auto(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.0000
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 145.9
        tuning.B_tripl_in = 169.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 61.7
        tuning.B_SEPdoublet_1 = 121.3
        tuning.B_SEPdoublet_2 = 131.4
        tuning.U_SEPWF2 = 40.0

        return tuning

    @classmethod
    def At_2_4_MeV_Tuning_PME(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.0000
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 131.7
        tuning.B_tripl_in = 147.3
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 20.0
        tuning.B_SEPdoublet_1 = 132.0
        tuning.B_SEPdoublet_2 = 140.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_2_4_MeV_Tuning_Manual(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.0000
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 145.0
        tuning.B_tripl_in = 160.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = -25.0
        tuning.B_SEPdoublet_1 = 115.0
        tuning.B_SEPdoublet_2 = 138.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_2_7_MeV_Tuning_Manual(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.0000
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 137.4
        tuning.B_tripl_in = 157.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 66.9
        tuning.B_SEPdoublet_1 = 136.6
        tuning.B_SEPdoublet_2 = 143.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_2_7_MeV_Tuning_PME(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 500.00
        tuning.B_PME_2 = 650.00
        tuning.B_tripl_ex = 137.4
        tuning.B_tripl_in = 157.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 64.0
        tuning.B_SEPdoublet_1 = 136.6
        tuning.B_SEPdoublet_2 = 150.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_2MeV_Tuning_Manual(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.0000
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 120.8
        tuning.B_tripl_in = 138.3
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 46.5
        tuning.B_SEPdoublet_1 = 120.7
        tuning.B_SEPdoublet_2 = 130.2
        tuning.U_SEPWF2 = 30.0

        return tuning

    @classmethod
    def At_2MeV_Tuning_PME_Manual(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 1200.0
        tuning.B_PME_2 = 600.0
        tuning.B_tripl_ex = 153.0
        tuning.B_tripl_in = 158.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = -52.0
        tuning.B_SEPdoublet_1 = 80.0
        tuning.B_SEPdoublet_2 = 140.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_3MeV_Tuning_Manual(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 0.0000
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 144.8
        tuning.B_tripl_in = 166.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 70.5
        tuning.B_SEPdoublet_1 = 144.0
        tuning.B_SEPdoublet_2 = 154.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_3MeV_Tuning_PME_Auto(cls):
        tuning = Tuning()

        tuning.B_PME_1 = -1200.0
        tuning.B_PME_2 = 0.0000
        tuning.B_tripl_ex = 146.2
        tuning.B_tripl_in = 153.8
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 105.5
        tuning.B_SEPdoublet_1 = 144.9
        tuning.B_SEPdoublet_2 = 155.0
        tuning.U_SEPWF2 = 40.0

        return tuning

    @classmethod
    def test_Tuning(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 800.0
        tuning.B_PME_2 = 800.0
        tuning.B_tripl_ex = 133.0
        tuning.B_tripl_in = 147.3
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 40.0
        tuning.B_SEPdoublet_1 = 140.0
        tuning.B_SEPdoublet_2 = 150.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_3MeV_Tuning_PME_Manual_2(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 1200.0
        tuning.B_PME_2 = 1200.0
        tuning.B_tripl_ex = 149.0
        tuning.B_tripl_in = 170.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 90.0
        tuning.B_SEPdoublet_1 = 145.0
        tuning.B_SEPdoublet_2 = 145.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    @classmethod
    def At_3MeV_Tuning_PME_Manual(cls):
        tuning = Tuning()

        tuning.B_PME_1 = 1200.0
        tuning.B_PME_2 = 1200.0
        tuning.B_tripl_ex = 146.5
        tuning.B_tripl_in = 160.0
        tuning.U_SEPWF1 = 60.0
        tuning.B_SEPsinglet1 = 75.0
        tuning.B_SEPdoublet_1 = 144.0
        tuning.B_SEPdoublet_2 = 149.0
        tuning.U_SEPWF2 = -60.0

        return tuning

    # default constructor
    def __init__(self, filename = None, skipFooter=1):
        if filename is not None:
            df = pd.read_csv(filename,
                             skipfooter=skipFooter,
                             skiprows=1,
                             sep='\s*\s',
                             engine='python',
                             header=None,
                             names=["name", "unit", "nothing", "field"])

            for index, row in df.iterrows():
                name = row['name']
                fieldToSet = row['field']
                print(row['name'], "=", row['field'])

                if name[0] == 'B':
                    fieldToSet *= 1000
                if name[0] == 'U':
                    fieldToSet /= 1000

                setattr(self, name, fieldToSet)


        else:
            self.B_PME_1 = 0.00001
            self.B_PME_2 = 0.00001
            self.B_tripl_ex = 0.00001
            self.B_tripl_in = 0.00001
            self.U_SEPWF1 = 0.00001
            self.B_SEPsinglet1 = 0.00001
            self.B_SEPdoublet_1 = 0.00001
            self.B_SEPdoublet_2 = 0.00001
            self.U_SEPWF2 = 0.00001

    def toArray(self):
        return [self.B_PME_1, self.B_PME_2, self.B_tripl_ex, self.B_tripl_in, self.U_SEPWF1, self.B_SEPsinglet1, self.B_SEPdoublet_1, self.B_SEPdoublet_2, self.U_SEPWF2]

    def toDict(self):
        return {
            Element.PME: [self.B_PME_1, self.B_PME_2],
            Element.TRIPLET: [self.B_tripl_ex, self.B_tripl_in],
            Element.SEPWF1: [self.U_SEPWF1],
            Element.SINGLET1: [self.B_SEPsinglet1],
            Element.DOUBLET: [self.B_SEPdoublet_1, self.B_SEPdoublet_2],
            Element.SEPWF2: [self.U_SEPWF2]
        }
