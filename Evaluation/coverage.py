import gensim

d_file = open("./term_file/Disease_Syndrom_Classified.txt","r")
s_file = open("./term_file/Medical_Devices_Classified.txt","r")
t_file = open("./term_file/Body_Part_Classified.txt","r")
d_lines = d_file.readlines()
s_lines = s_file.readlines()
t_lines = t_file.readlines()

model = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/MedHelp.model")
model_wiki = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/whole_wiki.model")
model_paper = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/whole_PubMed.model")
write_file = open("UMLS_term_list","w")
num = 0
for line in s_lines:
	line = line.rstrip()
	print(line)
	try:
		vector = model[line]
		num = num + 1
	except:
		print(str(line)+"\td\tnot in the vocaburary")
num_wiki= 0
for line in s_lines:
        line = line.rstrip()
        print(line)
        try:
                vector_wiki = model_wiki[line]
		num_wiki = num_wiki + 1 
        except:
                print(str(line)+"\tmed_devices\tnot in the vocaburary")
num_paper = 0
for line in s_lines:
        line = line.rstrip()
        print(line)
        try:
                vector_paper = model_paper[line]
		num_paper = num_paper + 1
        except:
                #write_file.write(str(line)+"\tBody_Part\tnot in the vocaburary\n")
                print(str(line)+"\tbody part \tnot in the vocaburary")
total = len(s_lines)
print("Disease has " + str(len(s_lines)))
print("MedHelp has " + str(num)+" coverage is " + str(float(num)/float(total)))
print("Wiki has " + str(num_wiki)+" coverage is " + str(float(num_wiki)/float(total)))
print("Paper has " + str(num_paper)+ "coverage is " + str(float(num_paper)/float(total)))
