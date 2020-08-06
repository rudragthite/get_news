from get_news.main import RssScrapper

class ScrapNews:

    def Start_Scrapping(self):
        a = RssScrapper()
        a.get_all(file="C:/Users/rudra/Downloads/Inter_Project/get_news/Feed_URLs.txt")

