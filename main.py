from flask import Flask, render_template, url_for, request
import os
from dotenv import load_dotenv
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        self.map = map
        self.regex = args[0]


def configure():
    load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('api_key')
app.config['UPLOAD_FOLDER'] = 'static/downloads'
app.url_map.converters['regex'] = RegexConverter


@app.route('/home', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/<regex(".*"):path>', methods=['put', 'get', 'head', 'delete'])
def upload(path):
    if request.method == 'PUT':
        path = str(path).replace('/', '\\')
        pos = path.rindex('\\')
        file = path[pos + 1:]
        path = path[:pos]
        file_path = os.path.join(path)
        os.makedirs(file_path, exist_ok=True)
        cat = os.getcwd()
        os.chdir(path)

        ffile = open(file, "w")
        ffile.close()

        os.chdir(cat)
        return 'File created!'




@app.errorhandler(404)
def not_found(e):
    return '404 Not Found'


@app.errorhandler(400)
def bad_request(e):
    return '400 Bad Request'


if __name__ == '__main__':
    configure()
    app.run(debug=True)
