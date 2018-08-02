"""
This file holds the configuration to be used in the entire module
:param PATH: is the path to the browser driver
:param BROWSER: browser type, typically firefox or chrome (not tested)
:param HEADLESS: boolean, whether to carry out the search in an open browser, True if headless
:param PAGE_LOAD_STRATEGY: 'normal', 'eager' or 'none', 'eager' recommended
:param TIMEOUT: waiting time for elements on a page
"""
PATH = '/home/vivek/PycharmProjects/selenium_project/geckodriver_loc/geckodriver'
BROWSER = 'Firefox'
HEADLESS = False
PAGE_LOAD_STRATEGY = 'eager'
TIMEOUT = 10
