import os
import sys
import load

tmp_path = "tmp_libmf"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
model_file = "%s/model.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
output_file = "%s/output.txt"%tmp_path

tool_path = "../tool/libmf-2.01"

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

    train_df = open(train_file, "w")
    for entry in train_set:
        train_df.write("%d %d %.1f\n"%(entry[0], entry[1], entry[2]))
    train_df.close()

    test_df = open(test_file, "w")
    for entry in test_set:
        test_df.write("%d %d %.1f\n"%(entry[0], entry[1], entry[2]))
    test_df.close()

    print(name)
    print("="*20)
    
    os.system("%s/mf-train -k 10 -t 1000 %s %s"%(tool_path, train_file, model_file))
    os.system("%s/mf-predict %s %s %s"%(tool_path, test_file, model_file, output_file))

os.system("rm -r %s"%tmp_path)



