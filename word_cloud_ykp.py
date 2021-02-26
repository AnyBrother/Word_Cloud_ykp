# -*- coding: utf-8 -*-
"""
@Time    : 2021/02/26 13:30
@Software: PyCharm
@Author  : ykp
Version  : 提取文本txt中关键词, 剔除异常字词, 生成对应形状的图片.
"""
import os
import numpy as np
import pandas as pd
import datetime
from PIL import Image
from matplotlib import pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator


def word_cloud_ykp(path, text_in_name, figure_in_name, text_out_name, figure_out_name,
                   stopwords_text_name, max_words_num, words_stat_name):
    """
    # Extract keywords from text TXT, remove abnormal words, and generate images of corresponding shapes.
    Input:
        path: Python file location.
        text_in_name: Input original text filename.
        figure_in_name: Input original figure filename.
        text_out_name: Output cleaned text filename.
        figure_out_name: Output word cloud figure filename.
        stopwords_text_name: Input stopwords text filename.
        max_words_num: Maximized number of key words in word cloud.
        words_stat_name: Output word stat excel filename.
    Output:
        "yyyy.dd.mm.text_out_name.txt"
        "yyyy.dd.mm.figure_out_name.png"
        "yyyy.dd.mm.words_stat_name.xlsx"
    """
    # 记录时间
    now_time1 = datetime.datetime.now().strftime('%Y.%m.%d.%H')  # 记录当前的年、月、日、小时
    now_time2 = datetime.datetime.now().strftime('%M')  # 记录当前的分钟
    save_time = now_time1 + '：' + now_time2 + '.'
    path_out = save_time + "Output" + "\\"
    os.makedirs(path_out)

    def read_and_cut_words():
        # 对原文本分词
        text_in = open(path + text_in_name,  encoding='UTF-8-SIG').read()
        text_cut = jieba.cut(text_in, cut_all=False)
        content = ""
        for i in text_cut:
            content += i
            content += " "
        return content

    def load_stopwords():
        # 加载stopwords
        stopwords_load = [line.strip() for line in open(path + stopwords_text_name, encoding='utf-8').readlines()]
        # print(stopwords)
        return stopwords_load

    def move_stopwords(content, stopwords_all):
        # 去除原文stopwords,并生成去除stopwords的新文本
        content_after = ''
        for word in content:
            if word not in stopwords_all:
                if word != '\t' and '\n':
                    content_after += word
        content_after = content_after.replace("   ", " ").replace("  ", " ")
        # print(content_after)
        # 写入去停止词后生成的新文本
        with open(path_out + save_time + text_out_name, 'w', encoding='UTF-8-SIG') as f:
            f.write(content_after)
        return content_after
    # 设置中文停止词
    stopwords = set(load_stopwords())  # 载入的网络下载的停止词
    stopwords.update(
        ['但是', '一个', '自己', '因此', '没有', '很多', '可以', '这个', '虽然', '因为', '这样', '已经', '现在', '一些', '比如', '不是', '当然', '可能',
         '如果', '就是', '同时', '比如', '这些', '必须', '由于', '而且', '并且', '他们',
         '字 治理', "社", "字", "面", "基", "济", "国", "监", "协", "家 治理", "中", "家",
         "成", "化", "全", "化 转型", "作", "重", "正", "样", "通", "代", "次", "新",
         "加", "体", "素", "超", "首", "治", "造", "理"])  # 人工更新的停止词
    # 读取清洁版的文本信息
    content_clean = move_stopwords(read_and_cut_words(), stopwords)  # 读取原始文本,进行分词并剔除停止词
    # content_clean = open(path + text_out_name, encoding='UTF-8-SIG').read()
    content_clean += ' '.join(jieba.cut(content_clean, cut_all=False))  # cut_all=False表示采用精确模式
    # 设置中文字体
    font_path = "C:\\Windows\\Fonts\\simhei.ttf"  # 思源黑体
    # 读取背景图片
    image_in = np.array(Image.open(os.path.join(path + figure_in_name)))
    # 提取背景图片颜色
    img_colors = ImageColorGenerator(image_in)
    # 设置词云参数
    wc = WordCloud(
        font_path=font_path,  # 中文需设置路径
        margin=2,  # 页面边缘
        mask=image_in,
        scale=2,
        max_words=max_words_num,  # 最多词个数
        min_font_size=5,  # 最小字体大小
        stopwords=stopwords,  # 停止词
        random_state=42,  # 随机种子
        background_color='white',  # 背景颜色
        # background_color = '#C3481A', # 背景颜色
        max_font_size=200,  # 最大字体大小
    )
    wc.generate(content_clean)
    # 获取文本词排序，可调整stopwords
    process_word = WordCloud.process_text(wc, content_clean)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
    # print(sort[:max_words_num])  # 获取文本词频最高的前max_words_num个词
    # 输出excel
    pd.DataFrame(sort).to_excel(path_out + save_time + words_stat_name)
    # 设置为背景色，若不想要背景图片颜色，就注释掉
    wc.recolor(color_func=img_colors)
    # 存储图像
    wc.to_file(path_out + save_time + figure_out_name)
    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    path = os.getcwd()+"\\"  # Python file location.
    text_in_name = '01.TextIn_BigData.txt'  # Input original text filename.
    figure_in_name = 'github_brand.png'  # Input original figure filename.
    text_out_name = "01.TextIn_BigData(Clean).txt"  # Output cleaned text filename.
    figure_out_name = "词云图.png"  # Output word cloud figure filename.
    stopwords_text_name = "00.Stopwords.2018.12.14.txt"  # Input stopwords text filename.
    max_words_num = 200  # Maximized number of key words in word cloud.
    words_stat_name = "词云统计表.xlsx"  # Output word stat excel filename.
    word_cloud_ykp(path, text_in_name, figure_in_name,
                   text_out_name, figure_out_name,
                   stopwords_text_name, max_words_num, words_stat_name)


if __name__ == "__main__":
    import warnings
    warnings.filterwarnings('ignore')
    main()
