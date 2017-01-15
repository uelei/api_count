# -*- coding: utf-8 -*-
__author__ = 'wesleywwerneck'
import pytest
from api_count import exceptions
from api_count import utils


def test_word_count():
    """
        Unit test for method word count
    """
    word = "gol"

    text = """ kombi fusca gol corsa fiat uno Gol corrola"""

    count = utils.word_count(word, text, case_insensitive=True)

    assert count == 2

    count = utils.word_count(word, text, case_insensitive=False)

    assert count == 1


def test_checkurl():
    """
        Unit test to validate url
    """
    assert None == utils.check_url("http://blog.uelei.com")

    with pytest.raises(exceptions.InvalidUrl) as error_info:
        utils.check_url("salslallasldalslda:///dasda")

    assert error_info.value.to_dict() == {'error': 'Invalid url'}
