from flask import Flask, url_for, render_template, request
from spacy_summarization import text_summarizer
import spacy
nlp = spacy.load ('en')
from bs4 import BeautifulSoup
from urllib import urlopen
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        # SUMMARIZATION
        final_summary = text_summarizer(rawtext)
    return render_template('index.html', final_summary)


# GET DATA FROM URL
def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    fetched_text = ' '.join(map(lambda p: p.text.soup.find_all('p')))
    return fetched_text


@app.route('/analyze_url', methods=['GET', 'POST'])
def analyze_url():
    if request.method == 'POST':
        raw_url = request.form['raw_url']
        rawtext = get_text(raw_url)

        # SUMMARIZATION
        final_summary = text_summarizer(rawtext)
    return render_template('index.html', final_summary)


if __name__ == '__main__':
    app.run(debug=True)
