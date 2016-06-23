from collections import defaultdict
import numpy as np

rmse_dict = defaultdict(lambda:defaultdict(list))
mae_dict = defaultdict(lambda:defaultdict(list))
for filename in ["rule", "libmf", "libfm"]:
    for line in open("src/log/%s.log"%filename):
        method, dataset, cross, rmse, mae = line.strip().split("\t")
        rmse_dict[method][dataset].append(float(rmse))
        mae_dict[method][dataset].append(float(mae))

method_list = ["global mean", "user mean", "item mean", "user item mean", "libmf", "libfm sgd", "libfm als", "libfm mcmc"]
dataset_list = ["ml-100k", "ml-1m", "ml-10m"]

out = ""
out += "# Benchmark4CF\n"

out += "## RMSE\n"
out += "|-|%s|\n"%("|".join(dataset_list))
out += "|:-|%s|\n"%("|".join([":-:" for d in dataset_list ]))
for method in method_list:
    out += "|%s|"%method
    for dataset in dataset_list:
        mean = np.mean(rmse_dict[method][dataset])
        std = np.std(rmse_dict[method][dataset])
        out += "%.4f $\pm$ %.4f|"%(mean, std)
    out += "\n"

out += "## MAE\n"
out += "|-|%s|\n"%("|".join(dataset_list))
out += "|:-|%s|\n"%("|".join([":-:" for d in dataset_list ]))
for method in method_list:
    out += "|%s|"%method
    for dataset in dataset_list:
        mean = np.mean(mae_dict[method][dataset])
        std = np.std(mae_dict[method][dataset])
        out += "%.4f $\pm$ %.4f|"%(mean, std)
    out += "\n"

df = open("README.md", "w")
df.write(out)
df.close()



