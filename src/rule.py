from collections import defaultdict
import numpy as np
import math
import load

rmse_score = defaultdict(lambda:defaultdict(list))
mae_score = defaultdict(lambda:defaultdict(list))

for name in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
    for cross in range(5):
        if name == "ml-100k":
            train_set, test_set = load.load_ml_100k(random_seed=cross)
        elif name == "ml-1m":
            train_set, test_set = load.load_ml_1m(random_seed=cross)
        elif name == "ml-10m":
            train_set, test_set = load.load_ml_10m(random_seed=cross)
        elif name == "ml-20m":
            train_set, test_set = load.load_ml_20m(random_seed=cross)
        elif name == "netflix":
            train_set, test_set = load.load_netflix(random_seed=cross)

        global_rating = []
        user_rating = defaultdict(list)
        item_rating = defaultdict(list)

        for t in train_set:
            user_id, item_id, rating = t
            global_rating.append(rating)
            user_rating[user_id].append(rating)
            item_rating[item_id].append(rating)

        global_mean = np.array(global_rating).mean()

        user_mean = {}
        for user_id in user_rating:
            user_mean[user_id] = np.array(user_rating[user_id]).mean()

        item_mean = {}
        for item_id in item_rating:
            item_mean[item_id] = np.array(item_rating[item_id]).mean()

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
            
            global_rmse += (rating - global_mean) ** 2
            user_rmse += (rating - user_mean[user_id]) ** 2
            item_rmse += (rating - item_mean[item_id]) ** 2
            user_item_rmse += (rating - (user_mean[user_id] + item_mean[item_id])/2) ** 2
            
            global_mae += abs(rating - global_mean)
            user_mae += abs(rating - user_mean[user_id])
            item_mae += abs(rating - item_mean[item_id])
            user_item_mae += abs(rating - (user_mean[user_id] + item_mean[item_id])/2)

        cnt = len(test_set)
            
        global_rmse = math.sqrt(global_rmse / cnt)
        user_rmse = math.sqrt(user_rmse / cnt)
        item_rmse = math.sqrt(item_rmse / cnt)
        user_item_rmse = math.sqrt(user_item_rmse / cnt)

        global_mae = global_mae / cnt
        user_mae = user_mae / cnt
        item_mae = item_mae / cnt
        user_item_mae = user_item_mae / cnt

        rmse_score["global mean"][name].append(global_rmse)
        rmse_score["user mean"][name].append(user_rmse)
        rmse_score["item mean"][name].append(item_rmse)
        rmse_score["user item mean"][name].append(user_item_rmse)

        mae_score["global mean"][name].append(global_mae)
        mae_score["user mean"][name].append(user_mae)
        mae_score["item mean"][name].append(item_mae)
        mae_score["user item mean"][name].append(user_item_mae)

df = open("log/rule.log", "w")
df.write("### Rule-based Methods RMSE\n")
df.write("||ml-100k|ml-1m|ml-10m|ml-20m|netflix|\n")
df.write("|:-|-|-|-|-|-|\n")
for method in ["global mean", "user mean", "item mean", "user item mean"]:
    df.write("|%s|"%method)
    for name in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
        mean = np.mean(rmse_score[method][name])
        std = np.std(rmse_score[method][name])
        df.write("%.4f $\pm$ %.4f|"%(mean, std))
    df.write("\n")
df.write("\n")
df.write("### Rule-based Methods MAE\n")
df.write("||ml-100k|ml-1m|ml-10m|ml-20m|netflix|\n")
df.write("|:-|-|-|-|-|-|\n")
for method in ["global mean", "user mean", "item mean", "user item mean"]:
    df.write("|%s|"%method)
    for name in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
        mean = np.mean(mae_score[method][name])
        std = np.std(mae_score[method][name])
        df.write("%.4f $\pm$ %.4f|"%(mean, std))
    df.write("\n")
df.write("\n")
df.close()



