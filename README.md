# Word_Cloud_ykp
**(In English)** Extract keywords from text TXT, remove abnormal words, and generate images of corresponding shapes.

**(In Chinese)** 提取文本txt中关键词, 剔除异常字词, 生成对应形状的图片.

# File Preparation
- **stopwords txt file**, eg: "00.Stopwords.2018.12.14.txt".
- **text in txt file**, eg: "01.TextIn_BigData.txt".
- **picture you want to shaped into**, recommend 'black_white' picture, eg: "github_brand.png".

# Paramaters setup in "word_cloud_ykp.py"
Only need to change code *From line 123 to 130* as below. Then run is ok and output files are all in *yyyy.mm.dd.hh：minutes.Output* file.
```python
path = os.getcwd()+"\\"  # Python file location.
text_in_name = '01.TextIn_BigData.txt'  # Input original text filename.
figure_in_name = 'github_brand.png'  # Input original figure filename.
text_out_name = "01.TextIn_BigData(Clean).txt"  # Output cleaned text filename.
figure_out_name = "词云图.png"  # Output word cloud figure filename.
stopwords_text_name = "00.Stopwords.2018.12.14.txt"  # Input stopwords text filename.
max_words_num = 200  # Maximized number of key words in word cloud.
words_stat_name = "词云统计表.xlsx"  # Output word stat excel filename.
```
