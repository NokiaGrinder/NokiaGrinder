import random as r
import matplotlib.pyplot as plt
import time
from mpl_toolkits import mplot3d
from collections import defaultdict

num = int(input("Enter lines created: "))

proj = plt.axes(projection="3d")

start_time = time.time()
count = 0
remove = []
grandx = [0]
grandy = [0]  
grandz = [0]   
indexvector = [[0, 0, 0]] 

for k in range(num): #the num variable determines how many lines (edges) are created
    ranx = r.randint(-1, 1)
    rany = r.randint(-1, 1)
    ranz = r.randint(-1, 1)
    #Creates coordinates of x y z to be added onto the previous xyz coords
    while ranx + grandx[k] == grandx[k] and rany + grandy[k] == grandy[k] and ranz + grandz[k] == grandz[k]:
        ranx = r.randint(-1, 1)
        rany = r.randint(-1, 1)
        ranz = r.randint(-1, 1)
    #Ensures that the new point does not have the same cords as the previous point
    grandx.append(ranx + grandx[k])
    grandy.append(rany + grandy[k])
    grandz.append(ranz + grandy[k])
    #These arrays are what is going to be plotted at the end
    indexvector.append([ranx, rany, ranz])
    #The vector created is stored as an array in indexvector
for k in range(num-1):
    if indexvector[k-1][0] == indexvector[k][0] and indexvector[k+1][0] == indexvector[k][0]:
        if indexvector[k-1][1] == indexvector[k][1] and indexvector[k+1][1] == indexvector[k][1]:
            if indexvector [k-1][2] == indexvector[k][2] and indexvector[k+1][2] == indexvector[k][1]:
                #This is all a comparison with each coordinate to see if the previous point and the next point uses the same vector, if so, then we add that to the remove array
                #These points are considered "Redundency Points"
                remove.append(k)

for l in remove:
    del grandx[l]
    del grandy[l]
    del grandz[l]
    for i in range(len(remove)):
        remove[i] -= 1
        #because remove is storing the index of the redundency point, we need to decrement that index after deleting one of the points
        #This is so that the index of the redundency point takes in account the smaller array

#removes all the redundency points in the grand arrays 
a = [grandx[0], grandx[num-len(remove)]]
b = [grandy[0], grandy[num-len(remove)]]
c = [grandz[0], grandz[num-len(remove)]]


proj.plot(a, b, c)
proj.plot(grandx, grandy, grandz)
#plots lmao

print(len(remove)-1)
#Counts how many redundency points have been removed
print("~0.156%. of points removed")
#This is the program's average percentage of redundency points removed
#NOT FULLY ACCURATE
print("max")
print(max(grandx))
print(max(grandy))
print(max(grandz))
print("min")
print(min(grandx))
print(min(grandy))
print(min(grandz))

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.4f} seconds") #Time to be executed can be shown
plt.show()
