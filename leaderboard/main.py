import requests
from bs4 import BeautifulSoup
import datetime
import requests
from bs4 import BeautifulSoup

spreadsheet_id = '17CASSRNu_l8kQT5YRVAz_G7diQHq9Mp-kDQ4YAYPN-o'

# The URL of the Google Spreadsheet's published view
url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/htmlview'

table = ''


last_run_date = ''

def extract_data():
    global table
    global last_run_date
    current_date = datetime.datetime.now().date()
    
    if current_date != last_run_date:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        last_run_date = current_date



x = 0
def get_data():
    data = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        row_data = ''
        for col in columns:
            if col.text:
                row_data+= f'{col.text} '
        if 'affiliate_name' in row_data:pass
        else:
            if len(row_data) !=0:
                #print(row_data.split(' '))
                code,code2,name, wager, rank , date1,time1,x,date2,time2,y,z = row_data.split(' ')
                #print(f"User name {name}, Amount wagered : {wager}, rank : {rank}")
                rank = int(rank)
                if rank == 1:amt = '₹ 20,000'
                elif rank == 2:amt = '₹ 10,000'
                elif rank == 3:amt = '₹ 5000'
                elif rank == 4:amt = '₹ 3000'
                elif rank == 5:amt = '₹ 2000'
                elif rank > 5 and rank <11:amt ='₹ 1000'
                elif rank >10 and rank <21:amt = '₹ 500'
                else: amt = '₹ 0'
                data.append({
                    "rank": int(rank),
                    "name":name,
                    "kudos": wager,
                    "handle": f'Prize : {amt}'
                })
    return data

def get_time():
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        row_data = ''
        for col in columns:
            if col.text:
                row_data+= f'{col.text} '
        if 'affiliate_name' in row_data:pass
        else:
            if len(row_data) !=0:
                #print(row_data.split(' '))
                code,code2,name, wager, rank , date1,time1,x,date2,time2,y,z = row_data.split(' ')
                #print(f"User name {name}, Amount wagered : {wager}, rank : {rank}")
                timeinterval = f'{date1} - {date2}'
    return timeinterval

def get_winner():
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        row_data = ''
        for col in columns:
            if col.text:
                row_data+= f'{col.text} '
        if 'affiliate_name' in row_data:pass
        else:
            if len(row_data) !=0:
                #print(row_data.split(' '))
                code,code2,name, wager, rank , date1,time1,x,date2,time2,y,z = row_data.split(' ')
                #print(f"User name {name}, Amount wagered : {wager}, rank : {rank}")
                if int(rank) ==1:
                    return wager
    

