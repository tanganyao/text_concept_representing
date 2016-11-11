#import preprocess_concept
from __future__ import division
import tf_df_concept
import nltk
from nltk.corpus import wordnet as wn
import Compute_weight
import math
import comput_df


'''
用于操作二维字典的函数
'''
def addtodict(thedict, key_a, key_b, val): 
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})
	
'''
同义词概念链各个概念的权重调整
'''
def synset_chain():
	
	word_weight_dict = Compute_weight.Compute_weight()
	#document_processed = preprocess_concept.preprocess()
	TF_result = tf_df_concept.Tf_Compute()
	#返回(path, word, word_in_chain) 包含路径，词，及词的概念链字典
	syn_document = []
	#计算目录数
	cate_num = len(set([path.split('/')[0] for path in word_weight_dict]))
	#print(cate_num)
	#print(word_weight_dict)
	#概念链的权重计算
	for path in word_weight_dict:
		cate = path.split('/')[0]
		for word in word_weight_dict[path]:
			#print(word)
			weight = word_weight_dict[path][word]
			word_syn = wn.synset( (str(word).split('(')[1]).split(')')[0][1:-1] )  #同义词
			hyper_set = word_syn.hypernyms()		#上位词集合
			paths = word_syn.hypernym_paths()	#路径链
			path_sum = len(paths)	#路径总数
			sum = 0
			#求beta
			'''
			for i in range(path_sum):
				for j in range(len(synset_in_apath)):
					sum += math.pow(0.6, j)
			beta = path_sum / sum
			'''
			temp_X = 0
			temp_Y = 0
			word_in_chain = {}
			#每条路径上的同义词集合
			for i in range(path_sum):
				s = [synset for synset in paths[i]]
				synset_in_apath = s[::-1]
				for j in range(len(synset_in_apath)):
					'''
					#求alpha
					alpha=0
					computed = comput_df.compute_num()
					word_in_all = computed[0]
					word_in_cate = computed[1]
					if synset_in_apath[j] in word_in_cate[cate]:
						with_word_cate = word_in_cate[cate][synset_in_apath[j]]
					else:
						with_word_cate = 0
					if synset_in_apath[j] in word_in_all:
						with_word_sum = word_in_cate[cate][synset_in_apath[j]]
					else:
						with_word_sum = 0
					for i in range(cate_num):
						temp_X += math.pow(with_word_cate-with_word_sum/cate_num, 2)
						temp_Y += with_word_cate
					if temp_Y :
						alpha = math.pow(math.pow(temp_X, 0.5) / temp_Y, 0.5)
					'''
					chain_word_weight = weight * pow(0.6, j)
					if chain_word_weight:
						addtodict( word_in_chain, i , synset_in_apath[j], chain_word_weight )
			#保存各个词的概念链字典		
			syn_document.append((path, word, word_in_chain))	
	
	print(syn_document)
	return syn_document
synset_chain()		
		