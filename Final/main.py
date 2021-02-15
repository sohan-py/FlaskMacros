from flask import Flask
from flask import render_template
from blogs import blogs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            blogs=blogs)

if __name__ == '__main__':
    app.run()
