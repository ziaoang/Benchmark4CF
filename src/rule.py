from collections import defaultdict
from load import load
import numpy as np
import math

df = open("log/rule.log", "w")
#for dataset in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
for dataset in ["jester"]:
    for cross in range(5):
        train_set, test_set = load(dataset, random_seed=cross)

        global_rating = []
        user_rating = defaultdict(list)
        item_rating = defaultdict(list)

        for t in train_set:
            user_id, item_id, rating = t
            global_rating.append(rating)
            user_rating[user_id].append(rating)
            item_rating[item_id].append(rating)

        global_mean = np.mean(global_rating)
        user_mean = { user_id : np.mean(user_rating[user_id]) for user_id in user_rating }
        item_mean = { item_id : np.mean(item_rating[item_id]) for item_id in item_rating }
        
        global_rmse, user_rmse, item_rmse, user_item_rmse = 0.0, 0.0, 0.0, 0.0
        global_mae, user_mae, item_mae, user_item_mae = 0.0, 0.0, 0.0, 0.0
    
        for t in test_set:
            user_id, item_id, rating = t
            u_mean, i_mean = user_mean[user_id], item_mean[item_id]
            global_rmse    += (rating - global_mean) ** 2
            user_rmse      += (rating - u_mean) ** 2
            item_rmse      += (rating - i_mean) ** 2
            user_item_rmse += (rating - (u_mean + i_mean)/2) ** 2
            global_mae     += abs(rating - global_mean)
            user_mae       += abs(rating - u_mean)
            item_mae       += abs(rating - i_mean)
            user_item_mae  += abs(rating - (u_mean + i_mean)/2)

        cnt = len(test_set)
        global_rmse    = math.sqrt(global_rmse / cnt)
        user_rmse      = math.sqrt(user_rmse / cnt)
        item_rmse      = math.sqrt(item_rmse / cnt)
        user_item_rmse = math.sqrt(user_item_rmse / cnt)

        global_mae     = global_mae / cnt
        user_mae       = user_mae / cnt
        item_mae       = item_mae / cnt
        user_item_mae  = user_item_mae / cnt

        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("global mean", dataset, cross+1, global_rmse, global_mae))
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("user mean", dataset, cross+1, user_rmse, user_mae))
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("item mean", dataset, cross+1, item_rmse, item_mae))
        df.write("%s\t%s\t%d\t%.4f\t%.4f\n"%("user item mean", dataset, cross+1, user_item_rmse, user_item_mae))
df.close()



