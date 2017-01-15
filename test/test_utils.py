# -*- coding: utf-8 -*-
__author__ = 'wesleywwerneck'

from api_count import utils

def test_word_count():

    word = "gol"

    text = """ kombi fusca gol corsa fiat uno Gol corrola"""

    count = utils.word_count(word, text, case_insensitive=True)

    assert count == 2

    count = utils.word_count(word, text, case_insensitive=False)

    assert count == 1


def test_checkurl():

    assert utils.check_url("http://blog.uelei.com")

    assert not utils.check_url("salslallasldalslda:///dasda")