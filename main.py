from flask import Flask, render_template, url_for, request
import os
import json
import wget
import shutil
import time
from werkzeug.routing import BaseConverter

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8000


class RegexConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.map = map
        self.regex = args[0]


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('api_key')
app.url_map.converters['regex'] = RegexConverter


@app.route('/home', methods=['get'])
@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/<regex(".*"):path>', methods=['put', 'get', 'head', 'delete'])
def upload(path):
    # Convert path
    path = str(path).replace('/', '\\')

    # Upload files with overwriting
    if request.method == 'PUT':
        pos = path.rindex('\\')
        file = path[pos + 1:]
        newPath = path[:pos]
        os.makedirs(newPath, exist_ok=True)
        dirr = os.getcwd()
        os.chdir(newPath)

        ffile = open(file, "w")
        ffile.close()

        os.chdir(dirr)
        return 'File created!'

    elif request.method == 'GET':
        # Extract file from path
        file = ''
        try:
            pos = str(path).rindex('\\')
            file = path[pos + 1:]
            if '.' not in file:
                file = ''
        except ValueError:
            ...

        # Download file
        if file:
            link = path.replace('\\', '/')
            wget.download('http://' + DEFAULT_HOST + ':' + str(DEFAULT_PORT) + '/' + link)
            return 'File successfully downloaded!'

        # Show all files in catalogue
        else:
            dirr = os.getcwd()
            os.chdir(path)
            files = json.dumps(os.listdir(os.getcwd()))
            os.chdir(dirr)
            return files

    # Show file info
    elif request.method == 'HEAD':
        file_stats = os.stat(os.getcwd() + '\\' + path)
        status = json.dumps(
            {'size': file_stats.st_size, 'last modified': time.ctime(os.path.getmtime(os.getcwd() + '\\' + path)),
             'create': time.ctime(os.path.getctime(os.getcwd() + '\\' + path)), 'permissions': file_stats.st_mode})
        return status

    # Delete selected file / catalogue
    elif request.method == 'DELETE':
        if '.' in path:
            os.remove(path=os.getcwd() + '\\' + path)

        else:
            shutil.rmtree(os.getcwd() + '\\' + path, ignore_errors=True)

        return 'Removed successfully!'


# Process 404 Error
@app.errorhandler(404)
def not_found(e):
    return '404 Not Found'


# Process 400 Error
@app.errorhandler(400)
def bad_request(e):
    return '400 Bad Request'


if __name__ == '__main__':
    app.run(DEFAULT_HOST, DEFAULT_PORT, debug=True, load_dotenv=True)
