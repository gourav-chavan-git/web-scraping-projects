
import scrapy

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"]

    def parse(self, response):
        rows = response.xpath('//table[contains(@class, "wikitable")]/tbody/tr')

        for row in rows:
            location = row.xpath('.//td[1]/a/text() | .//td[1]/text()').get()
            population = row.xpath('.//td[2]/text()').get()
            world_percentage = row.xpath('.//td[3]/text()').get()
            date = row.xpath('.//td[4]/text()').get()
            date = row.xpath('.//td[4]').xpath('string(.)').get()
            source = row.xpath('.//td[5]/text()').get()

            if location and population:
                yield {
                    'Location': location.strip() if location else 'N/A',
                    'Population': population.strip() if population else 'N/A',
                    '% of World': world_percentage.strip() if world_percentage else 'N/A',
                    'Date': date.strip() if date else 'N/A',
                    'Source': source.strip() if source else 'N/A',
                }
