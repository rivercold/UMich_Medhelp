#coding=utf8 
import os
import time
import gensim, logging
from gensim.models import word2vec
import cython 
from nltk.tokenize import WordPunctTokenizer
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#===============================================================================
# sentences = [['first', 'second','sentence'], ['second', 'sentence']]
# model = gensim.models.Word2Vec(sentences, min_count=1,workers=3)
# print(model.similarity('first','sentence'))
#===============================================================================
word_dict = {}
class MySentences(object):
	def __init__(self,dirname):
		self.dirname = dirname
	
	def __iter__(self):
		blank = 0
		count = 0 
		for fname in os.listdir(self.dirname):
			print(fname)
			if fname =="new_comment_table.txt":
				for line in open(os.path.join(self.dirname,fname)):
					try:
						line = line.split("\t")[5]
						token =  WordPunctTokenizer().tokenize(line)
						yield token
				
					except:
						blank = blank + 1
			else:
				for line in open(os.path.join(self.dirname,fname)):
					try:
						line = line.split("\t")[2] + line.split("\t")[6]
						token = WordPunctTokenizer().tokenize(line)
						yield token
					except:
						blank = blank + 1
				#print(line)
		#print("blank is " + str(blank))
	def len(self):
		count = 0
		for i in self:
			count = count + 1
		return count

#sentences = word2vec.LineSentence('comment/comment_table_cleaned.txt')
#sentences = sentences.decode('latin-1').encode('utf8')
print("Program Starts")
sentences = MySentences('/storage4/foreseer/users/keyangxu/word2vec/data/MedHelp')
model = gensim.models.Word2Vec(sentences,min_count=5,size=100,workers=5)
#print("The lengh of sentences is ")
#print(str(sentences.len()))
#model = gensim.models.Word2Vec.load('../model/MedHelp_tokenizer.model')
#model.train(sentences)
#b = model.most_similar(positive=['feminism'], topn=1)
#print(b)
model.save('../../model/final/MedHelp.model')
print(model['nurse'])
print(model.most_similar(['nurse'],topn=3))
#print(model.most_similar(['agree'],topn=10))
print(model.most_similar(['cancer'],topn=8))
#print(model.most_similar(positive=["pain", "disease"],topn=3))
