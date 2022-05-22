from flask import Flask, render_template, url_for
import os
from dotenv import load_dotenv


def configure():
    load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('api_key')
app.config['UPLOAD_FOLDER'] = 'static/downloads'


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    configure()
    app.run(debug=True)
