from flask import Flask, request, jsonify
from flask_cors import CORS
from elasticsearch import Elasticsearch
from openai import OpenAI

# 初始化 Flask 應用
app = Flask(__name__)
CORS(app)  # 設置 CORS 以允許所有來源的請求

# 設置 Elasticsearch 連接
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# 從文件中讀取 OpenAI API 密鑰
with open('api_key.txt', 'r') as file:
    openai_api_key = file.read().strip()
    
@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    print(query)
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    # 從 Elasticsearch 檢索數據
    response = es.search(
        index='products',
        body={
            'query': {
                'multi_match': {
                    'query': query,
                    'fields': ['name', 'description']
                }
            },
            'size': 5  # 控制檢索商品的數量
        }
    )
    print("response: ", response)
    products = [hit['_source'] for hit in response['hits']['hits']]
    context = ', '.join([f"{product['name']}: {product['description']}" for product in products])
    print("query: ", query)
    print("context: ", context)
    # 呼叫 GPT-4 API 生成回答
    client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a company product salesman."},
            {"role": "user", "content": f"{query}, Help me choose two of these product and don't change the original product name.| {context}"}
        ],
        model="gpt-4o",
        max_tokens=200
    )
    print("chat_completion: ", chat_completion)
    answer = chat_completion.choices[0].message.content.strip()
    print("answer: ", answer)
    print("products: ", products)

    return jsonify({'answer': answer, 'products': products})

if __name__ == '__main__':
    app.run(debug=True, port=30000)  # 指定端口 30000
