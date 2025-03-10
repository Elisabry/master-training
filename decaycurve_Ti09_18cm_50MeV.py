import pandas as pd
import curie as ci
import numpy as np

#dfCC = pd.read_csv("CC220217_Ti06_18cm_50MeV.csv")
#dfCO = pd.read_csv("CO020317_Ti06_18cm_50MeV.csv")
#df_Ti06 = pd.concat((dfCC, dfCO), axis = 0)
#df_Ti06.to_csv("Ti06.csv")

#dc = ci.DecayChain("48V", R = [[1E4,0.33]], units = "h")    # For 48V
dc = ci.DecayChain("46SC", R = [[1E4,0.33]], units = "h")    # For 46SC
dc.get_counts("Ti09", EoB = "02/13/2017 14:21:00", peak_data = "CF240217_Ti09_18cm_50MeV.csv")
isotopes, R, cov_R = dc.fit_R()
dc.plot()