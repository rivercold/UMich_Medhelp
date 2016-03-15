'''
2014.8.28
Keyang
'''
import math
def calc_distance(point,centroid):
    dim = len(point)
    sum = 0.0
    for i in range(dim):
        sum = sum + (centroid[i]-point[i])*(centroid[i]-point[i])
    return math.sqrt(sum/float(dim))

#print(calc_distance([1,2,3],[1,4,6]))
import os
class_list = ["Dis_Syn","Med_Devices","Body_Part"]
class_num = len(class_list)
UMLS_num_list = [0]*class_num
centroid_dict = {}
for i in range(0,class_num):
    centroid_dict[i] = [0.0]*100
#print(centroid_dict[1])
UMLS_file = open("../file/UMLS_term_list","r")
UMLS_lines = UMLS_file.readlines()
for line in UMLS_lines:
    line = line.rstrip()
    #print(len(line.split("\t")))
    term = line.split("\t")[0]
    classification = line.split("\t")[1]
    temp_split = line.split("\t")
    #print(classification)
    #2-101 Med_Help
    for i in range(class_num):
        if classification == class_list[i]:
            UMLS_num_list[i] = UMLS_num_list[i] + 1
            for j in range(2,102):
                centroid_dict[i][j-2] = centroid_dict[i][j-2] + float(temp_split[j])
            break
for i in range(class_num):
    #print(UMLS_num_list[i])
    for j in range(100):
        centroid_dict[i][j] = centroid_dict[i][j]/float(UMLS_num_list[i])
    print((centroid_dict[i]))
    #102-201 Wiki
    #202-301 Pub_Med
    
    
# Guess for MedHelp
#print(type(centroid_dict[i]))
MedHelp_lines = open("../file/body_test","r").readlines()
#print(len(MedHelp_lines))
right_num = 0
total_num = 0
for line in MedHelp_lines:
    line = line.rstrip()
    temp = line.split("\t")
    print(len(temp))
    term = temp[0]
    classification = temp[1]
    vector = [0.0]*100
    if classification == "Body_Part":
        total_num = total_num + 1
        for i in range(100):
            try:
                vector[i] = float(temp[i+2])
            except:
                print(term)
        distance_list = [0.0]*class_num
        for i in range(class_num):
            distance_list[i] = calc_distance(vector,centroid_dict[i])
        print(distance_list)
        flag = 1
        for j in range(class_num):
            if distance_list[2]>distance_list[j]:
                flag = 0
                break
        if flag==1:
            right_num = right_num + 1
print(right_num)
print(total_num)
