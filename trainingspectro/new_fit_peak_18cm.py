import curie as ci


cb = ci.Calibration("new_calibration_18cm.json")
#cb.plot()

sp = ci.Spectrum('CO020317_Ti06_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["55CO", "48V", "46SC", "47SC", "50V", "51SC", "44SC", "48SC", "40K", "42K"] #55CO, 46SC, 48V, 47SC, 51SC  
sp.plot()
sp.saveas('plot_Ti06_new_18cm_50MeV.png')