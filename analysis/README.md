# 微博数据分析

## 数据预处理

从数据集中提取与COVID-19 相关的微博数据

思路：分词后做文本分类与聚类

1. 使用 词袋（Bag of Words, BoW）模型计算词频
2. 使用 tf-idf 进行权重修正，再进行标准化，得到文本特征向量

词袋模型处理步骤：分词（tokenizing），统计修订词特征值（counting）与标准化（normalizing）。

### 构建语料库步骤

1. 除去数据中的非文本部分

2. 处理中文编码问题

```python

def is_zh(Chinese):
    return ('\u4e00' <= Chinese <= '\u9fa5')

```

3. 中文分词

使用现有工具完成文本分词。

简单的英文分词不需要任何工具，通过空格和标点符号进行分词，进一步的英文分词使用nltk。

对于中文分词，使用结巴分词（jieba）。

4. 引入停用词

/utility/stoplist.txt

### 聚类分析

#### 文本分类过程
<img src = "https://img-blog.csdnimg.cn/20181218160433769.png" title = "文本分类过程图"></img>

#### 文本表示
常用方法：布尔模型、向量空间模型（VSM）、隐（潜）语义模型（LSA）、概率模型



1. tf-idf 权重矩阵

使用scikit-learn 库计算tf-idf 矩阵，完成文本向量化。
sklearn 库计算时加入了平滑处理并进行了归一化Normalization，采用的是0-1 标准化

tf-idf 结果为(7885, 31730) 的稀疏矩阵，7885篇微博文档，31730个特征词，以稀疏矩阵的方式存储在 numpy.float64 类型的 Compressed Sparse Row 中

2. K-means 聚类


3. VSM 模型


4. Word2Vec 模型 

artifical 分析


