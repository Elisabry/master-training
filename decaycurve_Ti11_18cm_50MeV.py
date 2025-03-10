import pandas as pd
import curie as ci
import numpy as np

#dc = ci.DecayChain("48V", R = [[1E4,0.33]], units = "h")    # For 48V
dc = ci.DecayChain("46SC", R = [[1E4,0.33]], units = "h")    # For 46SC
dc.get_counts("Ti11", EoB = "02/13/2017 14:21:00", peak_data = "CI010317_Ti11_18cm_50MeV.csv")
isotopes, R, cov_R = dc.fit_R()
dc.plot()