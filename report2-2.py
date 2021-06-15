import matplotlib.pyplot as plt
from math import sqrt 
import sys
import numpy as np
import json
import random
from collections import OrderedDict

dataset = []
seeds = []
oldseeds = []
circus = True         #繰り返しのスイッチ

try:
    with open("dataset.json") as json_obj:        #事前に別のプログラムで生成したデータセットをインポート
        dataset = np.array(json.load(json_obj)).tolist()           #Datasetに一列目はレベル(クラスター)デフォルトは0
        
except:
    print("No such file")
    sys.exit()
    
#print("Dataset:\n","ラベル----X----Y\n"+str(dataset))          #検証用

k = int(input("Please enter the number of k.\"quit\" for QUIT"))     #K-meansのKを入れる

if k == "quit":
    sys.exit()
print("You chose %s-means" % k)
        
def get_seeds(data,k):           #Seedをランダムに選択される関数
    for index in range(0,k):
        #print(index)                 #検証用
        seed = random.choice(dataset)    #データセットからランダムにK個データを取り出して、SEEDとする
        seed[0] = index         #SEEDのインデックス
        seeds.append(seed)
        print("SEED{} IS: ".format(index+1)+str(seed))
        
def k_means(dataset,seeds):         #K-meansの関数
    for data in dataset:
        dists = []        #距離を格納するlist
        for seed in seeds:        #個々のデータとSEEDの距離を計算し、distsに格納する、最小距離のインデックスは、データの新しいクラスターにする
            dist = sqrt(((seed[1] - data[1]) ** 2)+((seed[2] - data[2])) ** 2)  #距離計算式
            dists.append(dist)
            data[0] = dists.index(min(dists))
#           print(dists.index(min(dists)))      #検証用
#           print(dists)       #検証用

def randomcolor():         #ランダムに点の色を決める関数
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color
            
def get_middle_point(dataset,seeds,k):         #中央点を計算する関数 
    middles = []
    middle = []
    for index in range(0,k):
        sums = [0,0]
        nums = 0
        for data in dataset:     #中央点を計算する
            if data[0] == index :
                nums += 1
                sums[0] = round((sums[0] + data[1]),3)
                sums[1] = round((sums[1] + data[2]),3)
                #print(sums,nums)    #検証用
        middle = [index,round(sums[0]/nums,3),round(sums[1]/nums,3)]
#       print("直後のMiddle "+str(middle))      #検証用
#       print(middle)               ＃検証用
        middles.append(middle)
    
    #print(middles)    #検証用       
    return middles

def plot_point(dataset,k):      #点の図を出力する
    for data in dataset:
        plt.xlim(0.0, 1.6) 
        plt.ylim(0.0, 1.6) 
        plt.scatter(data[1],data[2],c=color[int(data[0])],edgecolors="none",s=80)
    plt.show()
    
    
color = []                #ランダムに色を選択
for colorindex in range(k):
    color.append(randomcolor())    
    
get_seeds(dataset,k)      #一回目にSEEDを選択
i = 0 #第i回
while circus:     #二回目以降、Middle（中央点）を探す
    i += 1
    oldseeds = seeds[:]    #プログラム終了のインジケーター 
    k_means(dataset,seeds)
    print("第{}回クラスタリングとそのSEED（Middle）".format(i))
    plot_point(dataset,k)    #図の出力
    plot_point(seeds,k)      #図の出力
    plt.show()
    seeds = get_middle_point(dataset,seeds,k)   
    if oldseeds == seeds:       #もしすべての中央点が変わらなくなったら、プログラム終了
        break
#     print(seeds)      #検証用  
# print(dataset)            #検証用
