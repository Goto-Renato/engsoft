import scrapy

class bairrosMaisPerigosos(scrapy.Spider):
    name = "bairrosMaisPerigosos"
    listaBairros = {}
    n = 0

    start_urls = [
        'http://www.ondefuiroubado.com.br/sao-carlos/SP/estatisticas'
    ]

    def parse(self, response):
        for bairros in response.css('div.ss-district-name'):
		self.listaBairros[self.n] = bairros.select("text()").extract()[0]
		self.n += 1
	yield self.listaBairros
