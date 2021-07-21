import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//a[@class = "empresasSect" or @class = "alta-gerenciaSect" or @class = "economiaSect" or @class = "finansasSect" or @class = "empresasSect" or @class = "actualidadSect" or @class = "globoeconomiaSect" or @class = "editorial-opinionSect" or @class = "ocioSect" or @defaultSect]/@href'
XPATH_TITLE = '//div[@class = "mb-auto" or @class = "col order-2"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class= "lead"]/p/text()'
XPATH_BODY = '//div[@class = "html-content"]/p//text()'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            Home = response.content.decode('utf-8')
            parsed = html.fromstring(Home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)
def run():
    parse_home()

if __name__ == '__main__':
    run()



