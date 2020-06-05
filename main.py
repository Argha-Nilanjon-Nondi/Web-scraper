from bs4 import BeautifulSoup
import requests
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,'referer':'https://www.google.com/'}
url="pixabay.com/images/search/server/"
html = requests.get("http://webcache.googleusercontent.com/search?q=cache:"+url,headers=headers).text

print("Downloaded complete")
def html_parse(html):
	soup=BeautifulSoup(html,"html.parser")
	link=soup.find_all("div",class_="item")
	image_link=[]
	for i in link:
		image_link.append(i.find("meta",itemprop="contentUrl").get("content"))
	return image_link
	
print("Data achieved . ")
a=html_parse(html)

b=0
for i in range(len(a)):
	data=requests.get(a[i]).content
	open(str(b)+".png","wb").write(data)
	print("Downloading image {0}".format(b))
	b+=1