from bs4 import BeautifulSoup
import requests
import pandas as pd


def process_page(url: str):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "html.parser")

    table_rows = soup.select('.data-table__row')
    raw_data = []
    for row in table_rows:
        # print(type(row))
        # print(row.select(".data-table__value"))
        row_list = []
        for item in row.select(".data-table__value"):
            # print(item.getText())
            row_list.append(item.getText())
        raw_data.append(row_list)
    # print(raw_data)

    for item in raw_data:
        item[0] = int(item[0])
        item[3] = int(item[3].replace('$', '').replace(',', ''))
        item[4] = int(item[4].replace('$', '').replace(',', ''))
        # item[5] = int(item[5].replace('%', ''))
    return raw_data


# print(raw_data)
final_data = []
for i in range(1, 10):
    print(f'processing page {i}')
    page_url = f'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}'
    page_data = process_page(page_url)
    for row in page_data:
        final_data.append(row)

df = pd.DataFrame(final_data, columns=['rank', 'major', 'degree type',
                                       'early career pay', 'mid career pay', 'high meaning'])

# print(df.head())
print(df.shape)

print(df[['major', 'early career pay', 'mid career pay']].groupby('major').mean(). \
      sort_values('early career pay', ascending=False).head(5))

print(df[['major', 'early career pay', 'mid career pay']].groupby('major').mean(). \
      sort_values('mid career pay', ascending=False).head(5))
