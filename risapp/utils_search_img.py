import json
import urllib2

from bs4 import BeautifulSoup

SEARCH_GOOGLE = {
    "url": "https://www.google.com/searchbyimage?&image_url=",
}

SEARCH_BING = {
    "url": "https://www.bing.com/images/search?q=imgurl:",
}


class ImageSearchUtil:
    def __init__(self):
        pass

    def search_google(self, link):
        soup = self.__fetch(SEARCH_GOOGLE.get("url") + link)
        results = self.__parse_results(soup)
        results['imgurl'] = link
        return results

    def __fetch(self, url):
        request = urllib2.Request(url)
        request.add_header('Accept-Encoding', 'utf-8')
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11')
        response = urllib2.urlopen(request)

        soup = BeautifulSoup(response, "html.parser")
        return soup

    def __parse_results(self, soup):
        results = {
            'title': '',
            'links': [],
            'descriptions': [],
            'titles': [],
            'similar_images': []
        }

        search_title = soup.find('div', attrs={'class': '_hUb'}).find('a').text
        results['title'] = search_title

        # for div in soup.findAll('div', attrs={'class': 'g'}):
        #     links = div.find('a')
        #     results['links'].append(links['href'])
        #
        # for desc in soup.findAll('span', attrs={'class': 'st'}):
        #     results['descriptions'].append(desc.get_text())
        #
        # for title in soup.findAll('h3', attrs={'class': 'r'}):
        #     results['titles'].append(title.get_text())

        for similar_image in soup.findAll('div', attrs={'rg_meta'}):
            tmp = json.loads(similar_image.get_text())
            img_url = tmp['ou']
            results['similar_images'].append(img_url)

        return results
