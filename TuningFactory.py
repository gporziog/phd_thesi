from .HelperClasses import Tuning
import math

class TuningFactory:
    outputFile: str
    tuning: Tuning

    def formatFloat(self, fmt, val):
        ret = fmt.format(val)
        if ret.startswith("-0."):
            return ret
        else:
            return " " + ret

    def formatCosyField(self, val):
        return "{0:.{1}f}".format(val, self.decimals(val)) + "\n"

    def decimals(self, v):
        return max(0, min(5, 5 - int(math.log10(abs(v))))) if v else 5

    # default constructor
    def __init__(self, filename, tuning):
        self.outputFile = filename
        self.tuning = tuning
        self.write()

    def write(self):
        out_file = open(self.outputFile, "w")

        tuningString = "----------- ERNA fields (pyWrapper by Claus) -----------" + "\n"
        tuningString += " B_PME_1             [T] =  " + self.formatCosyField(self.tuning.B_PME_1/1000)
        tuningString += " B_PME_2             [T] =  " + self.formatCosyField(self.tuning.B_PME_2/1000)
        tuningString += " U_SEPWF1            [V] =  " + self.formatCosyField(self.tuning.U_SEPWF1)
        tuningString += " B_SEPWF1            [T] =  " + self.formatCosyField(0.00000)
        tuningString += " B_SEPWF1_exp        [T] =  " + self.formatCosyField(0.00000)
        tuningString += " U_SEPWF2            [V] =  " + self.formatCosyField(self.tuning.U_SEPWF2)
        tuningString += " B_SEPWF2            [T] =  " + self.formatCosyField(0.00000)
        tuningString += " B_SEPWF2_exp        [T] =  " + self.formatCosyField(0.00000)
        tuningString += " B_SEPsinglet1       [T] =  " + self.formatCosyField(self.tuning.B_SEPsinglet1/1000)
        tuningString += " B_SEPsinglet2       [T] =  " + self.formatCosyField(0.00000)
        tuningString += " B_SEPdoublet_1      [T] =  " + self.formatCosyField(self.tuning.B_SEPdoublet_1/1000)
        tuningString += " B_SEPdoublet_2      [T] =  " + self.formatCosyField(self.tuning.B_SEPdoublet_2/1000)
        tuningString += " B_tripl_ex          [T] =  " + self.formatCosyField(self.tuning.B_tripl_ex/1000)
        tuningString += " B_tripl_in          [T] =  " + self.formatCosyField(self.tuning.B_tripl_in/1000)
        tuningString += " B_cssm              [T] =  " + self.formatCosyField(0.00000)
        tuningString += " B_dipole            [T] =  " + self.formatCosyField(0.00000)
        tuningString += " B_dipole_exp        [T] =  " + self.formatCosyField(0.00000)
        tuningString += "-------------------------------------------" + "\n"
        tuningString += "Warning: B_SEPWF*, B_SEPWF*_exp, B_SEPsinglet2, B_cssm, B_dipole, B_dipole_exp" + "\n"
        tuningString += "Are not supported. Some of them are calculated by cosy on 'ProcessElement'" + "\n"
        out_file.write(tuningString)
        out_file.close()
