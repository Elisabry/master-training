import curie as ci


cb = ci.Calibration("calibrationByHand_CK010317_Ti02_18cm_30MeV.json")  # Hva skjer her? kallibreringer er feil!
#cb.plot()

sp = ci.Spectrum('CI010317_Ti11_18cm_50MeV.Spe')
sp.cb = cb
sp.isotopes = ["55CO", "48V", "46SC", "47SC", "50V", "51SC", "44SC", "48SC", "40K", "42K"]
sp.plot()
sp.saveas('plot_Ti11_18cm_50MeV.png')