import os
from load import load

tmp_path = "tmp_svdfeature"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
train_buffer_file = "%s/train.buffer"%tmp_path
test_buffer_file = "%s/test.buffer"%tmp_path
conf_file = "%s/conf.txt"%tmp_path

tool_path = "../tool/svdfeature-1.2.2"

#for dataset in ["ml-100k", "ml-1m", "ml-10m", "ml-20m", "netflix"]:
for dataset in ["ml-1m"]:
    train_set, test_set = load(dataset)

    max_user_index = 0
    max_item_index = 0
    rating_sum = 0
    rating_cnt = 0

    train_df = open(train_file, 'w')
    for t in train_set:
        user_id, item_id, rating = t
        max_user_index = max(max_user_index, user_id)
        max_item_index = max(max_item_index, item_id)
        rating_sum += rating
        rating_cnt += 1
        train_df.write("%.1f 0 1 1 %d:1 %d:1\n"%(rating, user_id, item_id))
    train_df.close()

    conf_df = open(conf_file, 'w')
    conf_df.write("base_score = %.4f\n"%(rating_sum/rating_cnt))
    conf_df.write("num_global = 0\n")
    conf_df.write("num_user = %d\n"%(max_user_index+1))
    conf_df.write("num_item = %d\n"%(max_item_index+1))
    conf_df.write("active_type = 0\n")
    conf_df.write("num_factor = 100\n")
    conf_df.write("learning_rate = 0.005\n")
    conf_df.write("wd_user = 0.04\n")
    conf_df.write("wd_item = 0.04\n")
    conf_df.close()

    test_df = open(test_file, 'w')
    for t in test_set:
        user_id, item_id, rating = t
        test_df.write("%.1f 0 1 1 %d:1 %d:1\n"%(rating, user_id, item_id))
    test_df.close()

    os.system("%s/tools/make_feature_buffer %s %s"%(tool_path, train_file, train_buffer_file))
    os.system("%s/tools/make_feature_buffer %s %s"%(tool_path, test_file, test_buffer_file))

    os.system("%s/svd_feature %s buffer_feature=%s test:buffer_feature=%s model_out_folder=%s num_round=100"%(tool_path, conf_file, train_buffer_file, test_buffer_file, tmp_path))
    os.system("%s/svd_feature_infer %s buffer_feature=%s test:buffer_feature=%s model_out_folder=%s"%(tool_path, conf_file, train_buffer_file, test_buffer_file, tmp_path))

os.system("rm -r %s"%tmp_path)



