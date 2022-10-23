"""\
参数A,B,C的取值范围是[5%,10%,15%,20%,25%,30%]
总行310116 对应值为15505 31011 46517 62023 77529 93034
"""
"""
破坏数据集处理
（1）对FB15K-237进行20%（A）的三元组随机替换，即将那20%（A）的三元组的尾实体任意替换为其他三元组的尾实体id，得到FB15K-237-1；对FB15K-237-1进行随机替换10%(B)，得到FB15K-237-2。
（2）再对FB15K-237进行20%的随机替换，得到FB15K-237-3；对FB15K-237-3随机替换10%得到FB15K-237-4；
（3）遍历几个替换完的三元组的头尾实体和关系，得到entities.dict和relations.dict。
（4）得到四份随机破坏的数据集FB15K-237-1、FB15K-237-2、FB15K-237-3、FB15K-237-4，里面分别包含triples.txt和entities.dict和relations.dict。
"""
import random
#步骤1 步骤2 按比例随机替换尾实体
def randomReplace():
    ran = random.sample(range(0, 310116), 31011)
    ran1=sorted(ran)
    fb15k=[]
    for line in open("D:\python_code\Hypernode\FB15k-237-3\FB15k-237-3.txt"):
        fb=[]
        head=line.split("\t")[0]
        relation=line.split("\t")[1]
        tail=line.split("\t")[2].split("\n")[0]
        fb.append(head)
        fb.append(relation)
        fb.append(tail)
        fb15k.append(fb)
    for i in ran1:
        replace=random.sample(range(0, 310116), 1)[0]
        fb15k[i][2]=fb15k[replace][2]
    f=open("D:\python_code\Hypernode\FB15k-237-4\FB15k-237-4.txt","a")
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
    randomReplace()
    # extract()
