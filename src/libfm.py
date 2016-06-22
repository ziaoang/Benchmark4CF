import os
import sys
import load

method_list = ["libfm sgd", "libfm als", "libfm mcmc"]
dataset_list = ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]

tmp_path = "tmp_libfm"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
output_file = "%s/output.txt"%tmp_path

tool_path = "../tool/libfm-1.42.src"

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

        rmse_score["libfm sgd"][dataset].append(rmse)
        mae_score["libfm sgd"][dataset].append(mae)

        os.system("%s -method als -regular '0,0,10' -init_stdev 0.1"%basic_head)

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
        
        rmse_score["libfm als"][dataset].append(rmse)
        mae_score["libfm als"][dataset].append(mae)

        os.system("%s -method mcmc -init_stdev 0.1"%basic_head)

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
        
        rmse_score["libfm mcmc"][dataset].append(rmse)
        mae_score["libfm mcmc"][dataset].append(mae)


df = open("log/libfm.log", "w")

df.write("### LibFM RMSE\n")
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

df.write("### LibFM MAE\n")
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

os.system("rm -r %s"%tmp_path)


