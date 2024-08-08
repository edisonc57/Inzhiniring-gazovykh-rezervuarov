def Sutton_function(SGG):
    Ppch= 0.006895*(756.8 - 131*SGG - 3.6*SGG*SGG)
    Tpch= 5/9*(169.2 + 349.5*SGG - 74*SGG*SGG)
    return (Ppch, Tpch)