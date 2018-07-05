import scrapy

class SancaMobSpider(scrapy.Spider):
    name = "rocaImoveis"
    imoveis = {}
    n = 0

    start_urls = [
        'https://www.roca.com.br/busca?ord=DESC&codigo=&nome_end=&tab=universitarios&tipo=&cidade=2&bairro=&quartos=&banheiros=&garagens=&preco_min=&preco_max=',
        'https://www.roca.com.br/busca?ord=DESC&codigo=&nome_end=&tab=locacao&tipo=31&cidade=2&bairro=&quartos=&banheiros=&garagens=&preco_min=&preco_max=',
    ]

    def parse(self, response):
	imovelHXS = scrapy.selector.HtmlXPathSelector(response)
        for imovel in response.css('div.listing-item'):
		listaEndereco = imovel.select('//div[@class="listing-title"]')[0].select("text()").extract()[2].strip().split(" - ")
		if(listaEndereco[0] != 'Barrac\u00e3o'):
			caracteristicas = imovel.css('.listing-features li span::text').extract()
			self.imoveis[self.n] = {
				'tipo': imovel.css('.listing-badges span::text').extract_first().strip(),
#				'codigo': imovel.css('.listing-price i::text').extract_first().strip(),
				'preco': imovel.css('.listing-title h4::text').extract_first().strip()[3:].strip(),
				'link': response.urljoin(imovel.css('.listing-img-container::attr(href)').extract_first()),
				'area': (caracteristicas[0].strip())[0:-1],
				'quartos': (caracteristicas[1]).strip(),
				'banheiros': (caracteristicas[2]).strip(),
				'garagens': (caracteristicas[3]).strip(),
				'endereco': listaEndereco[2],
				'bairro': listaEndereco[1],
				'categoria': listaEndereco[0]
			}
			yield scrapy.Request(self.imoveis[self.n]["link"], dont_filter=False, callback=self.pegarEndereco, meta={'index': self.n})
		        self.n += 1
	for link in response.css('div.pagination-container nav.pagination ul li'):
		texto = link.css('a::text').extract_first().strip()
		if(texto != "" and texto != "<<" and texto != ">>" and link.css('a::attr(class)').extract_first() != "current-page"):
			yield scrapy.Request(link.css('a::attr(href)').extract_first(), dont_filter=False, callback=self.parse)
			self.paginas += 1
    def pegarEndereco(self, response):
	i = response.meta["index"]
	self.imoveis[i]['lat'] = response.css('#lat::attr(value)').extract_first()
	self.imoveis[i]['long'] = response.css('#lng::attr(value)').extract_first()
	self.imoveis[i]['descricao'] = response.css('.property-description p::text').extract_first().strip()
        yield self.imoveis[i]
