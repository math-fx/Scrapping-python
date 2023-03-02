# ensure you have Python (3  or latest)
# ensure you have pip installer

from Scraper import Scraper
from Autosphere import Autosphere

# L'url du site que je souhaite Scraper
baseUrl = 'https://www.autosphere.fr/'
uri = "/recherche?market=VO&marque[]=DS&page="

autosphereInstance = Autosphere(baseUrl, uri, 16)

scraper = Scraper(autosphereInstance, "linksList.csv", "infos.csv")

scraper.exec()

print("Done")