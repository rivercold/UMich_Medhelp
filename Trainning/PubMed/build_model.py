#coding=utf8 
import os
import gensim, logging
from gensim.models import word2vec
import cython
from nltk.tokenize import WordPunctTokenizer
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#==========ijjjjjjjjkkkgghhgggggggggggggggg=====================================================================
# sentences = [['first', 'second','sentence'], ['second', 'sentence']]
# model = gensim.models.Word2Vec(sentences, min_count=1,workers=3)
# print(model.similarity('first','sentence'))
#===============================================================================
class MySentences(object):
	def __init__(self,dirname):
		self.dirname = dirname
	
	def __iter__(self):
		blank = 0
		count = 0 
		for dname in os.listdir(self.dirname):
			print(dname)
			for line in open(os.path.join(self.dirname,dname)):
				try:
					#print(line)
					line = line.split("\t")[1]
					token =  WordPunctTokenizer().tokenize(line)
				except:
					blank = blank + 1
				yield token
		#print("blank is " + str(blank))
	def len(self):
		count = 0
		for i in self:
			count = count + 1
		return count

#sentences = word2vec.LineSentence('comment/comment_table_cleaned.txt')
#sentences = sentences.decode('latin-1').encode('utf8')
print("Program Starts")
sentences = MySentences('/storage4/users/vgvinodv/Metamapped_MedLine/medline/parsedData/')
model = gensim.models.Word2Vec(sentences,min_count=5,size=100,workers=6)
#print("The lengh of sentences is ")
#print(str(sentences.len()))
#model = gensim.models.Word2Vec.load('../model/Med_Paper.model')
#model.train(sentences)
#b = model.most_similar(positive=['feminism'], topn=1)
#print(b)
model.save('../../model/final/whole_PubMed.model')
model.save_word2vec_format('../../model/final/whole_PubMed.model.bin', binary=True)
print(model.most_similar(['nurse'], topn=10))
#print(model['insulin'])
print(model.most_similar(['Nurse'],topn=3))
print(model.most_similar(['cancer'],topn=10))
print(model.most_similar(['pimple'],topn=8))
print(model.most_similar(positive=["pain", "disease"],topn=3))
