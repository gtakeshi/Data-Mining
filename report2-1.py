import numpy as np
from collections import OrderedDict

train = np.array([["m","b","t"],["m","s","t"],     #検証するには、授業で出たデータセットを利用
             ["g","q","t"],["h","s","t"],
             ["g","q","t"],["g","q","f"],
             ["g","s","f"],["h","b","f"],
             ["h","q","f"],["m","b","f"]])

test = np.array([["m","q"],["g","s"],        #テストデータセット
             ["g","q"],["h","s"],
             ["h","q"],["m","q"],  
             ["g","s"],["h","b"],
             ["h","q"],["m","b"]])
print("訓練データは:　\n"+ str(train))

probabilities = OrderedDict()                #確率を格納する順序付Dict
'''
ここで、訓練データとラベルを用いて、訓練をする
利用した計算式は Pr(A_i = a_i | C = c_j) = (A_i = a_i and class c_j)/(class c_j)
'''
def train_cal_probability(array,A="",C=""):      #訓練部属性ごとの確率を計算する（Ex. Pr(A=m|C=t)など）
    itemindex = numpy.argwhere(array[...,2] == C)    
    #print(itemindex)                #指定したCの数を確認､検証用コード
    counter = 0
    if A:   #AかBは渡されたか
        for index in itemindex[...,0]:            #まずCの値が一致する部分の位置をitemindexを格納する(Ex. C=tなら 0から4行)
            if A in array[index,...]:
                counter += 1                       #それに､もしitemindexに格納された行にAかBが存在すれば､個数counter加算
            AdC = counter/sum(array[...,2] == C) 
        if A in ["m","g","h"]:                             #Aのmかgかhかが入力した時
            #print("A="+A+" "+"C="+C+" : "+str(AdC))     #検証用
            probabilities[str("A="+A+",C="+C)]=AdC 
        else:                                            #Bが入力した時
            #print("B="+A+" "+"C="+C+" : "+str(AdC))     #検証用
            probabilities[str("B="+A+",C="+C)]=AdC
    else:                             #渡されないと､Pr(C=)を計算
        AdC =  sum(array[...,2] == C)/ len(array[...,2])     #Cだけの時
        #print("C="+C+" : "+str(AdC))                   #検証用
        probabilities[str("C="+C)]=AdC
        
def check_train_proba(probas):              #検証用  訓練後算出した確率
    print("\n訓練後:")        
    for pro in probabilities.items():
        print(pro)     
        
def test_function(proba,a,b):
    print("テストデータ: A="+a+" B="+b)
    PrCt = round(proba["C=t"]*proba["A="+a+",C=t"]*proba["B="+b+",C=t"],3)
    PrCf = round(proba["C=f"]*proba["A="+a+",C=f"]*proba["B="+b+",C=f"],3)
    print("予測: C="+("t" if PrCt > PrCf else "f"))
    
for attrs in ["m","g","h","b","s","q",""]:            #上のcal_probability関数でそれぞれの確率を計算し､Probabilitiesに入れ
    for labels in ["t","f"]:
        train_cal_probability(train,A=attrs,C=labels)       # 訓練をする
        
check_train_proba(probabilities)
print("\nテスト:")  
for index in range(len(test[...,0])):
    test_function(probabilities,test[index,0],test[index,1])


