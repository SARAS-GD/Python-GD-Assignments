"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://finance.yahoo.com/markets/stocks/most-active/'
response = requests.get(url)

if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")

content=response.text
soup = BeautifulSoup(content, 'lxml')
company_name=[]
span_values = soup.find_all('span', class_='symbol yf-ravs5v')

for i in span_values[:10]:
    title = i.get_text()

    company_name.append(title)

def most_young_ceo():
    details=[]
    for k in company_name:
        profile_page = f'https://finance.yahoo.com/quote/{k}/profile/'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        response = requests.get(profile_page, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        country_parent = soup.find('div', class_="address yf-wxp4ja")
        if country_parent:
            divs = country_parent.find_all('div')
        country = divs[-1].text.strip()
        Employees = soup.find('strong').text.strip()
        count = 0
        table = soup.find('table')
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            CEO_Name = cols[0].text.strip()
            Name = cols[1].text.strip()
            CEO_Year_Born = cols[4].text.strip()
                        # volume = cols[6].text.strip()
            if count==0:
                details.append({
                        "Name": Name,
                        "Country": country,
                        "Employees": Employees,
                        "CEO_Name": CEO_Name,
                        "CEO_Year_Born": CEO_Year_Born,
                        })
                count+=1
            else:
                break
        # print(row)
    return details
def tabulate():
    details = most_young_ceo()
    df = pd.DataFrame(details)
    sorted_df = df.sort_values("CEO_Year_Born", ascending=False)
    return sorted_df[:5]


print(tabulate())