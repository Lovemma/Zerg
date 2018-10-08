# -*- coding: utf-8 -*-

from flask import json, request
from werkzeug.exceptions import HTTPException as _HTTPException


class HTTPException(_HTTPException):
    code = 500
    msg = '服务器内部错误!'
    results = []

    def __init__(self, msg=None, code=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        super(HTTPException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = {
            'code': self.code,
            'msg': self.msg,
            'request_url': request.url
        }
        return json.dumps(body)

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]


