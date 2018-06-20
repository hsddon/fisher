# 在视图函数中平铺不是一个很好的习惯 所以新建一个类
class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{isbn}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def search_by_isbn(self, url):
        pass

    def search_by_keyword(self, url):
        pass
