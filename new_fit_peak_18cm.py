import curie as ci


cb = ci.Calibration("new_calibration_18cm.json")
#cb.plot()

sp = ci.Spectrum('CO020317_Ti06_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["55CO", "48V", "46SC", "47SC", "48CA", "44AR"] # 55CO, 46SC, 48V og 51SC ble dannet 
sp.plot()