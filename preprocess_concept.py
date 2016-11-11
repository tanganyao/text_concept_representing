
"""
文本预处理：分词，去停用词，是否在语义字典中，预处理后的数据以列表返回
[word_syn_fd, cate, path] 
word_syn_fd: 同义词集合的频率字典
cate : 目录
path ：文件目录（包含cate的值）
"""
import nltk
from nltk.corpus import stopwords
from nltk.corpus import PlaintextCorpusReader
import re
from nltk.corpus import wordnet as wn

def preprocess():

	file_path = []
	categories = []
	document_processed = []
	words_syn = []
	word_synsets = []

	corpus_root = "E:\\Text_represent\\20_newsgroups"
	wordlists = PlaintextCorpusReader(corpus_root, '.*')
	
	for path in wordlists.fileids():
		cate = path.split('/')[0]
		file_name = path.split('/')[1]
		#categories.append(cate)
		#file_path.append(path)
		#print(cate)
	
		words = wordlists.words(path)
		#words_token = nltk.word_tokenize(words)
		#正则表达式分词
		#words_re = re.split(r'\W+', words)	

		#停用词
		en_stopwords = stopwords.words('english')
		words_stop = [w for w in words if w.lower() not in en_stopwords]	
		english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '-', '_']	
		#英文符号过滤
		words_filtered = [word.lower() for word in words_stop if word not in english_punctuations]
		
		#porter词干提取器
		porter = nltk.PorterStemmer()
		
		for word in words_filtered:
			synset=wn.synsets(word)
			if len(synset):
				words_syn.append(porter.stem(word))

		#for word, num in word_dicts: 	#同义词集合
		#file_word = nltk.ConditionalFreqDist()
		#file_word.append(file_name, words_stem)
		#同义词集合
		for word in words_syn:
			w_synset = wn.synsets(word)
			for w in w_synset:
				word_synsets.append(w)				
		word_syn_fd = nltk.FreqDist(word_synsets)
		#word_syn_fd = nltk.FreqDist(words_syn)		#以词为特征来测试
		
		#word_syn_fd = sorted(word_fd.items(), key=lambda d:-d[1] )[:10000]
		#print(word_syn_fd)
		#print(len(word_syn_fd))
		#w_synsets = nltk.FreqDist(word_syn_fd)
		document_processed.append([word_syn_fd, cate, path])
	#print(document_processed)
	return document_processed
	#print(len(file_list))
#preprocess()