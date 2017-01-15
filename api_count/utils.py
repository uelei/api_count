# -*- coding: utf-8 -*-

__author__ = 'wesleywwerneck'

import requests
import validators

from api_count import exceptions


def word_count(word, text, case_insensitive):
    """ Count word for a given text"""
    if case_insensitive:
        text = text.lower()
        word = word.lower()

    count = text.count(word)
    return count


def request_url(url):
    """" Request the given url and return it's text"""
    try:
        req = requests.get(url)
    except (requests.RequestException, requests.Timeout,
            requests.TooManyRedirects, requests.HTTPError):
        raise exceptions.ErrorGettingUrl()

    return req.text


def check_url(url):
    """" Check if url is valid"""
    if not validators.url(url):
        raise exceptions.InvalidUrl()
