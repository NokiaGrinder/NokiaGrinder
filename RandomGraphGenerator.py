import random as r
import matplotlib.pyplot as plt
import time

num = int(input("Enter lines created: "))

start_time = time.time()

grandx = [0]
grandy = [0]      

for k in range(num): #the num variable determines how many lines (edges) are created
    ranx = r.randint(-1, 1) + grandx[k]
    rany = r.randint(-1, 1) + grandy[k]
    grandx.append(ranx)
    grandy.append(rany)
    randomx = [grandx[k], ranx]
    randomy = [grandy[k], rany]
    plt.plot(randomx, randomy)
    
plt.grid()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Code execution time: {elapsed_time:.4f} seconds") #Time to be executed can be shown
plt.show()
