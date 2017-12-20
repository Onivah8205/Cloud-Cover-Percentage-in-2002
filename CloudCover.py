import matplotlib.pyplot as plt
import numpy as np
import csv

#This opens the file, reads through it, and makes it into a list
csvFile = open("CloudFraction1_2002.csv")
csvReader = csv.reader(csvFile, delimiter=',')
stringMatrix = list(csvReader)

#This is needed to find the dimensions of the array
numCols = len(stringMatrix[0])
numRows = len(stringMatrix)

#Creates an empty NumPy array 
grid = np.empty([numRows, numCols, 3],dtype=np.uint8)

#The values in the brakets represent RGB values that will show the
cc1 = [255, 0, 0]
cc2 = [255, 124, 0]
cc3 = [255, 243, 0]
cc4 = [193, 255, 0]
cc5 = [100, 255, 0]
cc6 = [0, 255, 54]
cc7 = [0, 255, 158]
cc8 = [0, 255, 255]
cc9 = [0, 174, 255]
cc10 = [0, 62, 255]
csvFile.seek(0)

#Assigns the values in the CSV file to the RGB values defined earlier
rownum = -1
for row in csvReader:
   rownum += 1
   colnum = -1
   for value in row:
       colnum += 1
       if float(value) < 0.1:
            grid[rownum, colnum] = cc1
       elif 0.1 < float(value) < 0.2:
           grid[rownum,colnum] = cc2
       elif 0.2 < float(value) < 0.3:
           grid[rownum,colnum] = cc3
       elif 0.3 < float(value) < 0.4:
           grid[rownum,colnum] = cc4
       elif 0.4 < float(value) < 0.5:
           grid[rownum,colnum] = cc5
       elif 0.5 < float(value) < 0.6:
           grid[rownum,colnum] = cc6
       elif 0.6 < float(value) < 0.7:
           grid[rownum,colnum] = cc7
       elif 0.7 < float(value) < 0.8:
           grid[rownum,colnum] = cc8
       elif 0.8 < float(value) < 0.8:
           grid[rownum,colnum] = cc9
       elif 0.9 < float(value) <= 1:
           grid[rownum,colnum] = cc10

               
#Clears and makes the plot
plt.clf()
plt.suptitle("Cloud Cover Percentage in 2002", y=.80)
plt.imshow(grid)
plt.axis('off')
plt.show()