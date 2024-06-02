from elasticsearch import Elasticsearch

# 連接到Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])


# 獲取所有索引的列表
indices = es.cat.indices(format='json')
for index in indices:
    index_name = index['index']
    print(f"Index: {index_name}")

    # 獲取索引的映射
    mapping = es.indices.get_mapping(index=index_name)
    print(f"Mapping for {index_name}:")
    print(mapping)

    # 獲取索引中的前20個文檔
    response = es.search(index=index_name, body={"query": {"match_all": {}}, "size": 100})
    print(f"Documents in {index_name}:")
    for hit in response['hits']['hits']:
        print(hit['_source'])
    print("-" * 80)