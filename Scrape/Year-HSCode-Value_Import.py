#Importing packages
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup 

YY = [str(i) for i in range(2007,2021)]

MM = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

df = pd.DataFrame(columns = ['HSCode', 'Commodity', 'Value', 'Date'])
driver = webdriver.Chrome('C:/Users/Akars/Documents/Scrape/chromedriver')

for Year in YY:
	for Month in MM:
		driver.get("https://commerce-app.gov.in/meidb/comq.asp?ie=i")
		calendar_year = driver.find_elements_by_xpath('//*[@id="radioCY"]')
		calendar_year[0].click()

		month = driver.find_elements_by_xpath('//*[@id="select1"]')
		Select(month[0]).select_by_visible_text(Month)

		year = driver.find_elements_by_xpath('//*[@id="select2"]')
		Select(year[0]).select_by_visible_text(Year)

		all_commodities = driver.find_elements_by_xpath('//*[@id="radio2"]')
		all_commodities[0].click()

		all_record = driver.find_elements_by_xpath('//*[@id="radioDAll"]')
		all_record[0].click()

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
		df_small = pd.DataFrame(res, columns = ['S.No.', 'HSCode', 'Commodity', 'Value_prev_year', 'Value', '%Growth'])
		df_small['Date'] = pd.to_datetime('{}-{}'.format(Year, Month))
		df_small.drop(['S.No.','Value_prev_year','%Growth'],axis = 1,inplace = True)
		df = df.append(df_small)

df.to_csv('Year-HSCode-Value_Import.csv', header = True, index = False)