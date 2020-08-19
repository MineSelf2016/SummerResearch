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

2. 矩阵降维



#### 文本聚类

在将文本内容表示成数学上可分析处理的形式后，接下来的工作就是在此数学形式的基础上，对文本进行聚类处理。文本聚类主要有 2 种方法：基于概率 [6] 和基于距离 [7] 。基于概率的方法以贝叶斯概率理论为基础，用概率的分布方式描述聚类结果。基于距离的方法，就是以特征向量表示文档，将文档看成向量空间中的一个点，通过计算点之间的距离进行聚类。 

目前，基于距离的文本聚类比较成熟的方法大致可以分为 2 种类型：层次凝聚法和平面划分法。

对于给定的文件集合 D ={d1 , d 2 ,…,di ,…, dn } ，层次凝聚法的具体过程如下：

(1) 将 D 中的每个文件 di 看成一个具有单个成员的簇 ci ={di } ，这些簇构成了 D 的一个聚类 C={c1 ,c2 ,…,ci ,…,cn };

(2) 计算 C 中每对簇 (ci ,cj ) 之间的相似度 sim{ ci ,cj } ；

(3) 选取具有最大相似度的簇对 (ci ,cj ) 将 ci 和 cj 合并为一个新的簇 ck =sim ci ∪ cj ，从而构成了 D 的一个新的聚类 C =(c1 , c 2 ,…,cn-1 );

(4) 重复上述步骤，直至 C 中剩下一个簇为止。该过程构造出一棵生成树，其中包含了簇的层次信息以及所有簇内和簇间的相似度。


对于给定的文件集合 {} D ={d1 , d2 ,…,di ,…, dn } ，平面划分法的具体过程如下：

(1) 确定要生成簇的数目 k ；

(2) 按照某种原则生成 k 个聚类中心作为聚类的种子 S=(s1 ,s2 ,…,si ,…,sk );

(3) 对 D 中的每个文件 di ，依次计算它与各个种子 sj 的相似度 sim (di ,sj );
 
(4) 选取具有最大相似度的种子 ，将 di 归入以 sj 为聚类中心的簇 cj ，从而得到 D 的一个聚类 C ={ci ,cj }

(5) 重复此步骤若干次，以得到较为稳定的聚类结果。这 2 种类型各有优缺点。层次凝聚法能够生成层次化的嵌套簇，准确度较高。但在每次合并时，需要全局地比较所有簇之间的相似度，并选出最佳的 2 个簇，因此执行速度较慢，不适合大量文件的集合。而平面划分法相对来说速度较快，但是必须事先确定 k 的取值，且种子选取的好坏对群集结果有较大影响。


2. K-means 聚类


3. VSM 模型


4. Word2Vec 模型 

artifical 分析

sklearn 文本聚类

LDA 文本聚类

## 时序分析

对日期进行自定义排序

```python
def sortedDateValues(date_blog):
    keys = date_blog.keys()
    keys = sorted(keys, key = functools.cmp_to_key(order_rule))
    return [(key, date_blog[key]) for key in keys]

```

### 微博列表数据分析

1. 数据量统计

<table border=0 cellpadding=0 cellspacing=0 width=435 style='border-collapse:
 collapse;table-layout:fixed;width:325pt'>
 <col width=87 span=5 style='width:65pt'>
 <tr height=21 style='height:16.0pt'>
  <td height=21 width=87 style='height:16.0pt;width:65pt'></td>
  <td width=87 style='width:65pt'>forward</td>
  <td width=87 style='width:65pt'>comment</td>
  <td width=87 style='width:65pt'>like</td>
  <td width=87 style='width:65pt'>timeStamp</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 style='height:16.0pt'>count</td>
  <td align=right>7885</td>
  <td align=right>7885</td>
  <td align=right>7885</td>
  <td align=right>7885</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 style='height:16.0pt'>mean</td>
  <td align=right>9901.74534</td>
  <td align=right>3354.8577</td>
  <td align=right>52072.6529</td>
  <td align=right>1584050466</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 style='height:16.0pt'>std</td>
  <td align=right>262006.829</td>
  <td align=right>10707.3467</td>
  <td align=right>166692.254</td>
  <td align=right>3511551.7</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 style='height:16.0pt'>min</td>
  <td align=right>42</td>
  <td align=right>47</td>
  <td align=right>392</td>
  <td align=right>1577840100</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 class=xl63 align=right style='height:16.0pt'>25%</td>
  <td align=right>353</td>
  <td align=right>522</td>
  <td align=right>4091</td>
  <td align=right>1580912880</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 class=xl63 align=right style='height:16.0pt'>50%</td>
  <td align=right>736</td>
  <td align=right>1045</td>
  <td align=right>9422</td>
  <td align=right>1583843280</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 class=xl63 align=right style='height:16.0pt'>75%</td>
  <td align=right>1856</td>
  <td align=right>2554</td>
  <td align=right>30038</td>
  <td align=right>1586784960</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 style='height:16.0pt'>max</td>
  <td align=right>15460810</td>
  <td align=right>339350</td>
  <td align=right>3070305</td>
  <td align=right>1590940440</td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
  <td width=87 style='width:65pt'></td>
 </tr>
 <![endif]>
</table>


结论：
总体来看，like $\gt$ comment $\approx$ forward，forward 数据的75%分位数以上的部分过大，存在异常值，导致平均值相应增大。

根据单sigma 原则，筛选出少量微博（17条）存在转发量远大于评论量与点赞量的微博：
```python
df[df["forward"] > 9901 + 262006].count()
# count: 17
```
去掉过多的数量后，forward 回归正常，这17条微博存在有意转发的现象。
```python
df[df["forward"] > 1856 + 262006]["forward"].sum()
# 异常值sum：54839705.0，占比 70%

int(int(int(7885 * 9901.75) - 54839705) / (7885 - 17))
# 去掉异常值后的forward 转发量平均值：2953，远低于之前的9901
```

明星效应的影响：与明星相关，微博含有明星名字的微博转发量超过平均值非常多。是否存在“虚假账户”（水军）（阴兵）？
```python
celebrity_forward_num = 808452 + 1352428 + 1128548 + 961410 + 1110738 + 1134405 + 1236141
# celebrity_forward_num = 7732122
celebrity_effect = 7732122 /(78069385 -(54839705.0 - 7732122))
#明星效应影响celebrity_effect = 24.97%
```


作图分析，like，comment，forward 的分布状况



2. 微博话题的饼状图



3. 肺炎相关信息所占比重



4. 肺炎相关信息的关键词（武汉）



5. 微博话题变化趋势图


1. 微博发布量（日、周、月）





### 微博评论数据分析


