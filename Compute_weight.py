from __future__ import division
import tf_df_concept
import math

'''
用于操作二维字典的函数
'''
def addtwodimdict(thedict, key_a, key_b, val): 
    if key_a in thedict:
        thedict[key_a].update({key_b: val})
    else:
        thedict.update({key_a:{key_b: val}})
'''
权重计算
'''
		
def Compute_weight():
	
	TF_result = tf_df_concept.Tf_Compute()
	
	word_weight_dict = {}
	files_num = len(TF_result)
	
	#计算特征权重
	for path in TF_result:
		for word in TF_result[path]:
			word_n = int(TF_result[path][word][0])
			#word_sum = TF_result[path][word][1]
			with_word_sum = TF_result[path][word][2]
			addtwodimdict(word_weight_dict, path, word, (math.log(word_n + 1,2))* math.pow((math.log(files_num/with_word_sum)), 2))
	
	return word_weight_dict