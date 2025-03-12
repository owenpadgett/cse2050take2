# This program generates a list of numbers and writes them to a file.
import random

##### Generate list of numbers #####
n = 1500 # Max is 2000 due to memory constraints on the gradescope
         # containers that run your submissions
L = [i for i in range(n)]
L.append(5)

##### Create file to write to #####
f = open(f"./numbers.txt", "w")

##### Write numbers to file #####
for item in L:
    f.write(str(item))
    f.write(" ")

#### Close the file ####
f.close()