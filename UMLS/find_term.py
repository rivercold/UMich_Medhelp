import os

MRSTY_file = open("/storage4/users/vgvinodv/MedKnowledgeGraph/UMLSfiles/MRSTY.RRF.classified")
Concepts_file = open("/storage4/users/vgvinodv/MedKnowledgeGraph/UMLSfiles/UMLS.allConcepts.txt")
write_file = open("term_file/Health_Care_Activity_Classified.txt","w")

C_list = []
MRSTY_lines = MRSTY_file.readlines()
for line in MRSTY_lines:
	line = line.rstrip()
	T = (line.split("|")[1])
	if T == "T058":
		C = line.split("|")[0]
		if C not in C_list:
			C_list.append(C)
			#print(C+"|"+T)

print("Length of C_list is " + str(len(C_list)))
judge = {}
C_dict= {}
Concepts_lines = Concepts_file.readlines()
for line in Concepts_lines:
	line = line.rstrip()
	C = line.split("\t")[0]
	if  not judge.has_key(C):
		judge[C] = 0
		line = line.replace(C+"\t","")
		C_dict[C] = line
num = 0
word_dict = {}
for item in C_list:
	try:
		#print(C_dict[item])
		words = C_dict[item]
		words = words.split("\t")
		for i in range(len(words)):
			#print(words[i])
			if len(words[i].split(" "))==1:
				if len(words[i].split(","))==1:
					word = words[i].lower()
					if not word_dict.has_key(word):
						num = num + 1
						print("******"+word)
						print(C_dict[item]+"*****")
						word_dict[word] = 1
	except:
		print("error")
print("Length of single word is "+ str(num))
for key in word_dict:
	write_file.write(str(key)+"\n")
                #write_file.write(line+"\n")	
	
		#temp = line.split("\t")
		#for i in range(1,len(temp)):
		#	term = temp[i]
		#	if len(term.split(" "))==1:
		#		write_file.write(term.lower())
		#		print(term)
		#		judge[C] = 1
		#if judge[C]==1:
		#	write_file.write("\n")	

#print("Length of C_dict is "+ str(num))
