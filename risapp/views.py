# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .clarifai_utils import ClarifaiUtil
from .utils_search_img import ImageSearchUtil

from .models import MainImage


def home(request):
    results = {
        'list': MainImage.objects.all()
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
