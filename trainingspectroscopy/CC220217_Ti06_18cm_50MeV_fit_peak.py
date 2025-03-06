import curie as ci


cb = ci.Calibration("trainingspectroscopy/calibration_18cm.json")  # Hva skjer her? kallibreringer er feil!
#cb.plot()

sp = ci.Spectrum('trainingdata/CC220217_Ti06_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["48V", "44SCm", "46SC", "47SC", "44SC", "48SC", "42K"] # 44SC og 48SC skal med hvertfall
sp.plot()
#sp.saveas('filnavn!.png') 
sp.saveas("CC220217_Ti06_18cm_50MeV.csv")