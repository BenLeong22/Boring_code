from function_set import *
import json
import pickle
import pandas as pd

df = pd.read_excel (r'地點.xlsx')
point_name=[None]
point_name.extend(df["地點"])
lat=df["經度"]
lon=df["緯度"]

matrix_distance=[]
matrix_duration=[]
idx_r=0
idx_c=0
while idx_r < len(point_name):
    matrix_distance_row=[]
    matrix_duration_row=[]
    idx_c=0
    while idx_c<len(point_name):
        if idx_r==0 and idx_c==0:
            matrix_distance_row.extend(point_name)  #命名
            matrix_duration_row.extend(point_name)  #命名
        elif idx_r>0:
            if idx_c==0:
                matrix_distance_row.append(point_name[idx_r])
                matrix_duration_row.append(point_name[idx_r])
            else:
                data =osmr(lon[idx_r-1],lat[idx_r-1],lon[idx_c-1],lat[idx_c-1])

                matrix_distance_row.extend([data["distance"]])
                matrix_duration_row.extend([data["duration"]])
        idx_c+=1
    matrix_distance.append(matrix_distance_row)
    matrix_duration.append(matrix_duration_row)
    idx_r+=1

with open("matrix_distance_code.txt", "wb") as fp:
    pickle.dump(str(matrix_distance), fp)

with open("matrix_duration_code.txt", "wb") as fp:
    pickle.dump(str(matrix_duration), fp)

with open("matrix_distance_uft8.txt", "w") as fp:
    fp.write(str(matrix_distance))

with open("matrix_duration_uft8.txt", "w") as fp:
    fp.write(str(matrix_duration))