import pytest
from selenium import webdriver

def setUp(request):
    """
    setup web driver
    :param request:
    :return:
    """
    driver = webdriver.Chrome