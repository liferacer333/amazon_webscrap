
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

url = 'https://www.amazon.in/Dell-Office21-Inspiron-3515-D560702WIN9BE/product-reviews/B09NLRSKV3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(url,headers=headers)
page.content
soup = bs(page.content,'html.parser')
print(soup.prettify())

names = soup.find_all('span',class_='a-profile-name')
names

cust_names = []
for name in range(0,len(names)):
    cust_names.append(names[name].get_text())
cust_names   

cust_names.pop(2)
cust_names.pop(2)
cust_names
cust_names.pop(4)
cust_names.pop(5)
cust_names.pop(8)

cust_names

reviews = soup.find_all('a',class_="review-title")
reviews

reviews_title = []
for review in range(0,len(reviews)):
    reviews_title.append(reviews[review].get_text())
reviews_title 

reviews_title = [titles.strip('\n') for titles in reviews_title]
reviews_title

ratings = soup.find_all('i',class_='review-rating')
ratings

reviews_rating = []
for rating in range(0,len(ratings)):
    reviews_rating.append(ratings[rating].get_text())
reviews_rating 

reviews_rating.pop(0)
reviews_rating.pop(0)
reviews_rating

desc = soup.find_all('span',class_='review-text')
desc

reviews_desc = []
for content in range(0,len(desc)):
    reviews_desc.append(desc[content].get_text())
reviews_desc  

reviews_desc = [body.strip('\n') for body in reviews_desc]
reviews_desc

print(cust_names)
print(reviews_title)
print(reviews_rating)
print(reviews_desc)

df = pd.DataFrame()
df['Customer Name'] = cust_names
df['Rating'] = reviews_rating
df['Review Title'] = reviews_title
df['Review Description'] = reviews_desc

df.to_csv(r'reviews.csv')
