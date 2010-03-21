#!/usr/bin/python

import matplotlib.pyplot as plt
import math, numpy



def compound(P, z):
    range_y = []
    for i in numpy.arange(1, 50, 0.1):
        e = math.pow(eval("(1+%s)" % (z)), i)
        y = eval("%s*%s" % (P,e))
        range_y.append(y)
    return range_y 

def simple(P,z):
    range_y = []
    for i in numpy.arange(1, 50, 0.1):
        e = eval("%s*(%s*%s+1)" % (P,z,i))
        range_y.append(e)
    return range_y 

from matplotlib import rcParams

comp = plt.plot(numpy.arange(1,50,0.1), compound(100, 0.09), lw=2.3, c="purple", aa="True")
simp = plt.plot(numpy.arange(1,50,0.1), simple(100, 0.09), lw=2.3, c="blue", aa="True")
plt.legend([comp,simp], ["Zinseszins", "einfacher Zins"])
plt.ylabel("Kapital")
plt.xlabel("Jahre")
plt.grid(True)
plt.show()
