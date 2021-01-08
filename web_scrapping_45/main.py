from bs4 import BeautifulSoup

with open('website.html', 'r') as file_handle:
    contents = file_handle.read()

# print(contents)

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# print(soup.prettify())

# Get the anchor tag
# print(soup.a)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
for anchor in all_anchor_tags:
    print(anchor.getText(), anchor.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

company_url = soup.select_one(selector="p a")
print(company_url)
print(company_url.get("href"))

name = soup.select("#name")
print(name)

heading = soup.select(".heading")
print(heading)



