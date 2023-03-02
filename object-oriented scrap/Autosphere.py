from Toolkit import Toolkit
from AutosphereEntry import AutosphereEntry
class Autosphere:
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = ["model", "price", "fuel", "counter", "release", "type"]

    def setPageMax(self, pageMax):
        self.nbPage = pageMax + 1
        return self
    
    def getLinks(self):
        for i in range(1, self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls

    def setEndpoints(self, soup):
        containers = soup.findAll("div", {"class" : "liste-fiches"})
        links = []
        for container in containers:
            divs = container.findAll("div", {"class" : "span4"})
            for div in divs:
                a = div.find("a", {"class" : "lien-fiche"})
                try:
                    links.append(a['href'])
                except:
                    pass
        self.endpoints.extend(links)
        return self.endpoints

    def getEndpoints(self):
        return self.endpoints

    def getFinalFieldNames(self):
        return self.finalFileNameFields

    def getInfoByPage(self, soup):
        fiches = []
        model = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"id" : "gtmModele"}))
        price = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"id" : "gtmPrice"}))
        fuel = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"id" : "gtmFuel"}))
        counter = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"id" : "gtmKm"}))
        release = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"id" : "gtmYear"}))
        type = Toolkit.tryToCleanOrReturnBlank(soup.find("span", {"id" : "gtmTransmission"}))
        fiche = AutosphereEntry(model, price, fuel, counter, release, type)
        fiches.append(fiche)
        self.result.extend(fiches)
        return fiches

    def getResult(self):
        return self.result

    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result