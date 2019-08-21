import flask
import sys

sys.path.insert(0,'C:/Users/hotan/Documents/GitHub/ShareScraper/api')
#from ShareScraper import CurrentPortfolioValue
import ShareScraper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    value = ShareScraper.CurrentPortfolioValue()
    return str(value)

app.run()
