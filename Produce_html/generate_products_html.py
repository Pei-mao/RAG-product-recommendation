import pandas as pd


# 商品列表（去除重複值）
products = ['KAFEN卡氛極致旅行組60ml_3入', '【99好運轉不停】全方位維他命防護配方發泡錠10錠', '電影交換券', 'ECONECO資料夾',
          'AnimatoSHA無矽靈馬油昆布洗髮精700ml(新)', '精緻神祕好禮（芝麻活力膠囊乙包）', '全日營養肝精薑黃飲_食品_100mL',
          '日藥本舖週年購物袋', 'ZA仿真絲髮帶-贈品', '[99好運轉不停]DHC維他命C60粒_30日份', '舒特膚溫和潔膚乳250ml', 
          '日本獅王趣淨洗手慕斯250ml_清新果香', '【娘娘滿額贈】小黃瓜精華保濕化妝水', '全日營養肌美妍膠原蛋白飲_食品_100mL', 
          '【福利品】UnimatRiken愛貓關節保健營養粉100g', 'GATSBY指定款濕紙巾一包', '【春遊滿額贈】ECONECO海龍購物袋', 
          '野口研究EPA魚油膠囊45粒', '髮的料理米糠溫養豐盈洗髮精鮮花香350ml', 'KOSE光映透源治控油平衡面膜7入', 
          '精緻神祕好禮-保健（小兒利撒爾咀嚼式軟膠囊2粒裝）', '全日營養優和深海角鯊烯膠囊120粒', 'ECONECO驚喜包A（隨機贈品：購物袋或杯子）', 
          'Max柿涉去味速效頭皮淨化噴霧130ml', 'ECONECO厚手純水20抽濕紙巾', '髮的料理米糠溫養修護護髮素鮮果香350g', 
          '日藥本舖十週年ECONECO紀念購物袋', 'Farcent香水衣物香氛袋-贈品', 'BOTANiful本格自然派入浴鹽280g甜美草本', 
          '日藥本舖U虎元普醫療用口罩10入', 'ECONECO白雪魔法三層連續抽取式花紋衛生紙', 'Kose毛穴小町毛孔緊緻面膜7入', 
          '精緻神祕好禮-身體臉部保養（隨機面膜乙片）', '【滿件贈】万田酵素Mforte保養體驗組', '【EGAO】每日笑顏維生素D3錠31粒', 
          '【福利品】金亮還原型CoQ10_植物益生菌膠囊30粒', 'ISANA抗皺緊緻精華膠囊13g_紫', 'U虎玉米棒-濃湯口味（隨機送）', 
          '【定期購】GANO彈潤光透美容水凝膠80g', '坂元黑醋1000mL', 'Deve超潤澤洗髮乳-馬油椿油椰子油480ml', 
          '日本獅王NONIO終結口氣牙膏_晶燦亮白130g', '全日營養青汁果凍條10gx28包', 'Relove_淨柔白桃_私密美白賦活晶球凝露', 
          '金壕營養多補力錠50粒', 'BFREE角鯊烷敏弱性肌膚卸妝凝露100g（精緻神祕好禮-美妝）', '【福利品】UnimatRiken愛貓元氣滿分營養粉100g', 
          '金壕營養多補C錠50粒', '全方位Clean75%抗菌清潔酒精60ml', 'ECONECO奇幻森林派對購物袋', '全日營養DHA_EPA魚油果凍條10gx7包', 
          '日本獅王浸透護齦EX牙膏_溫和草本', 'BOTANIST植物性夏季潤髮乳_白茶天竺葵480ml', '全日營養青汁果凍條10gx7包', 
          'DHC精製魚油(DHA)(30日份)90粒', 'DHC綜合礦物質(30日份)90粒', 'KOSE光映透速攻集中安心面膜7入', '【99好運轉不停】酒精濕紙巾', 
          '【EGAO】每日笑顏維生素E美妍精華膠囊62粒', 'SHILLS很耐曬超清爽美白出水防曬凝乳40ml', '飲料券-（全家免運飲料券）', 
          '野口研究卵殼膜美顏膠囊45粒', '野口研究保固精華錠225粒', 'DHC維他命B群(30日份)60粒', '全日營養乳酸菌果凍條10gx7包', 
          'SHILLS很耐曬超清爽美白美肌柔護防曬凝乳40ml', '贈口券', '日本獅王NONIO終結口氣抗敏牙膏', 'Pharmaact清新滋潤洗髮精補充包400ml', 
          '金壕營養多補鐵錠50粒', '【EGAO】每日笑顏護明綜合營養膠囊31粒', '日藥本舖U虎多功能站式月曆', 'Ora2淨色無暇牙刷_超軟毛1入', 
          'Mdmmd新涼感抑菌衛生棉_超涼感_量多28cm', 'DHC維他命B群(90日份)-180粒', '野口研究活性納豆膠囊30粒', '獅王細潔超薄小頭牙刷1入', 
          'U虎玉米棒-明太子（隨機送）', '【EGAO】每日笑顏營養對策健康青汁', '【定期購】万田酵素Mforte保養精裝禮盒組', 
          '全日營養肌美妍膠原蛋白飲_食品_100mL_10入', 'Cocoegg卵殼膜保濕化妝水500ml贈品', '日本花王新蒸氣肩頸熱敷貼12P薰衣草香', 
          '野口研究百分百膠原蛋白', 'Phoenix馬油櫻花保濕潤髮乳500mL', '金壕營養多補薏仁膠原錠50粒', 'U虎玉米棒-濃湯口味(15入)', 
          '野口研究蜂膠蜂王乳膠囊30粒', '【定期購】PurBlanche光采彈潤美容水乳液130g', '日藥本舖11年週年購物袋', '【滿件贈】万田酵素Mforte保養精裝禮盒組', 
          '全日營養蜜桃青木瓜果凍條10gx7包', '全日營養肝精薑黃飲_食品_100mL_10入', 'Deve超潤澤護髮乳-馬油椿油椰子油480ml', 'U虎環保購物袋', 
          '野口研究DHA魚油膠囊60粒', 'DHC維他命D_30粒_30日份']


# 生成 products.html 的 Python 代碼
html_template = '''
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>商品頁</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .product {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }}
        .product:last-child {{
            border-bottom: none;
        }}
        .product img {{
            max-width: 100px;
            margin-right: 20px;
        }}
        .product-info {{
            flex: 1;
        }}
        .product-name {{
            font-size: 1.2em;
            margin: 0 0 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>商品展示</h1>
        {products_html}
    </div>
</body>
</html>
'''

product_html_template = '''
        <div class="product">
            <a href="{product}.html">
                <img src="https://via.placeholder.com/100" alt="{product}">
                <div class="product-info">
                    <p class="product-name">{product}</p>
                </div>
            </a>
        </div>
'''

products_html = '\n'.join([product_html_template.format(product=product) for product in products])

with open('products.html', 'w', encoding='utf-8') as file:
    file.write(html_template.format(products_html=products_html))

# 生成單個商品詳細頁面的 Python 代碼
product_detail_template = '''
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product_name}</title>
</head>
<body>
    <h1>{product_name}</h1>
    <p>這是{product_name}的詳細介紹頁面。</p>
</body>
</html>
'''

for product in products:
    with open(f'{product}.html', 'w', encoding='utf-8') as file:
        file.write(product_detail_template.format(product_name=product))
