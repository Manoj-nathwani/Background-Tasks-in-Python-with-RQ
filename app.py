import os
from flask import Flask
from flask import render_template
from rq import Queue
from worker import conn
from utils import count_words_at_url

app = Flask(__name__)
q = Queue(connection=conn)

@app.route('/')
def index():
    return render_template('index.html', name="Manoj")

@app.route('/test')
def test():
    result = q.enqueue(count_words_at_url, 'http://heroku.com')
    return str(result)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
