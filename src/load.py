import random

def load(dataset_name, random_seed=123456789):
    if dataset_name == "ml-100k":
        return load_ml_100k(random_seed=random_seed)
    elif dataset_name == "ml-1m":
        return load_ml_1m(random_seed=random_seed)
    elif dataset_name == "ml-10m":
        return load_ml_10m(random_seed=random_seed)
    elif dataset_name == "ml-20m":
        return load_ml_20m(random_seed=random_seed)
    elif dataset_name == "netflix":
        return load_netflix(random_seed=random_seed)

def load_ml_100k(folder_path="../data/ml-100k", split_ratio=0.9, random_seed=123456789):
    data_set = []
    for line in open(folder_path+"/u.data"):
        user_id, item_id, rating, timestamp = line.strip().split("\t")
        data_set.append([user_id, item_id, rating])
    return process(data_set, split_ratio, random_seed)

def load_ml_1m(folder_path="../data/ml-1m", split_ratio=0.9, random_seed=123456789):
    data_set = []
    for line in open(folder_path+"/ratings.dat"):
        user_id, item_id, rating, timestamp = line.strip().split("::")
        data_set.append([user_id, item_id, rating])
    return process(data_set, split_ratio, random_seed)

def load_ml_10m(folder_path="../data/ml-10M100K", split_ratio=0.9, random_seed=123456789):
    data_set = []
    for line in open(folder_path+"/ratings.dat"):
        user_id, item_id, rating, timestamp = line.strip().split("::")
        data_set.append([user_id, item_id, rating])
    return process(data_set, split_ratio, random_seed)

def load_ml_20m(folder_path="../data/ml-20m", split_ratio=0.9, random_seed=123456789):
    data_set = []
    line_no = 0
    for line in open(folder_path+"/ratings.csv"):
        line_no += 1
        if line_no == 1:
            continue
        user_id, item_id, rating, timestamp = line.strip().split(",")
        data_set.append([user_id, item_id, rating])
    return process(data_set, split_ratio, random_seed)

def load_netflix(folder_path="../data/download", split_ratio=0.9, random_seed=123456789):
    data_set = []
    for item_id in range(17770):
        line_no = 0
        for line in open(folder_path+"/training_set/mv_%07d.txt"%(item_id+1)):
            line_no += 1
            if line_no == 1:
                continue
            user_id, rating, date = line.strip().split(",")
            data_set.append([user_id, str(item_id), rating])
    return process(data_set, split_ratio, random_seed)

def process(data_set, split_ratio, random_seed):
    # map data
    user_id_user_index = {}
    item_id_item_index = {}
    global_user_index = 0
    global_item_index = 0
    map_data_set = []
    for t in data_set:
        user_id, item_id, rating = t
        if user_id not in user_id_user_index:
            user_id_user_index[user_id] = global_user_index
            global_user_index += 1
        if item_id not in item_id_item_index:
            item_id_item_index[item_id] = global_item_index
            global_item_index += 1
        user_index = user_id_user_index[user_id]
        item_index = item_id_item_index[item_id]
        map_data_set.append([user_index, item_index, float(rating)])
    # shuffle data
    random.seed(random_seed)
    random.shuffle(map_data_set)
    # load train set
    train_set = []
    user_set = set()
    item_set = set()
    for t in map_data_set[:int(len(map_data_set) * split_ratio)]:
        user_index, item_index, rating = t
        train_set.append(t)
        user_set.add(user_index)
        item_set.add(item_index)
    # load test set
    test_set = []
    for t in map_data_set[int(len(map_data_set) * split_ratio):]:
        user_index, item_index, rating = t
        if user_index in user_set and item_index in item_set:
            test_set.append(t)
    return train_set, test_set



