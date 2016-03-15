#coding=utf8 
import os
import time
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
word_dict = {}
class MySentences(object):
	def __init__(self,dirname):
		self.dirname = dirname
	
	def __iter__(self):
		blank = 0
		count = 0 
		for fname in os.listdir(self.dirname):
			for line in open(os.path.join(self.dirname,fname)):
				try:
					count = count + 1
					if count>300000000:
						break
					token =  WordPunctTokenizer().tokenize(line)
					yield token
				
				except:
					print("blank")
					blank = blank + 1
				#print(line)
		#print("blank is " + str(blank))
	def len(self):
		count = 0
		for i in self:
			count = count + 1
		print("count is " + str(count))
		return count

#sentences = word2vec.LineSentence('comment/comment_table_cleaned.txt')
#sentences = sentences.decode('latin-1').encode('utf8')
print("Program Starts")
sentences = MySentences('/storage4/users/vgvinodv/MedKnowledgeGraph/data/wiki/')
model = gensim.models.Word2Vec(sentences,min_count=5,size=100,workers=6)
#print("The lengh of sentences is ")
#print(str(sentences.len()))
#model = gensim.models.Word2Vec.load('../../model/new/new_wiki.model')
#model.train(sentences)
#b = model.most_similar(positive=['feminism'], topn=1)
#print(b)
model.save('../../model/new/new_wiki.model')
print(model['cancer'])
print(model.most_similar(['nurse'],topn=3))
print(model.most_similar(['pimples'],topn=10))
#print(model.most_similar(['cancer'],topn=8))
#print(model.most_similar(positive=["pain", "disease"],topn=3))
