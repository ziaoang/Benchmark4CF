from collections import defaultdict
import numpy as np
import math
import load

for name in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
    if name == "ml-100k":
        train_set, test_set = load.load_ml_100k()
    elif name == "ml-1m":
        train_set, test_set = load.load_ml_1m()
    elif name == "ml-10m":
        train_set, test_set = load.load_ml_10m()
    elif name == "ml-20m":
        train_set, test_set = load.load_ml_20m()
    elif name == "netflix":
        train_set, test_set = load.load_netflix()

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
    
    for t in test_set:
        user_id, item_id, rating = t

        global_rmse += (rating - global_mean) ** 2

        user_rmse += (rating - user_mean[user_id]) ** 2
    
        item_rmse += (rating - item_mean[item_id]) ** 2

        user_item_rmse += (rating - (user_mean[user_id] + item_mean[item_id])/2) ** 2

    cnt = len(test_set)    
    global_rmse = math.sqrt(global_rmse / cnt)
    user_rmse = math.sqrt(user_rmse / cnt)
    item_rmse = math.sqrt(item_rmse / cnt)
    user_item_rmse = math.sqrt(user_item_rmse / cnt)

    print("%s"%name)
    print("="*20)
    
    print("global mean: %.4f"%global_rmse)
    print("user mean: %.4f"%user_rmse)
    print("item mean: %.4f"%item_rmse)
    print("user item mean: %.4f"%user_item_rmse)



