def emi_calc(principle, rate, time):
    r = rate/12/100
    emi = (principle * r * (1+r)**time) / ((1+r)**time-1)
    return emi


print(emi_calc(2000, 400, 290))
