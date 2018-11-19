# program: FadeOut.py
# author: Amarpreet Kaur
# course: CS 827
# date: November 19th 2018
# description: this program reads in mysteryTones.dat file, applies the Fade-Out effect and writes the output in the out.dat file.
 


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib.pyplot as plt


data = pd.read_csv("C:/Users/amarpreet/Desktop/computer audio/Assignment 2/mysteryTones.dat", header=None, delimiter=r"\s+")

x = data[0]
y = data[1]
# time array
xlist = []
# amplitude array
ylist = []

# the columns in the file are read into the arrays.
for i in range(0,int(len(x))):
   xlist.append(float(x.iloc[i]))
   ylist.append(float(y.iloc[i]))   

f = open("out.dat", "w")


# required headers are added for the PCM file 
f.write("; Sample Rate "+str(44100)+"\n")
f.write("; Channels 1"+"\n")

# fade out filter
# scaling factor is chosen such that the amplitude values are multiplied with a factor varying from 1 to 0
scaling_factor = len(xlist)
length = len(xlist)
for i in range(0,int(length)):
   f.write(str(xlist[i])+"   "+str(((ylist[i])) * (scaling_factor/length)))
   f.write("\n")
   scaling_factor = scaling_factor - 1 

f.close() 
