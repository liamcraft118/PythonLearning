# -*- coding: utf-8 -*-

from DB import DB
from wordcloud import WordCloud
import jieba

# class WordCloud(object):

if __name__ == '__main__':
    db = DB()
    db.connect()
    result = db.readAllTitle()

    titles = ''
    for title in result:
        titles += title[0]

    words = " ".join(jieba.cut(titles))
    wordcloud = WordCloud(font_path="simsun.ttf").generate(words)

    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
