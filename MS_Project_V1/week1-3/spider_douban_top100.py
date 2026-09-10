import requests
from bs4 import BeautifulSoup

from mysql_helper import MySqlHelper


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}


movies = []

for start in [0, 25, 50, 75]:

    url = f"https://movie.douban.com/top250?start={start}"

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    print("状态码：", response.status_code)


    soup = BeautifulSoup(response.text, "lxml")

    items = soup.find_all("div", class_="item")
    print("找到电影数量：", len(items))



    for item in items:

        # 排名
        rank = item.find("em")
        rank = int(rank.text.strip())

        # 电影名
        titles = item.find_all("span", class_="title")
        title = titles[0].text.strip()

        # 评分
        rating = item.find("span", class_="rating_num")
        rating = float(rating.text.strip())

        # 评价人数
        vote_text = None

        spans = item.find_all("span")

        for span in spans:
            text = span.get_text(strip=True)

            if "人评价" in text:
                vote_text = text
                break

        if vote_text:
            votes = int(vote_text.replace("人评价", "").strip())
        else:
            votes = None

        # 详情链接
        link = item.find("div", class_="hd").find("a")
        link = link.get("href")

        # 基本信息
        info = item.find("div", class_="bd").find("p")
        info_parts = list(info.stripped_strings)



        if len(info_parts) >= 1:

            director_actor = info_parts[0]

            parts = director_actor.split("主演:")

            director = parts[0].replace("导演:", "").strip()

            if len(parts) >= 2:
                actors = parts[1].strip()
            else:
                actors = None

        else:
            director = None
            actors = None


        if len(info_parts) >= 2:

            details = info_parts[1].split("/")

            if len(details) >= 3:
                year = details[0].strip()
                country = details[1].strip()
                genre = details[2].strip()
            else:
                year = None
                country = None
                genre = None

        else:

            year = None
            country = None
            genre = None


        # 组成一部电影的数据
        movie = {
            "rank": rank,
            "title": title,
            "rating": rating,
            "people": votes,
            "director": director,
            "actors": actors,
            "year": year,
            "country": country,
            "genre": genre,
            "link": link
        }

        movies.append(movie)


print("最终电影数量：", len(movies))
    


db = MySqlHelper()

success = db.execute("TRUNCATE TABLE douban_movies")

if success:
    print("数据库旧数据已清空")
else:
    print("数据库清空失败")


sql = """
INSERT INTO douban_movies
(rank_num, title, rating, people, director, actors, year, country, genre, link)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for movie in movies:

    params = (
        movie["rank"],
        movie["title"],
        movie["rating"],
        movie["people"],
        movie["director"],
        movie["actors"],
        movie["year"],
        movie["country"],
        movie["genre"],
        movie["link"]
    )

    db.execute(sql, params)


# 查询数据库
result = db.query_all("SELECT * FROM douban_movies")

print("数据库数据条数：", len(result))

for row in result[:3]:
    print(row)


db.close()