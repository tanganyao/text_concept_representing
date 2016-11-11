import preprocess_concept

def compute_num():
	
	document_processed = preprocess_concept.preprocess()
	word_in_allfiles={}		#全部训练文本的词频
	word_in_cate={}			#在目录中词频
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
	#print(word_in_cate)
	return [word_in_allfiles, word_in_cate]
#compute_num()