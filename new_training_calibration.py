import curie as ci
import pandas as pd 

def new_calibration_18cm():

    cb = ci.Calibration()
    #sp_Ba133 = ci.Spectrum("./Ba133_150217_18cm.Spe")
    #sp_Ba133.isotopes = ["133BA"]
    #sp_Ba133.plot()

    sp_newEu152 = ci.Spectrum("./newEu152_030317_18cm.Spe")
    sp_newEu152.isotopes = ['152EU'] 
    #sp_newEu152.plot()

    #sp_Co56 = ci.Spectrum('./Co56_190217_18cm.Spe')
    #sp_Co56.isotopes = ['56CO'] 
    #sp_Co56.plot()

    sp_newCs137 = ci.Spectrum('./newCs137_030317_18cm.Spe')
    sp_newCs137.isotopes = ['137CS'] 
    # sp_newCs137.plot()


    sources = [{'isotope':'133BA', 'A0':3.989E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'152EU', 'A0':370000, 'ref_date':'11/01/1984 12:00:00'},
               {'isotope':'137CS', 'A0':3.855E4, 'ref_date':'01/01/2009 12:00:00'},
               {'isotope':'56CO', 'A0':3.929E4, 'ref_date':'01/01/2009 12:00:00'}]
    sources = pd.DataFrame(sources)

    cb.calibrate([sp_newEu152, sp_newCs137], sources=sources)
    cb.plot()
    cb.saveas("new_calibration_18cm.json")
new_calibration_18cm()


