import pandas as pd
import curie as ci
import numpy as np


#dc = ci.DecayChain("48V", R = [[1E4,0.33]], units = "h")    # For 48V
dc = ci.DecayChain("46SC", R = [[1E4,0.33]], units = "h")    # For 46SC
dc.get_counts("Ti10", EoB = "02/13/2017 14:21:00", peak_data = "CG240217_Ti10_18cm_50MeV.csv")
isotopes, R, cov_R = dc.fit_R()
dc.plot()