from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.web import book

#第三章完结版本，循环引用bug
if __name__ == '__main__':
    app.run()
