import requests
from bs4 import BeautifulSoup

Url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

r = requests.get(Url)

# Belirlediğimiz URL'e gider.

Soup = BeautifulSoup(r.text, "html5lib")

List = Soup.find("tbody", {"class":"lister-list"}).find_all("tr")

# Soup değişkeni html belgesini düzenli şekilde verir
# List değişkeni htmldeki sınıfı lister-list oan tbody'i bulur ve içindeki tr leri verir. find yazarsak 1 find_all yazarsak hepsini verir.

for Film in List:
    Name = Film.find("td", {"class":"titleColumn"}).a.text
    # td içindeki titeCoumun içindeki a textlerini alır
    # Sadece film isimlerini verir
    Tarih = Film.find("td", {"class":"titleColumn"}).span.text.strip("()")
    Rating = Film.find("td", {"class":"ratingColumn imdbRating"}).text.strip()

    print(f"""
    Film : {Name}
    Tarih : {Tarih}
    Rating : {Rating}
    """)
