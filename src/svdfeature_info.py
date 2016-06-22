import os
import sys
import random

tmp_path = "tmp_svdfeature_info"

if not os.path.isdir(tmp_path):
    os.system("mkdir %s"%tmp_path)

train_file = "%s/train.txt"%tmp_path
test_file = "%s/test.txt"%tmp_path
train_buffer_file = "%s/train.buffer"%tmp_path
test_buffer_file = "%s/test.buffer"%tmp_path
conf_file = "%s/conf.txt"%tmp_path

tool_path = "../tool/svdfeature-1.2.2"

user_id_user_index = {}
item_id_item_index = {}
global_user_index = 0
global_item_index = 0
data_set = []
for line in open("../data/ml-1m/ratings.dat"):
    user_id, item_id, rating, timestamp = line.strip().split("::")
    if user_id not in user_id_user_index:
        user_id_user_index[user_id] = global_user_index
        global_user_index += 1
    if item_id not in item_id_item_index:
        item_id_item_index[item_id] = global_item_index
        global_item_index += 1
    user_index = user_id_user_index[user_id]
    item_index = item_id_item_index[item_id]
    data_set.append([user_index, item_index, float(rating)])

random.seed(123456789)
random.shuffle(data_set)

split_ratio = 0.9

train_set = []
user_set = set()
item_set = set()
for t in data_set[:int(len(data_set) * split_ratio)]:
    user_index, item_index, rating = t 
    train_set.append(t)
    user_set.add(user_index)
    item_set.add(item_index)
    
test_set = []
for t in data_set[int(len(data_set) * split_ratio):]:
    user_index, item_index, rating = t 
    if user_index in user_set and item_index in item_set:
        test_set.append(t)

def get_gender_vector(gender):
    gender_vector = [0] * 2
    if gender == "M":
        gender_vector[0] = 1
    elif gender == "F":
        gender_vector[1] = 1
    return gender_vector

def get_age_vector(age):
    age_vector = [0] * 7
    if age == "1":
        age_vector[0] = 1
    elif age == "18":
        age_vector[1] = 1
    elif age == "25":
        age_vector[2] = 1
    elif age == "35":
        age_vector[3] = 1
    elif age == "45":
        age_vector[4] = 1
    elif age == "50":
        age_vector[5] = 1
    elif age == "56":
        age_vector[6] = 1
    return age_vector

def get_occupation_vector(occupation):
    occupation_vector = [0] * 21
    occupation_vector[int(occupation)] = 1
    return occupation_vector

user_info = {}
for line in open("../data/ml-1m/users.dat"): # 2 + 7 + 21 = 30
    user_id, gender, age, occupation, zip_code = line.strip().split("::")
    if user_id in user_id_user_index:
        user_index = user_id_user_index[user_id]
        user_info[user_index] = get_gender_vector(gender) + get_age_vector(age) + get_occupation_vector(occupation)

def get_year_vector(year):
    year_list = [1919, 1920, 1921, 1922, 1923, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
    index = {}
    for i in range(len(year_list)):
        index[year_list[i]] = i
    year_vector = [0] * len(year_list)
    year_vector[index[year]] = 1
    return year_vector

def get_genres_vector(genres):
    genre_list = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
    index = {}
    for i in range(len(genre_list)):
        index[genre_list[i]] = i
    genres_vector = [0] * len(genre_list)
    for genre in genres.split("|"):
        genres_vector[index[genre]] = 1
    return genres_vector

item_info = {}
for line in open("../data/ml-1m/movies.dat"): # 81 + 18 = 99
    item_id, title, genres = line.strip().split("::")
    if item_id in item_id_item_index:
        item_index = item_id_item_index[item_id]
        year = int(title[-5:-1])
        item_info[item_index] = get_year_vector(year) + get_genres_vector(genres)

max_user_index = 0
max_item_index = 0
rating_sum = 0
rating_cnt = 0
for t in train_set:
    user_id, item_id, rating = t
    max_user_index = max(max_user_index, user_id)
    max_item_index = max(max_item_index, item_id)
    rating_sum += rating
    rating_cnt += 1

conf_df = open(conf_file, 'w')
conf_df.write("base_score = %.4f\n"%(rating_sum/rating_cnt))
conf_df.write("num_global = 0\n")
conf_df.write("num_user = %d\n"%(max_user_index+30+1))
conf_df.write("num_item = %d\n"%(max_item_index+99+1))
conf_df.write("active_type = 0\n")
conf_df.write("num_factor = 100\n")
conf_df.write("learning_rate = 0.005\n")
conf_df.write("wd_user = 0.04\n")
conf_df.write("wd_item = 0.04\n")
conf_df.close()

train_df = open(train_file, 'w')
for t in train_set:
    user_id, item_id, rating = t
    user_vector = user_info[user_id]
    item_vector = item_info[item_id]
    user_count = 1
    item_count = 1
    user_str = "%d:1"%user_id
    item_str = "%d:1"%item_id
    for i in range(30):
        if user_vector[i] == 1:
            user_count += 1
            user_str += " %d:1"%(max_user_index + i + 1)
    for i in range(99):
        if item_vector[i] == 1:
            item_count += 1
            item_str += " %d:1"%(max_item_index + i + 1)
    train_df.write("%.1f 0 %d %d %s %s\n"%(rating, user_count, item_count, user_str, item_str))
train_df.close()

test_df = open(test_file, 'w')
for t in test_set:
    user_id, item_id, rating = t
    user_vector = user_info[user_id]
    item_vector = item_info[item_id]
    user_count = 1
    item_count = 1
    user_str = "%d:1"%user_id
    item_str = "%d:1"%item_id
    for i in range(30):
        if user_vector[i] == 1:
            user_count += 1
            user_str += " %d:1"%(max_user_index + i + 1)
    for i in range(99):
        if item_vector[i] == 1:
            item_count += 1
            item_str += " %d:1"%(max_item_index + i + 1)
    test_df.write("%.1f 0 %d %d %s %s\n"%(rating, user_count, item_count, user_str, item_str))
test_df.close()

print("ml-1m")
print("="*20)

os.system("%s/tools/make_feature_buffer %s %s"%(tool_path, train_file, train_buffer_file))
os.system("%s/tools/make_feature_buffer %s %s"%(tool_path, test_file, test_buffer_file))

os.system("%s/svd_feature %s buffer_feature=%s test:buffer_feature=%s model_out_folder=%s num_round=100"%(tool_path, conf_file, train_buffer_file, test_buffer_file, tmp_path))
os.system("%s/svd_feature_infer %s buffer_feature=%s test:buffer_feature=%s model_out_folder=%s"%(tool_path, conf_file, train_buffer_file, test_buffer_file, tmp_path))

os.system("rm -r %s"%tmp_path)



