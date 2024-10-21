import feedparser
from newspaper import Article
from newspaper import Config

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
config = Config()
config.browser_user_agent = user_agent

if __name__ == '__main__':
    feed = feedparser.parse("https://cointelegraph.com/rss/tag/bitcoin")
    for entry in feed.entries[:5]:
        article = Article(entry.id, config=config)
        try:
            article.download()
            article.parse()

            print(article.text)
        except Exception as e:
            print("Error", str(e))
            pass