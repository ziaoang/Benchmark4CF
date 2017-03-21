from collections import defaultdict
import numpy as np
import math
import os
from load import load

tmp_path = "tmp_libfm"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
output_file = "%s/output.txt"%tmp_path

tool_path = "../tool/libfm-1.42.src"

df = open("log/libfm.log", "w")
#for dataset in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
for dataset in ["jester"]:
    for cross in range(5):
        train_set, test_set = load(dataset, random_seed=cross)

        basic_pool = {}
        basic_index = 0

        train_df = open(train_file, 'w')
        for t in train_set:
            user_id, item_id, rating = t
            user_id = "u" + str(user_id)
            item_id = "v" + str(item_id)
            if user_id not in basic_pool:
                basic_pool[user_id] = basic_index
                basic_index += 1
            if item_id not in basic_pool:
                basic_pool[item_id] = basic_index
                basic_index += 1
            user_index = basic_pool[user_id]
            item_index = basic_pool[item_id]
            train_df.write("%.1f %d:1 %d:1\n"%(rating, user_index, item_index))
        train_df.close()

        test_df = open(test_file, "w")
        for t in test_set:
            user_id, item_id, rating = t
            user_id = "u" + str(user_id)
            item_id = "v" + str(item_id)
            user_index = basic_pool[user_id]
            item_index = basic_pool[item_id]
            test_df.write("%.1f %d:1 %d:1\n"%(rating, user_index, item_index))
        test_df.close()
    
        basic_head = "%s/bin/libFM -task r -train %s -test %s -out %s"%(tool_path, train_file, test_file, output_file)

        os.system("%s -method sgd -learn_rate 0.01 -regular '0,0,0.01' -init_stdev 0.1"%basic_head)
        rmse, mae, cnt = 0.0, 0.0, 0
        for line in open(output_file):
            cnt += 1
            rating = test_set[cnt-1][2]
            predict = float(line.strip())
            rmse += (rating - predict) ** 2
            mae += abs(rating - predict)
        rmse = math.sqrt(rmse / cnt)
        mae = mae / cnt
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("libfm sgd", dataset, cross+1, rmse, mae))

        os.system("%s -method als -regular '0,0,10' -init_stdev 0.1"%basic_head)
        rmse, mae, cnt = 0.0, 0.0, 0
        for line in open(output_file):
            cnt += 1
            rating = test_set[cnt-1][2]
            predict = float(line.strip())
            rmse += (rating - predict) ** 2
            mae += abs(rating - predict)
        rmse = math.sqrt(rmse / cnt)
        mae = mae / cnt
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("libfm als", dataset, cross+1, rmse, mae))
        
        os.system("%s -method mcmc -init_stdev 0.1"%basic_head)
        rmse, mae, cnt = 0.0, 0.0, 0
        for line in open(output_file):
            cnt += 1
            rating = test_set[cnt-1][2]
            predict = float(line.strip())
            rmse += (rating - predict) ** 2
            mae += abs(rating - predict)
        rmse = math.sqrt(rmse / cnt)
        mae = mae / cnt
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("libfm mcmc", dataset, cross+1, rmse, mae))

df.close()

os.system("rm -r %s"%tmp_path)



