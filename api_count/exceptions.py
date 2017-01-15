# -*- coding: utf-8 -*-

__author__ = 'wesleywwerneck'

import falcon


class BaseError(falcon.http_error.HTTPError):
    """ Base error for every exception"""
    def __init__(self, *args, **kwargs):
        falcon.http_error.HTTPError.__init__(self, *args, **kwargs)

    def to_dict(self, obj_type=dict):
        """ dict serializer"""
        message_error = {"status": "error"}
        return message_error


class InvalidUrl(BaseError):
    """ Exception for invalid url"""
    def __init__(self):
        BaseError.__init__(self, falcon.status_codes.HTTP_401)

    def to_dict(self, obj_type=dict):
        """ dict serializer"""
        message_error = {"error": "Invalid url"}
        return message_error

class ErrorGettingUrl(BaseError):
    """ Exception for erro getting url"""
    def __init__(self):
        BaseError.__init__(self, falcon.status_codes.HTTP_401)

    def to_dict(self, obj_type=dict):
        """ dict serializer"""
        message_error = {"error": "Coundn' fetch url content"}
        return message_error