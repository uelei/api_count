# -*- coding: utf-8 -*-

__author__ = 'wesleywwerneck'

import falcon
import json

from api_count import utils


class CountResource(object):
    """
    Count Resource to handle requests and output numbers of give word
    """

    def on_get(self, request, response):

        """
        Method get on /
        :param request: request object
        :param response: response object
        """
        url = request.get_param("url", True)

        word = request.get_param("word", True)

        case_sensitive = request.get_param_as_bool("ignore_case")
        if case_sensitive is None:
            case_sensitive = True

        utils.check_url(url)

        text = utils.request_url(url)

        count = utils.word_count(word=word, text=text,
                                 case_sensitive=case_sensitive)

        response.body = json.dumps({"url": url,
                                    "word": word,
                                    "count": count
                                    })


    def on_post(self, request, response):

        response.body = json.dumps({"ok": "ok"})



api = falcon.API()

api.add_route("/", CountResource())