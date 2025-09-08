import random as r
import matplotlib.pyplot as plt
from collections import defaultdict
import time
from mpl_toolkits import mplot3d

num = input("Enter lines created: ")

proj = plt.axes(projection="3d")

start_time = time.perf_counter()

remove = []
count = 0
inc = 0

grandx = defaultdict(int)
grandx["0"] = 0 
grandy = defaultdict(int)
grandy["0"] = 0 
grandz = defaultdict(int)
grandz["0"] = 0 

indexvector = defaultdict(list)
indexvector["0"] = [0, 0, 0]

for i in range(int(num)):
    ranx = r.randint(-1, 1)
    rany = r.randint(-1, 1)
    ranz = r.randint(-1, 1)
    while grandx[str(i)] + ranx == grandx[str(i)] and grandy[str(i)] + rany == grandy[str(i)] and grandz[str(i)] + ranz == grandz[str(i)]:
        ranx = r.randint(-1, 1)
        rany = r.randint(-1, 1)
        ranz = r.randint(-1, 1)
    grandx[str(i+1)] = grandx[str(i)] + ranx
    grandy[str(i+1)] = grandy[str(i)] + rany
    grandz[str(i+1)] = grandz[str(i)] + ranz
    indexvector[str(i+1)] = [ranx, rany, ranz]
    inc += 1
    if inc == 3:
        inc = 0
        if indexvector[str(i-2)][0] == indexvector[str(i-1)][0] and indexvector[str(i-1)][0] == indexvector[str(i)][0]:
            if indexvector[str(i-2)][1] == indexvector[str(i-1)][1] and indexvector[str(i-1)][1] == indexvector[str(i)][1]:
                if indexvector[str(i-2)][2] == indexvector[str(i-1)][2] and indexvector[str(i-1)][2] == indexvector[str(i)][2]:
                #This is all a comparison with each coordinate to see if the previous point and the next point uses the same vector, if so, then we add that to the remove array
                #These points are considered "Redundency Points"
                    del grandx[str(i-1)]
                    del grandy[str(i-1)]
                    del grandz[str(i-1)]
                    count += 1

print(count)

x = list(grandx.values())
y = list(grandy.values())
z = list(grandz.values())

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")

plt.plot(x, y, z)

plt.show()
