import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import feedparser
from flask import Flask
app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss"}

@app.route("/")
@app.route("/zhihu")
def zhihu():
    return get_news('zhihu')
@app.route("/netease")
def netease():
    return get_news('netease')
@app.route("/songshuhui")
def ifeng():
    return get_news('songshuhui')
def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return """<html>
       <body>
           <h1> news Headlines </h1>
           <b>{0}</b> <br/>
           <i>{1}</i> <br/>
           <p>{2}</p> <br/>
       </body>
   </html>""".format(first_article.get("title"), first_article.
   get("published"), first_article.get("summary"))

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000, debug=True)
