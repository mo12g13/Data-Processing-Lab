from bs4 import BeautifulSoup
import requests

html_content = requests.get('http://forecast.weather.gov/MapClick.php?lat=45.01265248822284&lon=-93.24372590552537#.WMn9UDsrKM8')
soup = BeautifulSoup(html_content.text, 'html.parser')
current_temp=soup.select('#current_conditions-summary > p.myforecast-current-lrg')
lower_temp = soup.select('#current_conditions-summary > p.myforecast-current-sm')
daily_tem = soup.select('#current_conditions_detail')
print(daily_tem[0].text.strip())
print('Current temperature": '+current_temp[0].text.strip())
print('Lowest temperature: '+lower_temp[0].text.strip())

html_day= requests.get('http://forecast.weather.gov/MapClick.php?lat=44.979967375000456&lon=-93.26383802699968#.WMoB7DsrKM8')
html_day.raise_for_status()
soup2 = BeautifulSoup(html_day, 'html.parser')
day_temp = soup2.select('#seven-day-forecast-list > li:nth-child(2) > div > p.period-name')
print(day_temp.text)
