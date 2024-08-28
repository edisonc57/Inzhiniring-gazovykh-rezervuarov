def wichert_aziz(CO2, H2S):    
    E = 120 *((CO2+ H2S)**0.9 - (CO2 + H2S)** 1.6) + 15* (H2S**0.5 - H2S**4)  
    return E