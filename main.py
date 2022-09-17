import pandas as pd
import numpy as np
"Costruisco il dataset"

columns_data = ["Dimension", "X_cor", "Y_cor"]
df = pd.read_csv("./dati.csv", sep=';')
data = pd.DataFrame(columns=columns_data, data=df)

"Lunghezze"

number_objects = len(data.index)
number_objects_small = len(data[data["Dimension"]== "Small"])
number_objects_medium = len(data[data["Dimension"]== "Medium"])
number_objects_big = len(data[data["Dimension"]== "Big"])

"Centroide"

X_column = data["X_cor"].sum()
Y_column = data["Y_cor"].sum()
X_centroid = X_column / number_objects
Y_centroid = Y_column / number_objects

"Small Points"
Small_points = data[data["Dimension"] == "Small"]
"Medium Points"
Medium_points = data[data["Dimension"] == "Medium"]
"Big Points"
Big_points = data[data["Dimension"] == "Big"]
print (Small_points)
print (Medium_points)
print (Big_points)
centroid = (X_centroid, Y_centroid)

"Liste"

list_small = []
list_medium = []
list_big = []

def compute_distance (point, centroid):
    """
    Return euclidean distance between points p and q
    assuming both to have the same number of dimensions
    """

    difference_squared = 0
    for (point_i,centroid_i) in zip (point, centroid):
        difference_squared += (point_i - centroid_i)**2
        real_distance = difference_squared**0.5
    return real_distance


Small_points = Small_points.reset_index()  # make sure indexes pair with number of rows
for index, row in Small_points.iterrows():
        point_X = row['X_cor']
        point_Y = row['Y_cor']
        point = (point_X,point_Y)
        distance = compute_distance(point,centroid)
        list_small.append(distance)

Medium_points_points = Medium_points.reset_index()  # make sure indexes pair with number of rows
for index, row in Medium_points_points.iterrows():
        point_X = row['X_cor']
        point_Y = row['Y_cor']
        point = (point_X,point_Y)
        distance = compute_distance(point,centroid)
        list_medium.append(distance)

Big_points = Big_points.reset_index()  # make sure indexes pair with number of rows
for index, row in Big_points.iterrows():
        point_X = row['X_cor']
        point_Y = row['Y_cor']
        point = (point_X,point_Y)
        distance = compute_distance(point,centroid)
        list_big.append(distance)

"Some prints to check the results"
#print("SMALL")
#print(list_small)
#print("MEDIUM")
#print(list_medium)
#print("BIG")
#print(list_big

list_small.sort()
list_medium.sort()
list_big.sort()
print ("SMALL")
print(list_small)
print ("MEDIUM")
print(list_medium)
print("BIG")
print(list_big)

"Computing quartiles..."

"UNIFIED"

"lower_quartile_medium_big"
list_unified_medium_big= list_big + list_medium
list_unified_medium_big.sort()
lower_quartile_MB = np.percentile(list_unified_medium_big,25)
"upper_quartile_medium_small"
list_unified_medium_small= list_small + list_medium
list_unified_medium_small.sort()
upper_quartile_MS = np.percentile(list_unified_medium_small,75)

"SMALL"

"upper quartile small"
upper_quartile_small = np.percentile(list_small,75)
print ("Upper_S")
print(upper_quartile_small)

"MEDIUM"

"lower_quartile_medium"
lower_quartile_medium = np.percentile(list_medium,25)
print ("Lower_M")
print (lower_quartile_medium)
"upper quartile medium"
upper_quartile_medium = np.percentile(list_medium,75)
print("Upper_M")
print(upper_quartile_medium)

"BIG"

"lower_quartile_big"
lower_quartile_big = np.percentile(list_big,25)
print ("Lower big")
print (lower_quartile_big)
"upper quartile big"
upper_quartile_big = np.percentile(list_big,75)
print("Upper_Big")
print(upper_quartile_big)


"Computing the 3 values..."
N_s = 0
for i in range (0,len(list_small)):
    if list_small[i] > lower_quartile_MB:
        N_s = N_s + 1
N_l = 0
for i in range (0,len(list_big)):
    if list_big[i] < upper_quartile_MS:
        N_l = N_l + 1
N_tmp = 0
for i in range (0,len(list_medium)):
    if list_medium[i] > lower_quartile_big:
        N_tmp = N_tmp + 1
for i in range (0,len(list_medium)):
    if list_medium[i] < upper_quartile_small:
        N_tmp = N_tmp + 1

N_m = N_tmp / 2

"Computing the degree of separation..."

S_e = 100*(1 - (N_s + N_l + N_m)/number_objects)
print ("Final degree of separation")
print(S_e)

final_results = []
final_results.append(S_e)


print(final_results)





