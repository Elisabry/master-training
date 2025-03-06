import curie as ci


cb = ci.Calibration("trainingspectroscopy/new_calibration_18cm.json")  # Hva skjer her? kallibreringer er feil!
#cb.plot()

sp = ci.Spectrum('trainingdata/CO020317_Ti06_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["55CO", "48V", "44SCm", "46SC", "47SC", "50V", "51SC", "44SC", "48SC", "40K", "42K"] # 44SC og 48SC skal med hvertfall
sp.plot()
#sp.saveas('plot_Ti11_18cm_50MeV.png') 
sp.saveas("CO020317_Ti06_18cm_50MeV.csv")