from bs4 import BeautifulSoup
import urllib2


response = urllib2.urlopen('https://app.meltwater.com/api/public/newsletters/592f3000745c6403248d10d6/newsletter/distribution/5eb08998dd284a0cf9bf5137/html')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))