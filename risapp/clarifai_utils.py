from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

API_KEY_GENERAL = {
    "key": "Ntxz6TD39ZmrA1F_ZBdWoxMe6jRF9fpsUExFA9QY",
    "secret": "yUFrUfI74DGN51Ced-1qHD_iwjiR3HPvzf_wwqZH",
    "model": 'general-v1.3'
}

API_KEY_FOOD = {
    "key": "b2iRfMcCFsrrqb2tcijSdNi5PzQoCfeEcNNqi4zB",
    "secret": "C1MeAxnMJ4d1YvHEDZnVXA_G82G9MsBgYi11Qb97",
    "model": "food-items-v1.0"
}

SIMILAR_SCORE_THRESHOLD = 0.6


class ClarifaiUtil(object):
    clarifai_app = object

    def __init__(self):
        self.clarifai_app = ClarifaiApp(API_KEY_FOOD.get("key"), API_KEY_FOOD.get("secret"))
        pass

    def search_by_image(self, link, score_threshold=SIMILAR_SCORE_THRESHOLD):
        search_result = self.clarifai_app.inputs.search_by_image(url=link)
        results = self.__parse_similar_images(search_result, score_threshold)
        results['title'] = link
        return results

    def __parse_similar_images(self, search_result, score_threshold):
        results = {
            'title': '',
            'links': [],
            'descriptions': [],
            'titles': [],
            'similar_images': []
        }

        for a_item in search_result:
            if a_item.score > score_threshold:
                results['similar_images'].append({"url": a_item.url, "score": a_item.score})

        return results

    def predict(self, link):
        model = self.clarifai_app.models.get(API_KEY_FOOD.get("model"))
        image = ClImage(url=link)
        search_result = model.predict([image])
        results = self.__parse_data(search_result['outputs'])
        return results

    def __parse_data(self, result):
        results = {'concepts': result[0]['data']['concepts']}

        return results

    def predict_concepts(self, concept):
        search_result = self.clarifai_app.inputs.search_by_predicted_concepts(concepts=concept.split(','))
        results = self.__parse_concepts(search_result, concept)
        return results

    def __parse_concepts(self, result, concepts):
        results = {
            'title': concepts,
            'links': [],
            'descriptions': [],
            'titles': [],
            'similar_images': []
        }

        for a_item in result:
            results['similar_images'].append({"url": a_item.url, "score": a_item.score})

        return results
