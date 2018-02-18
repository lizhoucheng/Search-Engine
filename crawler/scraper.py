import scrapy

# class BrickSetSpider(scrapy.Spider):
#     name = "brickset_spider"
#     start_urls = ['http://brickset.com/sets/year-2016']
#
#     def parse(self, response):
#         SET_SELECTOR = '.set'
#         for brickset in response.css(SET_SELECTOR):
#             NAME_SELECTOR = 'h1 a ::text'
#             PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
#             MINIFIGS_SELECTOR = './/dl[dt/text() = "minifigs"]/dd[2]/a/text()'
#             IMAGE_SELECTOR = 'img::attr(src)'
#             yield {
#                 'name': brickset.css(NAME_SELECTOR).extract_first(),
#                 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
#                 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
#                 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
#             }
#
#         NEXT_PAGE_SELECTOR = '.next a:: attr(href)'
#         next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#         if next_page:
#             yield scrapy.Request(
#                 response.urljoin(next_page),
#                 callback=self.parse
#             )


class MetaSpider(scrapy.Spider):
    name = "meta_spider"
    start_urls = ['http://www.metacritic.com/game/xbox-one/monster-hunter-world']

    def parse(self, response):
        TITLE_SELECTOR = '.game_content_head .product_title a span h1::text'
        META_RATING_SELECTOR = '.main_details .metascore_anchor div span::text'
        USER_RATING_SELECTOR = '.side_details .metascore_anchor div::text'
        CRITIC_REVIEW_SELECTOR = '.critic_reviews_module .review_body::text'
        title = response.css(TITLE_SELECTOR).extract_first()
        meta_score = response.css(META_RATING_SELECTOR).extract_first()
        user_score = response.css(USER_RATING_SELECTOR).extract_first()
        yield {
            'title': title,
            'meta_score': meta_score,
            'user_score': user_score
        }
        i = 1
        for critic_review in response.css(CRITIC_REVIEW_SELECTOR).extract():
            cr = ''.join(critic_review).strip();
            yield {
                'critic review ' + str(i): cr
            }
            i = i+1
