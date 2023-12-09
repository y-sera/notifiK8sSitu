#!/usr/bin/python3
import requests

# 一旦URLべた書き
# kubectl proxy使用中に実行
res = requests.get('http://127.0.0.1:8001/api/v1/namespaces')
namespaces = res.json()["items"]

for ns in namespaces:
    print(ns["metadata"]["name"])
print('----')
print('namespaces: ',len(namespaces))


