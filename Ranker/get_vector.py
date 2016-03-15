import gensim

d_file = open("./d_s_t/d_list.txt","r")
s_file = open("./d_s_t/s_list.txt","r")
t_file = open("./d_s_t/t_list.txt","r")
d_lines = d_file.readlines()
s_lines = s_file.readlines()
t_lines = t_file.readlines()

model = gensim.models.Word2Vec.load("/storage4/foreseer/users/keyangxu/word2vec/model/final/MedHelp.model")
print(model.most_similar("nurse"))
write_file = open("MedHelp_ranker_list","w")
for line in d_lines:
	line = line.rstrip()
	print(line)
	try:
		vector = model[line]
		write_file.write(line+"\td\t")
		for item in vector:
			write_file.write(str(item)+"\t")
		write_file.write("\n")
	except:
		write_file.write(str(line)+"\td\tnot in the vocaburary\n")
		print(str(line)+"\td\tnot in the vocaburary")

for line in s_lines:
	line = line.rstrip()
	print(line)
	try:
		vector = model[line]
		write_file.write(line+"\ts\t")
		for item in vector:
			write_file.write(str(item)+"\t")
		write_file.write("\n")
	except:
		write_file.write(str(line)+"\td\tnot in the vocaburary\n")
		print(str(line)+"\td\tnot in the vocaburary")

for line in t_lines:
	line = line.rstrip()
	print(line)
	try:
		vector = model[line]
		write_file.write(line+"\tt\t")
		for item in vector:
			write_file.write(str(item)+"\t")
		write_file.write("\n")
	except:
		write_file.write(str(line)+"\td\tnot in the vocaburary\n")
		print(str(line)+"\td\tnot in the vocaburary")
