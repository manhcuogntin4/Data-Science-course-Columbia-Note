# -*- coding: utf-8 -*-
import collections
FILE_NAME="98-0.txt"
STOP_FILE="stopwords"
def read_file_text(file_name):
	dict={}
	punctuation=[",", ".", "", "\"","“"]
	with open(file_name) as f:
		for content in f:
			#print content
			#Remove punctation
			for i in punctuation:
				content.replace(i," ")
				words=content.split(" ")
			for i in words:
				#print i
				if i.strip().lower() in dict and i!="":
					dict[i.strip().lower()]+=1
				else:
				 	dict[i.strip().lower()]=1
	return dict
def read_file_stop_word(file_name):
	stop_list=[]
	with open(file_name) as f:
		for content in f:
			stop_list.append(content.strip())
	return stop_list

file_name=FILE_NAME
stop_file=STOP_FILE
dict=read_file_text(file_name)
stop_list=read_file_stop_word(stop_file)
#print stop_list
most_count=sorted(dict.items(), key=lambda x: x[1])
dict_with_stop_word={}
for key, value in dict.items():
	if key not in stop_list:
		dict_with_stop_word[key]=value
#dict_with_stop_word=[i for i in dict and dict[i] not in stop_list]
print most_count[-11:]
#print dict
most_count_stop=sorted(dict_with_stop_word.items(), key=lambda x: x[1])
print most_count_stop[-11:]
print "\xe2\x80\x9ci"