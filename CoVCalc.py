
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt


# population of germany
people = 83190556




x = requests.get('https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx?__blob=publicationFile',allow_redirects=True)
open('covdata.xlsx', 'wb').write(x.content)

val = pd.read_excel('covdata.xlsx', sheet_name=2, usecols='B', skiprows=1, header=None)
date = pd.read_excel('covdata.xlsx', sheet_name=2, usecols='A', skiprows=1, header=None)
print(val)

vallist = [float(val.T[i])/people for i in range(len(val)-4)]
datelist = [i for i in range(len(val)-4)]


sumlist=[vallist[0]]
for i in range(1,len(vallist)):
    sumlist.append(vallist[i] + sumlist[i-1])

p = np.polyfit(datelist, sumlist, deg=1)


poly1d_fn = np.poly1d(p) 
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(datelist,sumlist, 'yo', datelist, poly1d_fn(datelist), '--k')
print(p)

plt.xlim(0, 20)
plt.ylim(0, 0.01)
plt.show()

print("Days to 50%", 0.50/p[0])
