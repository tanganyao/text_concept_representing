from __future__ import division
import math
import tf_iwfiwf

'''
规范化文本的概念向量空间
目前还是特征向量空间的规范
'''

def regular():

	file_guiyi = []
	file_guiyi_temp = 0
	sum = 0
	TF_result = tf_iwfiwf.Tf_Compute()
	
	#求出归一因子，并且保存到file_guiyi[]中
	for file in TF_result.keys():
		sum = 0
		for word in TF_result[file].keys():
			if TF_result[file][word]:
				sum += math.pow(TF_result[file][word], 2)
		file_guiyi_temp = math.pow(sum, 0.5)			
		#file_guiyi.append(file_guiyi_temp)
		for word in TF_result[file]:
			if file_guiyi_temp:
				TF_result[file][word] /= file_guiyi_temp
			
	print(TF_result)
	

regular()