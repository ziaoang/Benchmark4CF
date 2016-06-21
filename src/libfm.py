import os
import sys
import load

tmp_path = "tmp_libfm"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
output_file = "%s/output.txt"%tmp_path

tool_path = "../tool/libfm-1.42.src"

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

    print(name)
    print("="*20)
    
    # als
    os.system("%s/bin/libFM -task r -train %s -test %s -out %s -method als -regular '0,0,10' -init_stdev 0.1"%(tool_path, train_file, test_file, output_file))

    # sgd
    os.system("%s/bin/libFM -task r -train %s -test %s -out %s -method sgd -learn_rate 0.01 -regular '0,0,0.01' -init_stdev 0.1"%(tool_path, train_file, test_file, output_file))

    # mcmc
    os.system("%s/bin/libFM -task r -train %s -test %s -out %s -method mcmc -init_stdev 0.1"%(tool_path, train_file, test_file, output_file))

os.system("rm -r %s"%tmp_path)



