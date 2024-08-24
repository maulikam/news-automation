import requests
from bs4 import BeautifulSoup
import time
import random

def fetch_hindubusinessline_headlines():
    url = "https://www.thehindubusinessline.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []

    # Capture headlines from <h2>, <h1>, and <h3> tags with relevant classes
    for tag in ['h1', 'h2', 'h3']:
        for item in soup.find_all(tag, class_=['imgStory', 'title', 'news-lg-title']):
            link = item.find('a')
            if link:
                headline = link.get_text().strip()
                article_url = link['href']
                if not article_url.startswith('http'):
                    article_url = 'https://www.thehindubusinessline.com' + article_url
                articles.append({'headline': headline, 'url': article_url})

    return articles

def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Fetch the main article content from the specific div
    content_div = soup.find('div', id=lambda x: x and x.startswith('content-body-'))
    if not content_div:
        content_div = soup.find('div', class_='Normal')

    article_content = ' '.join([p.get_text().strip() for p in content_div.find_all('p') if p.get_text().strip()])

    return article_content

if __name__ == "__main__":
    articles = fetch_hindubusinessline_headlines()
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['headline']}")
        print(f"URL: {article['url']}")

        content = fetch_article_content(article['url'])
        print(f"Content: {content[:500]}...")  # Print the first 500 characters of the content
        print("-" * 80)

        # Random sleep interval between 1 to 3 seconds
        time.sleep(random.uniform(1, 3))
