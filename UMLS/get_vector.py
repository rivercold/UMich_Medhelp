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
for line in d_lines:
	line = line.rstrip()
	print(line)
	num = num + 1
	try:
		vector = model[line]
		vector_paper = model_paper[line]
		vector_wiki = model_wiki[line]
		write_file.write(line+"\tDis_Syn\t")
		for item in vector:
			write_file.write(str(item)+"\t")
		for item in vector_wiki:
			write_file.write(str(item)+"\t")
		for item in vector_paper:
			write_file.write(str(item)+"\t")
		write_file.write("\n")
	except:
		#write_file.write(str(line)+"\tdt_sy\tnot in the vocaburary\n")
		print(str(line)+"\td\tnot in the vocaburary")
num = 0
for line in s_lines:
        line = line.rstrip()
        print(line)
	num = num + 1 
        try:
                vector = model[line]
                vector_paper = model_paper[line]
                vector_wiki = model_wiki[line]
                write_file.write(line+"\tMed_Devices\t")
                for item in vector:
                        write_file.write(str(item)+"\t")
                for item in vector_wiki:
                        write_file.write(str(item)+"\t")
                for item in vector_paper:
                        write_file.write(str(item)+"\t")
                write_file.write("\n")
        except:
                #write_file.write(str(line)+"\tMed_Devices\tnot in the vocaburary\n")
                print(str(line)+"\tmed_devices\tnot in the vocaburary")
num = 0
for line in t_lines:
        line = line.rstrip()
        print(line)
	num = num + 1
        try:
                vector = model[line]
                vector_paper = model_paper[line]
                vector_wiki = model_wiki[line]
                write_file.write(line+"\tBody_Part\t")
                for item in vector:
                        write_file.write(str(item)+"\t")
                for item in vector_wiki:
                        write_file.write(str(item)+"\t")
                for item in vector_paper:
                        write_file.write(str(item)+"\t")
                write_file.write("\n")
        except:
                #write_file.write(str(line)+"\tBody_Part\tnot in the vocaburary\n")
                print(str(line)+"\tbody part \tnot in the vocaburary")

