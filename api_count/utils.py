# -*- coding: utf-8 -*-

__author__ = 'wesleywwerneck'

import requests
import validators

from api_count import exceptions


def word_count(word, text, case_sensitive):
    if case_sensitive:
        text = text.lower()
        word = word.lower()

    count = text.count(word)
    return count


def request_url(url):
    try:
        req = requests.get(url)
    except (requests.RequestException, requests.Timeout,
            requests.TooManyRedirects, requests.HTTPError):
        raise exceptions.ErrorGettingUrl()

    return req.text


def check_url(url):
    if not validators.url(url):
        raise exceptions.InvalidUrl()
