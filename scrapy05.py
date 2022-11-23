import scrapy


class QuotesSpider(scrapy.Spider):
    name = "honda"
    start_urls = [
        'https://www.sanook.com/auto/tag/honda:city/',
    ]

    def parse(self, response):
        for quote in response.css('div.row'):
            yield {
                'headline': quote.css('h3::text').get(),
                'detail': quote.css('p::text').get(),
                'date': quote.css('jsx-1818055635 text"::text').get(),
                'viewers': quote.css('jsx-1818055635 text::text').get(),
            }

        next_page = response.css('a./tags/honda-honda/3').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        df = pd.DataFrame(zip(title.article), columns = ['headline','detail', 'date', 'viewers'])
        print(df)