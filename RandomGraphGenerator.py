import random as r
import matplotlib.pyplot as plt
import time

num = int(input("Enter lines created: "))

start_time = time.time()
count = 0
remove = []
grandx = [0]
grandy = [0]     
indexvector = [[0, 0]] 

for k in range(num): #the num variable determines how many lines (edges) are created
    ranx = r.randint(-1, 1)
    rany = r.randint(-1, 1)
    while ranx + grandx[k] == grandx[k] and rany + grandy[k] == grandy[k]:
        ranx = r.randint(-1, 1)
        rany = r.randint(-1, 1)
    grandx.append(ranx + grandx[k])
    grandy.append(rany + grandy[k])
    indexvector.append([ranx, rany])
for k in range(num-1):
    if indexvector[k-1][0] == indexvector[k][0] and indexvector[k+1][0] == indexvector[k][0]:
        if indexvector[k-1][1] == indexvector[k][1] and indexvector[k+1][1] == indexvector[k][1]:
            remove.append(k)

for l in remove:
    del grandx[l]
    del grandy[l]
    for i in range(len(remove)):
        remove[i] -= 1
plt.plot(grandx, grandy)

for i in remove:
    count += 1
print(count)
print("~1.56%. of redundancy points removed")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.4f} seconds") #Time to be executed can be shown
plt.show()
