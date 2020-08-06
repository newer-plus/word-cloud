# coding: utf-8
import jieba
import re
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from imageio import imread

text = []
nickname = ['xx', 'xx'] #去掉昵称
stopwords = ['我', '我们', '你', '你们', '了', '不', '动画',
             '表情', '图片', '[', ']', '，', '？', 'smile']   #去掉停用词，可自己扩展
pattern = re.compile('|'.join(nickname))

with open('109', 'r', encoding='utf-8') as f: #加载聊天内容
    for line in f.readlines():
        line = line.strip()
        if re.findall(pattern, line):
            continue
        seglist = jieba.cut(line)
        for word in seglist:
            if word not in stopwords:
                text.append(word)

len(text)

curdir = os.getcwd()

font_path = curdir + '/fonts/SourceHanSerif/SourceHanSerifK-Light.otf' #设置字体
back_coloring = imread('little prince.png') #背景图片

wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
               max_font_size=100, random_state=42, width=1000, height=860, margin=2, )

wc.generate(' '.join(text))

image_colors_byImg = ImageColorGenerator(back_coloring)
# show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
plt.axis("off")
plt.figure()
# plt.imshow(back_coloring, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file('109.jpeg')
