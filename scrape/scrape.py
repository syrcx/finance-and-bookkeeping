import re
import requests
from bs4 import BeautifulSoup

url = 'http://wenshu.court.gov.cn/list/list/?sorttype=1&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E5%A4%A9%E6%B4%A5%E5%8C%BB%E8%8D%AF%E9%9B%86%E5%9B%A2'
# The site had blocked robots.So needs access with user agent as a browser.
# https://stackoverflow.com/questions/37625461/why-cant-i-access-the-html-of-some-websites
headers = {'content-type': 'application/json', 'User-agent': 'Mozilla/5.0'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

print(soup)
for i in soup.find_all('div', {'class': "download"}):
    print("start ==============")
    print(i)
    print("end ================")
#print(re.search('http://.*\.apk', i.get('href')).group(0))




#print('Beginning file download with urllib2...')
#
#url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
#urllib.request.urlretrieve(url, '/Users/xiaocao/Downloads/cat.jpg')
#urllib.request.urlretrieve('http://wenshu.court.gov.cn/content/content?DocID=1ebd1319-6b24-4990-8e63-a756011d9296', 'file.docx')
