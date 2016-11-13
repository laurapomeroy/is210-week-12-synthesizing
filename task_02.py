#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom exception class"""


class CustomError(Exception):
    """Cusom Error class

    Args:
        message(optional): a message.
        cause(optional): a cause.
    """
    def __init__(self, message, cause):
        Exception.__init__(self, message)
        self.cause = cause
