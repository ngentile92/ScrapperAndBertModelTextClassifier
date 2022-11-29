# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from urllib import parse
from os import path
from scrapy.http.response.html import HtmlResponse

class NewsSpider(CrawlSpider):

    name = 'crawler_pagina12'
    # solo descargar paginas desde estos dominios
    allowed_domains = ('www.pagina12.com.ar','pagina12.com.ar')
    
    rules = (
        # solo bajar las paginas cuya url incluye "/secciones", pero no aquellas cuya url include "/catamarca12" o "/dialogo"
        # normaliza las urls para no descargarlas 2 veces la misma pagina con distinta url.
        Rule(LinkExtractor(allow=r'.+/secciones/.+',deny='.+(/catamarca12|/dialogo).+',
               deny_domains=['auth.pagina12.com.ar'], canonicalize=True,
               deny_extensions=['7z', '7zip', 'apk', 'bz2', 'cdr,' 'dmg', 'ico,' 'iso,' 'tar', 'tar.gz','pdf','docx', 'jpg', 'png', 'css', 'js']),
               callback='parse_response', follow=True),
     )
     
    # configuracion de scrappy, ver https://docs.scrapy.org/en/latest/topics/settings.html
    custom_settings = {
      # mentir el user agent
     'USER_AGENT': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
     'LOG_ENABLED': True,
     'LOG_LEVEL': 'INFO',
      # no descargar mas de 1 link desde la pagina de origen
     'DEPTH_LIMIT': 2,
      # ignorar robots.txt (que feo)
     'ROBOTSTXT_OBEY': False,
     # esperar entre 0.5*DOWNLOAD_DELAY y 1.5*DOWNLOAD_DELAY segundo entre descargas
     'DOWNLOAD_DELAY': 1
     'RANDOMIZE_DOWNLOAD_DELAY': True
    }

    def __init__(self, save_pages_in_dir='.', *args, **kwargs):
          super().__init__(*args, **kwargs)
          # guardar el directorio en donde vamos a descargar las paginas
          self.basedir = save_pages_in_dir
    
    def parse_response(self, response:HtmlResponse):
          """
          Este metodo es llamado por cada url que descarga Scrappy.
          response.url contiene la url de la pagina,
          response.body contiene los bytes del contenido de la pagina.
          """
          # el nombre de archivo es lo que esta luego de la ultima "/"
          print(type(response))
          html_filename = path.join(self.basedir,parse.quote(response.url[response.url.rfind("/")+1:]))
          if not html_filename.endswith(".html"):
              html_filename+=".html"
          print("URL:",response.url, "Pagina guardada en:", html_filename)
          with open(html_filename, "wt") as html_file:
              html_file.write(response.body.decode("utf-8"))
          

if __name__ == "__main__":
  crawler = CrawlerProcess()
  crawler.crawl(NewsSpider, save_pages_in_dir='.', start_urls = ['http://www.pagina12.com.ar/'])
  crawler.start()
 