import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.amazon.in/?&tag=googinhydmabk-21&ref=pd_sl_5m73uf1pk6_e&adgrpid=159067178132&hvpone=&hvptwo=&hvadid=678754928338&hvpos=&hvnetw=g&hvrand=10990278355365908385&hvqmt=e&hvdev=m&hvdvcmdl=&hvlocint=&hvlocphy=9146123&hvtargid=kwd-10544572015&hydadcr=4305_2265528")#("https://www.livemint.com/news/india/mumbai-news-maratha-quota-protest-march-to-cause-traffic-snarls-on-republic-day-2024-details-here/amp-11706152008632.html#amp_tf=From%20%251%24s&aoh=17062006866637&referrer=https%3A%2F%2Fwww.google.com")
soup = BeautifulSoup(req.content,"html.parser")
res = soup.title
print (soup.prettify())