from collections import defaultdict
import numpy as np
import math
import os
import load

dataset_list = ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]

tmp_path = "tmp_libmf"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
model_file = "%s/model.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
output_file = "%s/output.txt"%tmp_path

tool_path = "../tool/libmf-2.01"

rmse_score = defaultdict(list)
mae_score = defaultdict(list)

for dataset in dataset_list:
    for cross in range(5):
        if dataset == "ml-100k":
            train_set, test_set = load.load_ml_100k(random_seed=cross)
        elif dataset == "ml-1m":
            train_set, test_set = load.load_ml_1m(random_seed=cross)
        elif dataset == "ml-10m":
            train_set, test_set = load.load_ml_10m(random_seed=cross)
        elif dataset == "ml-20m":
            train_set, test_set = load.load_ml_20m(random_seed=cross)
        elif dataset == "netflix":
            train_set, test_set = load.load_netflix(random_seed=cross)

        train_df = open(train_file, "w")
        for entry in train_set:
            train_df.write("%d %d %.1f\n"%(entry[0], entry[1], entry[2]))
        train_df.close()

        test_df = open(test_file, "w")
        for entry in test_set:
            test_df.write("%d %d %.1f\n"%(entry[0], entry[1], entry[2]))
        test_df.close()
        
        os.system("%s/mf-train -k 10 -t 100 %s %s"%(tool_path, train_file, model_file))
        os.system("%s/mf-predict %s %s %s"%(tool_path, test_file, model_file, output_file))

        rmse = 0
        mae = 0
        cnt = 0
        for line in open(output_file):
            cnt += 1
            rating = test_set[cnt-1][2]
            predict = float(line.strip())
            rmse += (rating - truth) ** 2
            mae += abs(rating - truth)
        rmse = math.sqrt(rmse / cnt)
        mae = mae / cnt

        rmse_score[dataset].append(rmse)
        mae_score[dataset].append(mae)


df = open("log/libmf.log", "w")

df.write("### LibMF RMSE\n")
df.write("||%s|\n"%("|".join(dataset_list)))
df.write("|:-|-|-|-|-|-|\n")
df.write("|libmf|")
for dataset in dataset_list:
    mean = np.mean(rmse_score[dataset])
    std = np.std(rmse_score[dataset])
    df.write("%.4f $\pm$ %.4f|"%(mean, std))
df.write("\n\n")

df.write("### LibMF MAE\n")
df.write("||%s|\n"%("|".join(dataset_list)))
df.write("|:-|-|-|-|-|-|\n")
df.write("|libmf|")
for dataset in dataset_list:
    mean = np.mean(mae_score[dataset])
    std = np.std(mae_score[dataset])
    df.write("%.4f $\pm$ %.4f|"%(mean, std))
df.write("\n\n")
df.close()

os.system("rm -r %s"%tmp_path)


