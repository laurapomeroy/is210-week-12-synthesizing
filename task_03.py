#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


def exception_test(arg1, arg2, arg3):
    """Exception clause

    Args:
        caught (bool): False if there is no error.

    Returns:
        caught (bool): returns True if an error is found.

    Examples:
        >>> exception_test(['apple'], 0, 'p')
        False
        >>> exception_test(43, 1, 1)
        True
    """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, LookupError):
        caught = True

    return caught
