import requests
from bs4 import BeautifulSoup
import time
import random

def fetch_toi_headlines():
    url = "https://timesofindia.indiatimes.com/business"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []

    # Find all figure elements containing articles
    for item in soup.find_all('figure', class_='_YVis'):
        headline = item.find('figcaption').get_text().strip()
        article_url = item.find('a')['href']
        if not article_url.startswith('http'):
            article_url = 'https://timesofindia.indiatimes.com' + article_url

        articles.append({'headline': headline, 'url': article_url})

    return articles

def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check for content in divs with class '_s30J clearfix'
    content_divs = soup.find_all('div', class_='_s30J clearfix')
    if not content_divs:
        # If no content found in the first div class, check for divs with class 'Normal'
        content_divs = soup.find_all('div', class_='Normal')

    article_content = ' '.join([div.get_text().strip() for div in content_divs])

    return article_content

if __name__ == "__main__":
    articles = fetch_toi_headlines()
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['headline']}")
        print(f"URL: {article['url']}")

        content = fetch_article_content(article['url'])
        print(f"Content: {content[:500]}...")  # Print the first 500 characters of the content
        print("-" * 80)

        # Random sleep interval between 1 to 3 seconds
        time.sleep(random.uniform(1, 3))
