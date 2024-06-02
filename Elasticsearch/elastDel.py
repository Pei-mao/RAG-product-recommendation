from elasticsearch import Elasticsearch

# 連接到 Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# 指定索引名稱
index_name = 'products'

# 刪除索引（如果存在）
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
    print(f"Index '{index_name}' has been deleted.")

# 創建索引
es.indices.create(index=index_name)
print(f"Index '{index_name}' has been created.")
