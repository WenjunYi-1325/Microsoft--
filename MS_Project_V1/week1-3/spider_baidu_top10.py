import requests
from bs4 import BeautifulSoup

from mysql_helper import MySqlHelper

url = "https://top.baidu.com/board?tab=realtime"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

print("状态码：", response.status_code)

soup = BeautifulSoup(response.text, "lxml")


# 1. 找到所有热点卡片
items = soup.find_all(
    "div",
    class_="category-wrap_iQLoo"
)

print("找到热点卡片数量：", len(items))


# 2. 排除置顶新闻
hot_items = []

for item in items:

    top_icon = item.find(
        "img",
        class_="top-icon_15tUE"
    )

    if top_icon:
        continue

    hot_items.append(item)

print("过滤后热点数量：", len(hot_items))


# 3. 取真正的 Top 10
top10 = hot_items[:10]

print("\n百度热搜 Top 10：")


# 4. 提取每一个热点的数据
hot_list = []

for item in top10:
    rank = item.find(
        "div",
        class_="index_1Ew5p"
    )

    title = item.find(
        "div",
        class_="c-single-text-ellipsis"
    )

    hot = item.find(
        "div",
        class_="hot-index_1Bl1a"
    )

    link = item.find("a")

    hot_data = {
    "rank": int(rank.text.strip()),
    "title": title.text.strip(),
    "hot": int(hot.text.strip()),
    "url": link.get("href")
    }

    hot_list.append(hot_data)

print("\n最终数据：")

for hot in hot_list:
    print(hot)


#5. 连接Mysql
db = MySqlHelper()

#6. 准备insert sql
sql = """
INSERT INTO baidu_hot
(rank_num, title, hot, url)
VALUES (%s, %s, %s, %s)
"""

#7. 将数据逐一导入数据库
for hot in hot_list:

    params = (
        hot["rank"],
        hot["title"],
        hot["hot"],
        hot["url"]
    )

    db.execute(sql, params)


db.close()

print("数据保存成功！")
