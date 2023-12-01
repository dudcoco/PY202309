import os
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
from operator import itemgetter

# 웹페이지에서 div 태그의 quote 클래스에 해당하는 내용 저장
url = 'https://quotes.toscrape.com/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
quotes = soup.find_all('div', {'class': "quote"})

# 단어들을 리스트에 저장
word_list = []

# span 태그의 text 클래스에 해당하는 내용 저장 및 단어추출
for quote in quotes:
    quote = quote.find_all('span', {'class': 'text'})
    for i in quote:
        # 단어 추출
        words = i.text.lower().split()
        word_list.extend(words)

# 딕셔너리에 단어 빈도수를 저장
word_freq = {}

# 단어들의 빈도수를 계산
for word in word_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# 가장 많이 등장한 순으로 정렬
sorted_word_freq = sorted(word_freq.items(), key=itemgetter(1), reverse=True)

# 상위 5개의 단어 출력
print("=== 상위 5개 단어 출력 ===")
for word, freq in sorted_word_freq[:5]:
    print(f"{word}: {freq}회")
