import requests

# # Step 1: Use the requests library to grab the page
# # Note, this may fail if you have a firewall blocking Python/Jupyter 
# # Note sometimes you need to run this twice if it fails the first time
# res = requests.get("http://www.example.com")

# print(type(res))

# print(res.text)

# import bs4

# soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)

# print(soup.select('title'))


import bs4

# soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)

# soup.select('title')



# First get the request
# res = requests.get('https://en.wikipedia.org/wiki/Yuri_Gagarin')

# # Create a soup from request
# soup = bs4.BeautifulSoup(res.text,"lxml")

# # print(soup)

# soup.select(".mw-headline")

# for item in soup.select(".mw-headline"):
#     print(item.text)

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text,'lxml')

image_info = soup.select('.thumbimage')

image_info

print(len(image_info))

computer = image_info[0]

print(type(computer))

print(computer['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

# The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
image_link.content

f = open('my_new_file_name.jpg','wb')

f.write(image_link.content)

f.close()