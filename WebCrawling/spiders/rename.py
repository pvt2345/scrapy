import scrapy
import glob
import os
import codecs
from fuzzywuzzy import fuzz
import string
# from ..search_engine_LCS import SearchEngine
# class rename_spider(scrapy.Spider):
#     name = "rename_spider"
#     start_urls = ["file:///D:/File/TranslatedHTML/0e60dc388343b96f154ced76a20f44ae86caf9ce.html"]
#     pdf_path = "D:\File\PaperCrawler\*.pdf"
#     pdf_files = []
#     pdf_files_ = glob.glob(pdf_path)
#     for item in pdf_files_:
#         pdf_files.append(item.split('\\')[-1][:-4])
#
#     def parse(self, response):
#         title = response.css("a::attr(onclick)").extract_first().split('&')[2][9:]
#         html_path = '/'.join(response.urls.split('/')[:-1])
#         if title is None:
#             title = response.css("head title::text").extract_first()
#             os.rename(response.urls, html_path + '/' + title)
#         else:
#             pdf_path = "D:\File\PaperCrawler\*.pdf"
#             pdf_files = []
#             pdf_files_ = glob.glob(pdf_path)
#             for item in pdf_files_:
#                 pdf_files.append(item.split('\\')[-1][:-4])
#
#             searcher = SearchEngine(title)
#             item_ = pdf_files[0]
#             score = searcher.LCS4Sentence(item_, '0010')[0]
#             for item in pdf_files:
#                 score_ = searcher.LCS4Sentence(item, '0010')[0]
#                 if score_ > score:
#                     score = float(score_)
#                     item_ = str(item)
#             os.rename(response.urls, html_path + '/' + item_)

if __name__ == '__main__':
    #
    # e = "5G in MENA GCC operators set for global leadership"
    # d = 'US Advanced Manufacturing Leadership Strategy '
    # f = 'STRATEGY FOR AMERICAN LEADERSHIP IN ADVANCED MANUFACTURING'
    #
    # with open("D:/File/TranslatedHTML/0e60dc388343b96f154ced76a20f44ae86caf9ce.html","r", encoding="UTF-8") as f:
    #     text = f.read()
    html_path = "D:\File\TranslatedHTML\*.html"
    html_files = glob.glob(html_path)
    html_files = [item.replace('\\', '/') for item in html_files]
    # for item in html_files:
    punc = "\ / : * ? \" < > |".split()
    print(html_files)
    for path in html_files:
        with codecs.open(path, "r", encoding="UTF-8") as f:
            text = f.read()
        sel = scrapy.Selector(text=text)
        title = sel.css("a::attr(onclick)").extract_first()
        html_path = '/'.join(f.name.split('/')[:-1])
        if title is None:
            title = sel.css("head title::text").extract_first()
            for c in punc:
                title = title.replace(c, "")
                
            os.rename(f.name, html_path  + '/' + title + '.html')
        else:
            title = title.split('&')[2][9:]
            pdf_path = "D:\File\PaperCrawler\*.pdf"
            pdf_files = []
            pdf_files_ = glob.glob(pdf_path)
            for item in pdf_files_:
                pdf_files.append(item.split('\\')[-1][:-4])

            # searcher = SearchEngine(title)
            item_ = pdf_files[0]
            # score = searcher.LCS4Sentence(item_, '0010')[0]
            score = fuzz.ratio(title.lower(), item_.lower())
            for item in pdf_files:
                # score_ = searcher.LCS4Sentence(item, '0010')[0]
                score_ = fuzz.ratio(title.lower(), item.lower())
                if score_ > score:
                    score = float(score_)
                    item_ = str(item)
            os.rename(f.name, html_path + '/' + item_ + '.html')
