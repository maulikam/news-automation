import requests
from bs4 import BeautifulSoup

def fetch_toi_headlines():
    url = "https://timesofindia.indiatimes.com/business"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []

    # Targeting figcaption elements which contain the headlines
    for item in soup.find_all('figcaption'):
        headline_text = item.get_text().strip()
        if headline_text and headline_text not in headlines:
            headlines.append(headline_text)

    return headlines

if __name__ == "__main__":
    headlines = fetch_toi_headlines()
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
