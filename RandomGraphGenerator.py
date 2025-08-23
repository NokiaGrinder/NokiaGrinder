import random as r
import matplotlib.pyplot as plt
import numpy as np
import time

num = int(input("Enter lines created: "))

start_time = time.time()

grandx = [0]
grandy = [0]      

for k in range(num): #the num variable determines how many lines (edges) are created
    ranx = r.randint(-1, 1) + grandx[k]
    rany = r.randint(-1, 1) + grandy[k]
    posx = grandx[k]
    posy = grandy[k]
    grandx.append(ranx)
    grandy.append(rany)
    randomx = [posx, ranx]
    randomy = [posy, rany]
    x = np.array(randomx)
    y = np.array(randomy)
    plt.plot(x, y, "o")
    plt.plot(x, y)
    

plt.grid()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.4f} seconds") #Time to be executed can be shown
plt.show()
