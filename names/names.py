import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Default initial code for duplicates
# duplicates = []
# for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
# runtime - 7.0s


# Check out difference removing one of the for loops
# duplicates = []
# for name_1 in names_1:
#    if name_1 in names_2:
#        duplicates.append(name_1)
# runtime - 1.3s


# Tried using dictionary with union of set operations
duplicates = set(names_1) & set(names_2)
# runtime - .009s


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

