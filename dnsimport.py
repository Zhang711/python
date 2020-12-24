#!/usr/bin/env python3

import pandas as pd
import xlrd
import os

df = pd.read_excel(r"D:\DEV.xlsx", usecols=[1, 3], names=None)
df_li = df.values.tolist()

for i in df_li:

    # 将 DNS 用 "." 分隔
    x = i[0].split(".")

    try:
        cmd = "etcdctl put /coredns/{}/{}/{}/{} '{{\"host\":\"{}\",\"ttl\":10}}'".format(x[3], x[2], x[1], x[0], i[1])
        print(cmd)
        #    os.system(cmd)
    except IndexError:
        cmd = "etcdctl put /coredns/{}/{}/{} '{{\"host\":\"{}\",\"ttl\":10}}'".format(x[2], x[1], x[0], i[1])
        print(cmd)
        #    os.system(cmd)