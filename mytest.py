import json
data_json_dir = "/Users/shukai/Downloads/3d/dataset_3d_fold_0.json"
with open(data_json_dir, "r") as f:
    data_json = json.load(f)
    print(data_json)