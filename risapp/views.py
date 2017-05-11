import json
import urllib2

from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from clarifai.rest import ClarifaiApp

SEARCH_URL = 'https://www.google.com/searchbyimage?&image_url='


def home(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):
    return render(request, 'contact.html', {})


@require_http_methods(["GET", "POST"])
def search(request):
    # client_json = json.loads(request.body)
    # soup = fetch(client_json['image_url'])
    link = request.GET.get('q')

    if not link:
        link = "http://mblogthumb4.phinf.naver.net/20160906_59/jihye3682_1473143270909nq1TO_JPEG/image_3230629031473143042075__IMG_0027.jpg?type=w800"

    soup = fetch(SEARCH_URL + link)
    results = parse_results(soup)
    return render(request, 'search_result.html', {'results': results})


def parse_results(soup):
    results = {
        'title': '',
        'links': [],
        'descriptions': [],
        'titles': [],
        'similar_images': []
    }

    search_title = soup.find('div', attrs={'class': '_hUb'}).find('a').text
    results['title'] = search_title

    for div in soup.findAll('div', attrs={'class': 'g'}):
        links = div.find('a')
        results['links'].append(links['href'])

    for desc in soup.findAll('span', attrs={'class': 'st'}):
        results['descriptions'].append(desc.get_text())

    for title in soup.findAll('h3', attrs={'class': 'r'}):
        results['titles'].append(title.get_text())

    for similar_image in soup.findAll('div', attrs={'rg_meta'}):
        tmp = json.loads(similar_image.get_text())
        img_url = tmp['ou']
        results['similar_images'].append(img_url)

    return results


def fetch(url):
    request = urllib2.Request(url)
    request.add_header('Accept-Encoding', 'utf-8')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11')
    response = urllib2.urlopen(request)

    soup = BeautifulSoup(response, "html.parser")
    return soup


def search_by_clarifai(request):
    link = request.GET.get('link')
    try:
        app = ClarifaiApp("Ntxz6TD39ZmrA1F_ZBdWoxMe6jRF9fpsUExFA9QY", "yUFrUfI74DGN51Ced-1qHD_iwjiR3HPvzf_wwqZH")

        search_result = app.inputs.search_by_image(url=link)
        results = parse_result_clarifai(search_result)
        return render(request, 'search_result.html', {'results': results})
    except:
        return HttpResponseServerError()


def parse_result_clarifai(result):
    results = {
        'title': '',
        'links': [],
        'descriptions': [],
        'titles': [],
        'similar_images': []
    }

    for a_item in result:
        results['similar_images'].append(a_item.url)

    return results
