# Kevin Lee

import numpy as np  
import matplotlib.pyplot as plt
import os
 
choice = input("Please enter 1 for Tippecanoe_River\nPlease enter 2 for Wildcat_Creek_at_Lafayette:\nOR user specified file enter 3!\n")
choice = int(choice)
 
if choice == 1:
    print("process with Tippecanoe_River_at_Ora.Annual_Metrics.txt")
    data = "Tippecanoe_River_at_Ora.Annual_Metrics.txt"
elif choice == 2:
    print("Process with Wildcat_Creek_at_Lafayette.Annual_Metrics.txt")
    data = "Wildcat_Creek_at_Lafayette.Annual_Metrics.txt"
elif choice == 3:
    print("You entered 3, tell me the file name")
    data = input()
else:
    print("wowowowo u don't listen.....u should make the program then BYE")

ofile = input("Please enter output file name, all output files will be produced in pdf format.\n")
ofile = str(ofile)

data1 = np.genfromtxt(data, unpack= True, skip_header=1)
# data2 = np.genfromtxt('Wildcat_Creek_at_Lafayette.Annual_Metrics.txt', unpack= True)
#Year	Mean	Max	Min	StdDev	Tqmean	RBindex

plt.subplot(311)
plt.plot( data1[0,:], data1[1,:],'k', label='Mean')
plt.plot(data1[0,:], data1[2,:],'r', label='Max')
plt.plot(data1[0,:], data1[3,:],'b', label='Min')
plt.xlabel('Year')
plt.ylabel('Streamflow (cfs)')
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0.)


plt.subplot(312)
plt.scatter(data1[0,:], data1[5,:]*100, label='Tqmean')
plt.xlabel('Year')
plt.ylabel('Tqmean %')
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0.)

plt.subplot(313)
plt.bar(data1[0,:], data1[6,:], label='Min')
plt.xlabel('Year')
plt.ylabel('R-B index ratio')
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0.)
filename = os.path.join(ofile +"."+ "pdf")
plt.savefig(filename)