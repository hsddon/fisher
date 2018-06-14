from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q,page):
    '''
        q:普通关键字
        page
    :return:
    '''
    #isbn isbn13 13个0到9的数字
    #isbn10 10个0到9的数字组成含义一些"-"
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key == 'isbn'
    short_q = q.replace('-','')
    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        isbn_or_key = 'isbn'


    pass


if __name__ == '__main__':
    app.run()
