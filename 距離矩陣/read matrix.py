import pickle
with open("distance_final.txt", "rb") as fp:   # Unpickling
    b = pickle.load(fp)
print(b[50][10])
print(b[50])

