import requests

from bs4 import BeautifulSoup

print('requestModule.py')

# url = "https://dummyjson.com/products"

# response = requests.get(url)

# print(response.text)

url = "https://datesheet.vu.edu.pk"

response = requests.get(url)

# print(response.text)

result = BeautifulSoup(response.text,"html.parser")

# print(result.prettify())


# result = BeautifulSoup(response.text, "html.parser")

# print(result.prettify())

# for strong in result.find_all("strong"):
#     print(strong.text)
# for strong in result.find_all("tr"):
#     print(strong.text)
for strong in result.find_all("a"):
    print(strong.text)


