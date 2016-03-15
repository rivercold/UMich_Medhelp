import gensim
print("loading models")
model_wiki  = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/whole_wiki.model")
#model_forum = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/MedHelp.model")
#model_paper = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/whole_PubMed.model")
print("loading succesfully!")
d_t_lines = open("diseases-treatment.txt","r").readlines()
d_s_lines = open("diseases-symptoms.txt","r").readlines()

d_t_file = open("d_t_s_wiki.txt","w")
#d_s_file = open("d_s_forum.txt","w")




for line in d_t_lines:
	line = line.rstrip()
	line = line.replace(" ","")
	try:
		[disease,treat] = line.split("\t")
		vector = model_wiki[disease]-model_wiki[treat]
		d_t_file.write(disease+" "+treat+"\t"+"d-t"+"\t")
		for item in vector:
			d_t_file.write(str(item)+"\t")
		d_t_file.write("\n")
	except:
		print("not in vocaburary")
		d_t_file.write("not in vocaburary\n")



for line in d_s_lines:
	line = line.rstrip()
	line = line.replace(" ","")
	try:
		[disease,treat] = line.split("\t")
		vector = model_wiki[disease]-model_wiki[treat]
		d_t_file.write(disease+" "+treat+"\t"+"d-s" +"\t")
		for item in vector:
			d_t_file.write(str(item)+"\t")
		d_t_file.write("\n")
	except:
		print("not in vocaburary")
		d_t_file.write("not in vocaburary\n")
