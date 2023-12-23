#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker"""

import requests


def get_page(url: str) -> str:
    """Gets the HTML content of a web page"""
    req = requests.get(url)
    

    return req.text