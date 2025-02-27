import curie as ci
import pandas as pd 

def calibration_18cm():

    cb = ci.Calibration()
    sp_Ba133 = ci.Spectrum("./Ba133_150217_18cm.Spe")
    sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()

    sp_Eu152 = ci.Spectrum("./Eu152_150217_18cm.Spe")
    sp_Eu152.isotopes = ["152EU"]
    #sp_Eu152.plot()

    sp_Co56 = ci.Spectrum('./Co56_190217_18cm.Spe')
    sp_Co56.isotopes = ['56CO'] 
    #sp_Co56.plot()

    sp_Cs137 = ci.Spectrum('./Cs137_230317_18cm.Spe')
    sp_Cs137.isotopes = ['137CS'] 
    #sp_Cs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.989E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'152EU', 'A0':370000, 'ref_date':'11/01/1984 12:00:00'},
               {'isotope':'137CS', 'A0':3.855E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_Ba133, sp_Eu152, sp_Cs137, sp_Co56], sources=sources)
    cb.plot()
    cb.saveas("calibration_18cm.json")
calibration_18cm()





if __name__ == '__main__':

    calibration_18cm()
