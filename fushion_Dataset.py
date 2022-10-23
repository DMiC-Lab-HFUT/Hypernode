from collections import Counter
"""\

参数A,B,C的取值范围是[5%,10%,15%,20%,25%,30%]
总行310116 对应值为15505 31011 46517 62023 77529 93034
"""
"""
三、直接融合数据集
（1）遍历FB15K-237、FB15K-237-1、FB15K-237-2、FB15K-237-3、FB15K-237-4的每一行进行比较，因为我们只替换了尾实体，并且按行替换，所以进行逐行比对即可；尾实体不一致的取多数投票，票数一样的随机取一个保留，将三元组写到新的文件中如fusion.txt，三元组数量应该和FB15K-237等单独的数据集一样的。
（2）遍历fusion.txt的头尾实体和关系，得到entities.dict和relations.dict。
"""
import random
#步骤1 融合
def fushion():
    fb15k=[]
    for line in open("D:\python_code\Hypernode\FB15k-237\FB15k-237.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k.append(fb)
    fb15k1=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-1\FB15k-237-1.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k1.append(fb)
    fb15k2=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-2\FB15k-237-2.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k2.append(fb)
    fb15k3=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-3\FB15k-237-3.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k3.append(fb)
    fb15k4=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-4\FB15k-237-4.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k4.append(fb)
    print(len(fb15k))
    print(len(fb15k1))
    print(len(fb15k2))
    print(len(fb15k3))
    print(len(fb15k4))
    f = open("D:\python_code\Hypernode\\fushion\\fushion.txt", "a")
    for i in range(0,310116):
        list_num=[fb15k[i][2],fb15k1[i][2],fb15k2[i][2],fb15k3[i][2],fb15k4[i][2]]
        tail=find_max(list_num)
        f.write(fb15k[i][0]+"\t"+fb15k[i][1]+"\t"+tail+"\n")
# 找到出现次数最多的尾实体
def find_max(list_max):
    res=Counter(list_max)
    return res.most_common(1)[0][0]
#步骤3 提取三元组的头尾实体 关系
def extract():
    #获取entities.dict
    fb15k_head_tail=[]
    for line in open("D:\python_code\Hypernode\\fushion\\fushion.txt"):
        head=line.split("\t")[0]
        tail=line.split("\t")[2].split("\n")[0]
        fb15k_head_tail.append(head)
        fb15k_head_tail.append(tail)
    fb15k_head_tail=list(set(fb15k_head_tail))
    f=open("D:\python_code\Hypernode\\fushion\\entities.dict","a")
    num=0
    for i in fb15k_head_tail:
        f.write(str(num)+"\t"+i+"\n")
        num=num+1
    #获取relations.dict
    fb15k_relation=[]
    for line in open("D:\python_code\Hypernode\\fushion\\fushion.txt"):
        relation = line.split("\t")[1]
        fb15k_relation.append(relation)
    fb15k_relation=list(set(fb15k_relation))
    f=open("D:\python_code\Hypernode\\fushion\\relations.dict","a")
    num1=0
    for i in fb15k_relation:
        f.write(str(num1)+"\t"+i+"\n")
        num1=num1+1
if __name__ == '__main__':
    # fushion()
    extract()