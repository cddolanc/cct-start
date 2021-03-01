# pip install requests
# pip install lxml
# pip install bs4


import requests

# # Step 1: Use the requests library to grab the page
# # Note, this may fail if you have a firewall blocking Python/Jupyter 
# # Note sometimes you need to run this twice if it fails the first time
# res = requests.get("https://034f8a1dcb5c.eu.ngrok.io/course/view.php?id=12")

# type(res)

# print(res.text)


import bs4

# soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)

# print(soup.select('title'))



# First get the request
res = requests.get('https://034f8a1dcb5c.eu.ngrok.io/course/view.php?id=12')

# Create a soup from request
soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)

soup.select("div")

for item in soup.select("div"):
    print(item.text)