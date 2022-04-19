import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Area = (17.78 * 1.32)
headers = ['Seconds', 'Strain(mm/mm)', 'Force(N)']
df1 = pd.read_table(r"C:\Users\Justin Blevins\Desktop\ENGR 298\MaterialsData\wood1.csv", sep = ",", names = headers)
x1 = df1['Strain(mm/mm)']
y1 = df1['Force(N)']
stresslist1 = list()
arrx1 = np.array(x1)
arry1 = np.array(y1)
for val in arry1:
    stress = val/Area
    stresslist1.append(stress)
stressarr1 = np.array(stresslist1)
averagex1 = np.average(arrx1)
averagey1 = np.average(arry1)
tuff1 = np.dot(arrx1, stressarr1)
avgstress1 = np.average(stressarr1)
modulus1 = np.divide(avgstress1, averagex1)
ductile1 = averagex1
print('The average stress = '+str(avgstress1))
print('The toughness of is '+ str(tuff1))
print('The average modulus = '+str(modulus1))
print('The average ductile = '+str(ductile1)+'%')
print('Average strain = '+str(averagex1)+'(mm/mm)')
print('Average force = '+str(averagey1)+'N')
df2 = pd.read_table(r"C:\Users\Justin Blevins\Desktop\ENGR 298\MaterialsData\wood2.csv", sep = ",", names = headers)
x2 = df2['Strain(mm/mm)']
y2 = df2['Force(N)']
stresslist2 = list()
arrx2 = np.array(x2)
arry2 = np.array(y2)
for val in arry2:
    stress2 = val/Area
    stresslist2.append(stress2)
stressarr2 = np.array(stresslist2)
arrx2 = np.array(x2)
arry2 = np.array(y2)
averagex2 = np.average(arrx2)
averagey2 = np.average(arry2)
tuff2 = np.dot(arrx2, stressarr2)
avgstress2 = np.average(stressarr2)
modulus2 = np.divide(avgstress2, averagex2)
ductile2 = averagex2
print('The average stress = '+str(avgstress2))
print('The toughness of is '+ str(tuff2))
print('The average modulus = '+str(modulus2))
print('The average ductile = '+str(ductile2)+'%')
print('Average strain = '+str(averagex2)+'(mm/mm)')
print('Average force = '+str(averagey2)+'N')
df3 = pd.read_table(r"C:\Users\Justin Blevins\Desktop\ENGR 298\MaterialsData\wood3.csv", sep = ",", names = headers)
x3 = df3['Strain(mm/mm)']
y3 = df3['Force(N)']
stresslist3 = list()
arrx3 = np.array(x3)
arry3 = np.array(y3)
for val in arry3:
    stress3 = val/Area
    stresslist3.append(stress3)
stressarr3 = np.array(stresslist3)
arrx3 = np.array(x3)
arry3 = np.array(y3)
averagex3 = np.average(arrx3)
averagey3 = np.average(arry3)
tuff3 = np.dot(arrx3, stressarr3)
avgstress3 = np.average(stressarr1)
modulus3 = np.divide(avgstress1, averagex1)
ductile3 = averagex1
print('The average stress = '+str(avgstress3))
print('The toughness of is '+ str(tuff3))
print('The average modulus = '+str(modulus3))
print('The average ductile = '+str(ductile3)+'%')
print('Average strain = '+str(averagex3)+'(mm/mm)')
print('Average force = '+str(averagey3)+'N')

averageforce = (averagey1 + averagey2 + averagey3)/3
averagestrain = (averagex1 + averagex2 + averagex3)/3
averagetuff = (tuff1 + tuff2 + tuff3)/3
averagestress = (np.average(stressarr1) + np.average(stressarr2) + np.average(stressarr3))/3
averagemodulus = (modulus1 + modulus2 + modulus3)/3
averageductile = (ductile1 + ductile2 + ductile3)/3
print('The average stress of the three samples is ' + str(averagestress))
print('The average force of the three samples is ' + str(averageforce))
print('The average strain of the three samples is ' + str(averagestrain))
print('The average toughness of the three samples is ' + str(averagetuff))
print('The average modulus = '+str(averagemodulus))
print('The average ductile = '+str(averageductile)+'%')
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.title('Strain vs Force')
plt.xlabel('Strain (mm/mm)')
plt.ylabel('Force (N)')
plt.legend(['Sample1', 'Sample2', 'Sample3'])
plt.show()