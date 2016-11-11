from __future__ import division
import math
import preprocess_concept
import comput_df

'''
word_in_allfiles_stat{A:n1,B:n2,⋯⋯}
word_in_afile_stat{a:{A:[aA,suma],B:[aB,suma],⋯⋯}, ⋯⋯}, b:{A:[bA,sumb],B:[bB,sumb],⋯⋯}, ⋯⋯},⋯⋯}
        在以上两个字典中集合{A,B,⋯⋯}代表搜索关键字集，集合{a,b,⋯⋯}代表文档集，{aA,aB,⋯⋯}代表文档包含关键字的个数，{suma,sumb,⋯⋯}代表文档对应的总词数。
        例如，在word_in_afile_stat中a:{A:[aA,suma],B:[aB,suma],⋯⋯}代表文档a中包含关键字A的词数为aA，包含关键字B的词数为aB⋯⋯，文件a的总词数为suma，若a没有关键词B，则字典中不包含B这个键名。
        在word_in_allfiles_stat中，代表共有n1个文档包含关键词A，n2个文档包含关键词B。

'''
'''
建立特征字典， 计算每个词文本的数量，在目录出现频率，在全部训练集中出现频率
'''
def Tf_Compute():
	document_processed = preprocess_concept.preprocess()
	computed_tf = comput_df.compute_num()
	
	word_in_afile={}   		#在一个文本中词频
	word_in_cate={}			#在目录中词频
	word_in_allfiles={}		#全部训练文本的词频
	word_weight_dict = {}	#词权重字典
	
	word_in_cate = computed_tf[1]
	word_in_allfiles = 	computed_tf[0]	
	files_num = len(document_processed)	#文本数量
	#结果保存到TF_result{}中			
	if (word_in_allfiles) and (files_num !=0):  
		TF_result={}  
		for word_FreqD,categories,path in document_processed:  
			TF_result[path]={}  
			for word in word_FreqD:  
				if word not in TF_result[path]:
					TF_result[path][word] = []
					TF_result[path][word].append(word_FreqD[word])
					TF_result[path][word].append(word_in_cate[categories][word])
					TF_result[path][word].append(word_in_allfiles[word])
	'''
		for word_FreqD,cate,path in document_processed:
			if cate not in cate_list:
				cate_list.append(cate)
	
	#for cate in cate_list:
	#构建词字典
	for word_FreqD,categories,path in document_processed:

		file_name = path.split('/')[1]
		
		for word in word_FreqD:
			#全部训练文本的词频
			if word not in word_in_allfiles:  
				word_in_allfiles[word]=1 
			else:  
				word_in_allfiles[word]+=1
			#在目录中词频
			if categories not in word_in_cate:
				word_in_cate[categories]={}
			if word not in word_in_cate[categories]:
				word_in_cate[categories][word]= 1
			else:
				word_in_cate[categories][word] += 1
	'''


	#print(word_in_cate)
		
	#print(word_weight_dict)
	return TF_result

#Tf_Compute()
					