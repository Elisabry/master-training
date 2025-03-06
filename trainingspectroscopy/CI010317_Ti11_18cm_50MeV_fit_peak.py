import curie as ci


cb = ci.Calibration("trainingspectroscopy/calibrationByHand_CK010317_Ti02_18cm_30MeV.json")  # Hva skjer her? kallibreringer er feil!
#cb.plot()

sp = ci.Spectrum('trainingdata/CI010317_Ti11_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["48V", "42K", "46SC", "47SC"] # 44SC og 48SC skal med hvertfall
sp.plot()
#sp.saveas('filnavn!.png') 
sp.saveas("CI010317_Ti11_18cm_50MeV.csv")