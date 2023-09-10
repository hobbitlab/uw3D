import json
import os
pwd = os.getcwd()
def getPwd(s):
    return pwd + s[1:]

def process(a):
    for d in a["train"]:
        d["image"] = getPwd(d["image"])
        d["mask"] = getPwd(d["mask"])
        d["mask_multiclass"] = getPwd(d["mask_multiclass"])
    for d in a["val"]:
        d["image"] = getPwd(d["image"])
        d["mask"] = getPwd(d["mask"])
        d["mask_multiclass"] = getPwd(d["mask_multiclass"])

