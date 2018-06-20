from httper import HTTP


# 在视图函数中平铺不是一个很好的习惯 所以新建一个类
class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        b1 = 'test'
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result
