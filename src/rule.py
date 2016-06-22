from collections import defaultdict
import numpy as np
import math
import load

method_list = ["global mean", "user mean", "item mean", "user item mean"]
dataset_list = ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]

rmse_score = defaultdict(lambda:defaultdict(list))
mae_score = defaultdict(lambda:defaultdict(list))

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

        global_rating_sum = 0.0
        global_rating_cnt = 0
        user_rating_sum = defaultdict(float)
        user_rating_cnt = defaultdict(int)
        item_rating_sum = defaultdict(float)
        item_rating_cnt = defaultdict(int)

        for t in train_set:
            user_id, item_id, rating = t
            global_rating_sum += rating
            global_rating_cnt += 1
            user_rating_sum[user_id] += rating
            user_rating_cnt[user_id] += 1
            item_rating_sum[item_id] += rating
            item_rating_cnt[item_id] += 1

        global_mean = global_rating_sum / global_rating_cnt

        global_rmse = 0.0
        user_rmse = 0.0
        item_rmse = 0.0
        user_item_rmse = 0.0
        
        global_mae = 0.0
        user_mae = 0.0
        item_mae = 0.0
        user_item_mae = 0.0
    
        for t in test_set:
            user_id, item_id, rating = t
            
            user_mean = user_rating_sum[user_id] / user_rating_cnt[user_id]
            item_mean = item_rating_sum[item_id] / item_rating_cnt[item_id]

            global_rmse += (rating - global_mean) ** 2
            user_rmse += (rating - user_mean) ** 2
            item_rmse += (rating - item_mean) ** 2
            user_item_rmse += (rating - (user_mean + item_mean)/2) ** 2
            
            global_mae += abs(rating - global_mean)
            user_mae += abs(rating - user_mean)
            item_mae += abs(rating - item_mean)
            user_item_mae += abs(rating - (user_mean + item_mean)/2)

        cnt = len(test_set)
            
        global_rmse = math.sqrt(global_rmse / cnt)
        user_rmse = math.sqrt(user_rmse / cnt)
        item_rmse = math.sqrt(item_rmse / cnt)
        user_item_rmse = math.sqrt(user_item_rmse / cnt)

        global_mae = global_mae / cnt
        user_mae = user_mae / cnt
        item_mae = item_mae / cnt
        user_item_mae = user_item_mae / cnt

        rmse_score["global mean"][dataset].append(global_rmse)
        rmse_score["user mean"][dataset].append(user_rmse)
        rmse_score["item mean"][dataset].append(item_rmse)
        rmse_score["user item mean"][dataset].append(user_item_rmse)

        mae_score["global mean"][dataset].append(global_mae)
        mae_score["user mean"][dataset].append(user_mae)
        mae_score["item mean"][dataset].append(item_mae)
        mae_score["user item mean"][dataset].append(user_item_mae)


df = open("log/rule.log", "w")

df.write("### Rule-based Methods RMSE\n")
df.write("||%s|\n"%("|".join(dataset_list)))
df.write("|:-|-|-|-|-|-|\n")
for method in method_list:
    df.write("|%s|"%method)
    for dataset in dataset_list:
        mean = np.mean(rmse_score[method][dataset])
        std = np.std(rmse_score[method][dataset])
        df.write("%.4f $\pm$ %.4f|"%(mean, std))
    df.write("\n")
df.write("\n")

df.write("### Rule-based Methods MAE\n")
df.write("||%s|\n"%("|".join(dataset_list)))
df.write("|:-|-|-|-|-|-|\n")
for method in method_list:
    df.write("|%s|"%method)
    for dataset in dataset_list:
        mean = np.mean(mae_score[method][dataset])
        std = np.std(mae_score[method][dataset])
        df.write("%.4f $\pm$ %.4f|"%(mean, std))
    df.write("\n")
df.write("\n")

df.close()


