from __future__ import division
import math
import preprocess_concept

'''
word_in_allfiles_stat{A:n1,B:n2,⋯⋯}
word_in_afile_stat{a:{A:[aA,suma],B:[aB,suma],⋯⋯}, ⋯⋯}, b:{A:[bA,sumb],B:[bB,sumb],⋯⋯}, ⋯⋯},⋯⋯}
        在以上两个字典中集合{A,B,⋯⋯}代表搜索关键字集，集合{a,b,⋯⋯}代表文档集，{aA,aB,⋯⋯}代表文档包含关键字的个数，{suma,sumb,⋯⋯}代表文档对应的总词数。
        例如，在word_in_afile_stat中a:{A:[aA,suma],B:[aB,suma],⋯⋯}代表文档a中包含关键字A的词数为aA，包含关键字B的词数为aB⋯⋯，文件a的总词数为suma，若a没有关键词B，则字典中不包含B这个键名。
        在word_in_allfiles_stat中，代表共有n1个文档包含关键词A，n2个文档包含关键词B。
'''

def Tf_Compute():
	document_processed = preprocess_concept.preprocess()
	
	word_in_afile={}  
	word_in_cate={}
	word_in_allfiles={}
	files_num = len(document_processed)
	
	for word_FreqD,categories,path in document_processed:

		file_name = path.split('/')[1]
		
		for word in word_FreqD:
			if word not in word_in_allfiles:  
				word_in_allfiles[word]=1 
			else:  
				word_in_allfiles[word]+=1
			
			if categories not in word_in_cate:
				word_in_afile[categories]={} 
			if word not in word_in_cate[categories]:
				word_in_cate[categories][word]=1
			else:
				word_in_cate[categories][word] += 1
				
			if file_name not in word_in_afile:  
				word_in_afile[file_name]={}  
			if word not in word_in_afile:  
				word_in_afile[file_name][word]=[]  
				word_in_afile[file_name][word].append(word_FreqD[word])  
				word_in_afile[file_name][word].append(len(word_FreqD.items()))
				
	if (word_in_afile) and (word_in_allfiles) and (files_num !=0):  
		TF_result={}  
		for filename in word_in_afile.keys():  
			TF_result[filename]={}  
			for word in word_in_afile[filename].keys():  
				word_n=word_in_afile[filename][word][0]  
				word_sum=word_in_afile[filename][word][1]  
				with_word_sum=word_in_allfiles[word]  
				TF_result[filename][word]=(math.log(word_n + 1,2))*(math.log(files_num/with_word_sum))  				
				
	print(TF_result)
	return TF_result

Tf_Compute()
					