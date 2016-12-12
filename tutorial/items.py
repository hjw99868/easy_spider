import scrapy

class DmozItem(scrapy.Item):
    filmname = scrapy.Field()
    director = scrapy.Field()
    genre = scrapy.Field()
    num = scrapy.Field()
    link = scrapy.Field()
    score = scrapy.Field()
    year = scrapy.Field()
    commentnum = scrapy.Field()
    picture = scrapy.Field()
    actor = scrapy.Field()
    story = scrapy.Field()
    pass
