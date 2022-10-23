from collections import Counter
"""

参数A,B,C的取值范围是[5%,10%,15%,20%,25%,30%]
总行310116 对应值为15505 31011 46517 62023 77529 93034
"""
"""
四、sameas处理a
	（实体破坏）每个数据源实体表示并不一致，需要进行实体对齐
（1）对刚刚上一步得到的FB15K-237-1文件的entities.dict选取5%（C）的实体进行实体随机编码处理，注意随机的编码不重复，譬如可以叫FB0000，将被（替换的原实体id  sameas 随机编码id）写到sameas.txt文件中；
（2）将随机编码id替换掉FB15K-237-1文件三元组文件中的对应的id；
（3）以上FB15K-237-1、FB15K-237-2、FB15K-237-3、FB15K-237-4四份文件重复操作；
（5）操作完成后将FB15K-237、FB15K-237-1、FB15K-237-2、FB15K-237-3、FB15K-237-4五份文件的三元组文件放到一个txt文件中，遍历三元组的头尾实体和关系，得到entities.dict和relations.dict。
于是我们会得到（五份文件在一起的）entities.dict和relations.dict，triples.txt和sameas.txt。

"""
import random
#步骤1 生成sameas
def sameas():
    ran = random.sample(range(0, 14533), 726)
    ran1=sorted(ran)
    fb15k=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-1\entities.dict"):
        fb=[]
        head=line.split("\t")[0]
        tail=line.split("\t")[1].split("\n")[0]
        fb.append(head)
        fb.append(tail)
        fb15k.append(fb)
    print(fb15k)
    f = open("D:\python_code\Hypernode\FB15k-237-1\sameas.txt", "a")
    for i in ran1:
        tail=get_pin()
        tail="/m/"+tail
        f.write(fb15k[i][1]+"\t"+"sameas"+"\t"+tail+"\n")
        fb15k[i][1]=tail
#生成随机6位编码
def get_pin():
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
              'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    total_set = number + letter

    value_set = "".join(random.sample(total_set, 6))

    return value_set


#步骤2 将随机编码id替换掉FB15K-237-1文件三元组文件中的对应的id
def replace_Sameas():
    fb15k=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-1\FB15k-237-1.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k.append(fb)
    sameas=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-1\sameas.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(tail)
        sameas.append(fb)
    #遍历，替换
    for i in fb15k:
        for j in sameas:
            if i[0]==j[0]:
                i[0] = j[1]
            if i[2] == j[0]:
                i[2] = j[1]
    f=open("D:\python_code\Hypernode\FB15k-237-1\FB15k-237-1-new.txt","a")
    for i in fb15k:
        f.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\n")
#步骤3 提取三元组的头尾实体 关系
def extract():
    #获取entities.dict
    fb15k_head_tail=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-4\FB15k-237-4.txt"):
        head=line.split("\t")[0]
        tail=line.split("\t")[2].split("\n")[0]
        fb15k_head_tail.append(head)
        fb15k_head_tail.append(tail)
    fb15k_head_tail=list(set(fb15k_head_tail))
    f=open("D:\python_code\Hypernode\FB15k-237-4\entities.dict","a")
    num=0
    for i in fb15k_head_tail:
        f.write(str(num)+"\t"+i+"\n")
        num=num+1
    #获取relations.dict
    fb15k_relation=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-4\FB15k-237-4.txt"):
        relation = line.split("\t")[1]
        fb15k_relation.append(relation)
    fb15k_relation=list(set(fb15k_relation))
    f=open("D:\python_code\Hypernode\FB15k-237-4\\relations.dict","a")
    num1=0
    for i in fb15k_relation:
        f.write(str(num1)+"\t"+i+"\n")
        num1=num1+1
if __name__ == '__main__':
    replace_Sameas()