### RAG-product-recommendation
Use OpenAI API to connect to Elasticsearch search engine, and then recommend users.

### Purpose
Allow users to input their questions on the front end, search the database based on the users' questions, and respond with suitable products for the users.

## Preparation
Install exe [Elasticsearch](https://www.elastic.co/cn/elasticsearch)
Install python package: pip install flask

## Code description
Elasticsearch/elast.py:  
Read SalePage.csv and input the product names and product descriptions into Elasticsearch.
Elasticsearch/elastSh.py:  
Query what values are in Elasticsearch.
Elasticsearch/elashDel.py:  
Delete all products in Elasticsearch.

Produce_html/generate_products_html.py:  
Generate the front-end homepage, search button, and product page.
Produce_html/SalePage.7z:  
It contains product data. Please unzip it and use the password to unlock.

Frontend_Backend/api_key.txt:  
Store the OpenAI API key, please use your own.
Frontend_Backend/app.py:  
Use a Flask-written backend to connect to Elasticsearch, send the values returned by Elasticsearch to the OpenAI API for GPT-4, and finally send the values returned by GPT-4 to index.html.
Frontend_Backend/index.html:  
Front-end homepage
Frontend_Backend/products.html:  
Product page