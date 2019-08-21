from flask import render_template
import flask
import connexion
import ShareScraper

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

app.run(debug=True)
