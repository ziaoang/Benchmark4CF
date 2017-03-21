from collections import defaultdict
import numpy as np
import math
import os
from load import load

tmp_path = "tmp_libmf"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
model_file = "%s/model.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
output_file = "%s/output.txt"%tmp_path

tool_path = "../tool/libmf-2.01"

df = open("log/libmf.log", "w")
#for dataset in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
for dataset in ["jester"]:
    for cross in range(5):
        train_set, test_set = load(dataset, random_seed=cross)

        train_df = open(train_file, "w")
        for t in train_set:
            train_df.write("%d %d %.1f\n"%(t[0], t[1], t[2]))
        train_df.close()

        test_df = open(test_file, "w")
        for t in test_set:
            test_df.write("%d %d %.1f\n"%(t[0], t[1], t[2]))
        test_df.close()
        
        os.system("%s/mf-train -k 10 -t 100 %s %s"%(tool_path, train_file, model_file))
        os.system("%s/mf-predict %s %s %s"%(tool_path, test_file, model_file, output_file))

        rmse, mae, cnt =0.0, 0.0, 0
        for line in open(output_file):
            cnt += 1
            rating = test_set[cnt-1][2]
            predict = float(line.strip())
            rmse += (rating - predict) ** 2
            mae += abs(rating - predict)
        rmse = math.sqrt(rmse / cnt)
        mae = mae / cnt
        
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("libmf", dataset, cross+1, rmse, mae))
df.close()

os.system("rm -r %s"%tmp_path)



