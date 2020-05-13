#-*- coding:utf-8 -*-
from konlpy.tag import Okt
from collections import Counter

def get_tags(text, ntags=50):
    okt = Okt()
    nouns = okt.nouns(text)
    count = Counter(nouns)
    noun_count_list = []  # 빈도수를 저장하는 변수

    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        noun_count_list.append(temp)

    return noun_count_list

input_file_name = "tagdata.txt"
noun_count = 100 # 빈도수에 따른 키워드 결과값 최대 100개
output_file_name = "keyword.txt"
open_text_file = open(input_file_name, 'r', -1, "utf-8")
text = open_text_file.read()
tags = get_tags(text, noun_count)
open_text_file.close()
open_output_file = open(output_file_name, 'w', -1, "utf-8")

for tag in tags:
    noun = tag['tag']
    count = tag['count']
    open_output_file.write('{} {}\n'.format(noun, count))

open_output_file.close()


