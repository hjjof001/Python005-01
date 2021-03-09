import codecs

from bs4 import BeautifulSoup as bs
import csv
import requests

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}

url = "https://maoyan.com/board"

response = requests.get(url, headers=headers)

bs_res = bs(response.text, 'html.parser')

with open('movie_top10.csv','w', newline='', encoding='utf-8') as csvfile:
    csvfile.write(codecs.BOM_UTF8.decode('utf-8'))
    fieldnames = ['电影名称','电影类型','上映时间']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tags in bs_res.find_all('div', attrs={'class': 'board-item-content'}):
        movie = {}
        movie["电影名称"] = tags.find('p', attrs={'class': 'name'}).a['title']
        movie["电影类型"] = tags.find('p', attrs={'class': 'star'}).text.strip()
        movie["上映时间"] = tags.find('p', attrs={'class': 'releasetime'}).text.strip().split('：')[1]
        writer.writerow(movie)
        

