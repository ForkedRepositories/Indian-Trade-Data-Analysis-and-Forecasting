#Importing packages
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup 

YY = [str(i) for i in range(2007,2021)]
MM = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

# YY = ['2020']
# MM = ['JAN','FEB']

df = pd.DataFrame(columns = ['Country', 'Value', 'Date'])
driver = webdriver.Chrome('C:/Users/Akars/Documents/Scrape/chromedriver')
for Year in YY:
	for Month in MM:
		
		driver.get("https://commerce-app.gov.in/meidb/cntq.asp?ie=e")

		calendar_year = driver.find_elements_by_xpath('//*[@id="radioCY"]')
		calendar_year[0].click()

		month = driver.find_elements_by_xpath('//*[@id="select1"]')
		Select(month[0]).select_by_visible_text(Month)

		year = driver.find_elements_by_xpath('//*[@id="select2"]')
		Select(year[0]).select_by_visible_text(Year)


		value = driver.find_elements_by_xpath('//*[@id="radiousd"]')
		value[0].click()

		submit = driver.find_elements_by_xpath('//*[@id="button1"]')
		script = submit[0].click()

		soup=BeautifulSoup(driver.page_source, 'html')
		table = soup.find('table')
		table_rows = table.find_all('tr')
		col = []
		res = []
		for tr in table_rows[:-1]:
		    td = tr.find_all('td')
		    row = [tr.text.strip() for tr in td[:-3]]
		    if row:
		        res.append(row)
		    else:
		        th = tr.find_all('th')
		        col = [tr.text.strip() for tr in th[:-3] if tr.text.strip()]
		        print(col)
		df_small = pd.DataFrame(res, columns = ['S.No.', 'Country', 'Value_prev_year', 'Value', '%Growth'])
		df_small['Date'] = pd.to_datetime('{}-{}'.format(Year, Month))
		df_small.drop(['S.No.','Value_prev_year','%Growth'],axis = 1,inplace = True)
		df = df.append(df_small)

df.to_csv('Year-Country-Value_Export.csv', header = True, index = False)