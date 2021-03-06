# def func_one(n):
#     '''
#     Given a number n, returns a list of string integers
#     ['0','1','2',...'n]
#     '''
#     return [str(num) for num in range(n)]

# # print(func_one(10))

# def func_two(n):
#     '''
#     Given a number n, returns a list of string integers
#     ['0','1','2',...'n]
#     '''
#     return list(map(str,range(n)))

# # print(func_two(10))

# import time

# # STEP 1: Get start time
# start_time = time.time()
# # Step 2: Run your code you want to time

# result = func_one(1000000)
# # Step 3: Calculate total time elapsed
# end_time = time.time() - start_time

# print(end_time)

# # STEP 1: Get start time
# start_time = time.time()
# # Step 2: Run your code you want to time
# result = func_two(1000000)
# # Step 3: Calculate total time elapsed
# end_time = time.time() - start_time

# print(end_time)


# import timeit

# setup = '''
# def func_one(n):
#     return [str(num) for num in range(n)]
# '''

# stmt = 'func_one(100)'

# print(timeit.timeit(stmt,setup,number=100000))


# setup2 = '''
# def func_two(n):
#     return list(map(str,range(n)))
# '''

# stmt2 = 'func_two(100)'

# print(timeit.timeit(stmt2,setup2,number=100000))



# f = open("new_file.txt",'w+')
# f.write("Here is some text")
# f.close()

# f = open("new_file2.txt",'w+')
# f.write("Here is some text")
# f.close()


# import zipfile

# comp_file = zipfile.ZipFile('comp_file.zip','w')

# comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)

# comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)

# comp_file.close()


# zip_obj = zipfile.ZipFile('comp_file.zip','r')

# zip_obj.extractall("extracted_content")

# import shutil

# directory_to_zip='/workspace/cct-start/extracted_content'

# # Creating a zip archive
# output_filename = 'example'
# # Just fill in the output_filename and the directory to zip
# # Note this won't run as is because the variable are undefined
# shutil.make_archive(output_filename,'zip',directory_to_zip)



# pip install requests
# pip install lxml
# pip install bs4

# import requests

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

# title_tag = soup.select('title')
# title_tag[0]
# type(title_tag[0])
# print(title_tag[0].getText())


# # First get the request
# res = requests.get('https://en.wikipedia.org/wiki/Yuri_Gagarin')
# # Create a soup from request
# soup = bs4.BeautifulSoup(res.text,"lxml")

# # note depending on your IP Address,
# # this class may be called something different
# soup.select(".mw-headline")
# for item in soup.select(".mw-headline"):
#     print(item.text)

# import requests
# import bs4

# base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# # res = requests.get(base_url.format(n))

# soup = bs4.BeautifulSoup(res.text,"lxml")

# two_star_books = []

# for n in range(1,51):

#     res = requests.get(base_url.format(n))

#     for book in soup.select(".product_pod"):
#             if book.select('.Two'):
#                 two_star_books.append(book.select('a')[1]['title'])

#     print(two_star_books)

# soup.select(".product_pod")

# products = soup.select(".product_pod")

# example = products[0]

# type(example)

# print(example.attrs)

# print(list(example.children))

# print(example.select('.star-rating.Two'))





import requests
import bs4
import lxml

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

two_star_books = []

for n in range(1,51):

    res = requests.get(base_url.format(n))

    soup = bs4.BeautifulSoup(res.text,"lxml")
    # Thanks to Michael
    for book in soup.select('.product_pod'):
        if book.select('.Two'):
            two_star_books.append(book.select('a')[1]['title'])
    print(n)
    
print(two_star_books)

# from bs4 import BeautifulSoup
# import requests
# page = requests.get('https://forecast.weather.gov/MapClick.php?lat=47.19044000000008&lon=-122.29563999999999#.Xq3cLZl7lPY')
# soup = BeautifulSoup(page.text, 'lxml')
# print(soup)