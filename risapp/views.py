# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .clarifai_utils import ClarifaiUtil
from .utils_search_img import ImageSearchUtil


def home(request):

    results = {
        'list': [
            {'url': "http://cfile7.uf.tistory.com/image/26663633550EB8BC1BCD74", 'title': "지성 - 너무 잘 생김.. >.<", 'type': 'S1'},
            {'url': "http://img.lifestyler.co.kr/uploads/program/cheditor/2017/03/I9Y2C6KR4CRG6EBONN1S.jpg", 'title': "터널 - 요즘 완전 잼있음 ㅎ", 'type': 'S1'},
            {'url': "http://www.zenithnews.com/news/photo/201603/34953_33450_2129.jpg", 'title': "윤현민 - 야구선수 출신 배우 ㅎ 존잘생김 ㅎㅎ", 'type': 'S1'},
            {'url': "http://image.chosun.com/sitedata/image/201703/22/2017032202141_0.jpg", 'title': "이유영 - 새로 발견한 배우..근데 김주혁이랑 열애(17살차이..ㅎㄷㄷ)", 'type': 'S1'},
            {'url': "https://scontent.cdninstagram.com/hphotos-xpf1/t51.2885-15/e15/11176024_821896324572130_1104310486_n.jpg", 'title': "커피빈", 'type': 'S2'},
            {'url': "http://image.auction.co.kr/itemimage/86/fd/61/86fd61c05.jpg", 'title': "탐앤탐스", 'type': 'S2'},
            {'url': "http://www.giftishow.com/Resource/goods/G00000008066/G00000008066.jpg", 'title': "스타벅스", 'type': 'S3'},
            {'url': "http://image.ytn.co.kr/general/jpg/2017/0316/201703161720067326_d.jpg", 'title': "스타벅스 여러개~", 'type': 'S2'},
        ]
    }
    return render(request, 'index.html', {'results': results})


@require_http_methods(["GET", "POST"])
def search(request):
    img_url = request.GET.get('q')

    if not img_url:
        img_url = "http://cfile30.uf.tistory.com/image/246CCB3F57E7C7A30ECA08"

    search_util = ImageSearchUtil()
    results = search_util.search_google(img_url)
    return render(request, 'search_result.html', {'results': results})


def search_by_clarifai(request):
    img_url = request.GET.get('q')

    results = []
    if img_url:
        util = ClarifaiUtil()
        results = util.search_by_image(img_url)
        # results['concepts'] = util.predict(link)

    return render(request, 'search_result_related.html', {'results': results})


def search_by_predicted_concepts(request):
    concept_word = request.GET.get('q')

    results = []
    if concept_word:
        util = ClarifaiUtil()
        results = util.predict_concepts(concept_word)

    return render(request, 'search_result_concepts.html', {'results': results})


def predict_by_clarifai(request):
    img_url = request.GET.get('q')

    results = []
    if img_url:
        util = ClarifaiUtil()
        results = util.predict(img_url)
        results['imgurl'] = img_url

    return render(request, 'search_result_predict.html', {'results': results})


def about(request):
    return render(request, 'about.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def contact(request):
    return render(request, 'contact.html', {})
