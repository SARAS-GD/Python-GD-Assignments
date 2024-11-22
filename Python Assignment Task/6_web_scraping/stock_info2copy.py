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

stat_page = 'https://finance.yahoo.com/markets/stocks/most-active/?start=0&count=227'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
response1 = requests.get(stat_page, headers=headers)

def top_10_stocks():
    list1=[]
    soup = BeautifulSoup(response1.text, 'lxml')
    table=soup.find('table',class_="markets-table freeze-col yf-1dbt8wv fixedLayout").find('tbody')
    table_row=table.find_all('tr') 
    for row in table_row:
        cells = row.find_all('td')
        name_tag = cells[0].find('span', class_='longName')
        code_tag = cells[0].find('span', class_='symbol yf-ravs5v')
        Name = name_tag.text.strip()
        Code = code_tag.text.strip()
        _52_week_change = cells[8].text.strip()
        Total_cash = cells[5].text.strip()
        list1.append({
            "Name": Name,
            "Code": Code,
            "_52_week_change": _52_week_change,
            "Total_cash": Total_cash
                        })
    return list1

def tabulate1():
    details = top_10_stocks()
    df = pd.DataFrame(details)
    df['_52_week_change'] = df['_52_week_change'].str.replace('%', '', regex=False)
    df['_52_week_change'] = df['_52_week_change'].str.replace(',', '', regex=False).astype(float)

    
    df_sorted1 = df.sort_values(by="_52_week_change", ascending=False)
    sorted_df_reset = df_sorted1.reset_index(drop=True)
    return sorted_df_reset[:10]

tabulate1()

    
    


    