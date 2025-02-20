import curie as ci


cb = ci.Calibration("calibration_18cm.json")
#cb.plot()

sp = ci.Spectrum('BU170217_Fe01_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["55CO", "56CO","57CO", "58COm"]
sp.plot()
