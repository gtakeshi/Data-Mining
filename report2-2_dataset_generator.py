import random
import matplotlib.pyplot as plt
import json
import math
import datetime 

dataset = []

for i in range(0,101):
    random.seed(datetime.datetime.now())
    dataset.append([0,round(random.uniform(0.1,1.5),2),round(random.uniform(0.1,1.5),2)])
for data in dataset:
    plt.scatter(data[1],data[2],c="blue",s=40)
    
plt.show()
with open("dataset.json","w") as json_obj:
    json.dump(dataset,json_obj)
    
