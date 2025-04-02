import requests
from bs4 import BeautifulSoup
import csv

# 目标URL（豆瓣电影Top250）
url = "https://movie.douban.com/top250"

# 请求头（模拟浏览器访问，避免被反爬）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 发送HTTP请求
response = requests.get(url, headers=headers)
response.encoding = "utf-8"  # 确保中文正常显示

# 检查请求是否成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 提取所有电影条目（HTML中class为"item"的div）
    movies = soup.find_all("div", class_="item")
    
    # 存储数据
    movie_list = []
    
    for movie in movies:
        # 电影标题（包含中文名和原名）
        title = movie.find("span", class_="title").text
        
        # Movie 评分
        rating = movie.find("span", class_="rating_num").text
        
        # 电影详情页链接
        link = movie.find("a")["href"]
        
        # 添加到列表
        movie_list.append([title, rating, link])
    
    # 将数据保存到CSV文件
    with open("douban_top250.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["电影名称", "评分", "链接"])  # 写入表头
        writer.writerows(movie_list)  # 写入数据
    
    print("数据已保存到 douban_top250.csv")
else:
    print("请求失败，状态码:", response.status_code)
# the end    