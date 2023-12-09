#!/usr/bin/python3
import requests
import json
import os

# 一旦URLべた書き
# kubectl proxy使用中に実行
res = requests.get('http://127.0.0.1:8001/api/v1/namespaces')
namespaces = res.json()["items"]

notice_text = 'namespaces: ' + str(len(namespaces)) + '\n'
notice_text += '------' + '\n'
print('namespaces: ',len(namespaces))
print('----')

for ns in namespaces:
    print(ns["metadata"]["name"])
    notice_text += ns["metadata"]["name"] + '\n'



webHookUrl = os.environ['SLACK_WEBHOOK_URL']
requests.post(webHookUrl, data = json.dumps({
  'text': notice_text,
  'username': u'namespace count'
}))
