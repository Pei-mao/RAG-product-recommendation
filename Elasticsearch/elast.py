from elasticsearch import Elasticsearch, helpers
import json
import pandas as pd
import numpy as np
import re

# 加載數據
file_path = 'SalePage.csv'
df = pd.read_csv(file_path)

# 替換 NaN 值為空字符串或其他默認值
df['SaleProductDescShortContent'] = df['SaleProductDescShortContent'].replace(np.nan, 'No description')
# 去除描述欄位裡面開頭的數字並去除換行符號
df['SaleProductDescShortContent'] = df['SaleProductDescShortContent'].apply(lambda x: re.sub(r'^\d+', '', x).strip().replace('\n', '').replace('\r', ''))


# 生成商品數據列表
products = []

for index, row in df.iterrows():
    product = {
        'name': row['SalePageTitle'],
        'description': row['SaleProductDescShortContent']
    }
    products.append(product)

#顯示生成的商品數據
for product in products[:10]:
    print(product)


# 連接到Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])


# 創建索引並添加商品數據
index_name = 'products'
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

actions = [
    {
        '_op_type': 'index',
        '_index': index_name,
        '_id': product['name'],
        '_source': product
    }
    for product in products
]

helpers.bulk(es, actions)
print("商品數據已成功索引到Elasticsearch中")
