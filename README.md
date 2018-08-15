# prices
This repo implements a flask app that delivers item prices from three major online shopping sites from India
using a selenium scrapper.

It has primarily three major components:
  - Python Selenium framework which wraps around the Webdriver to give Page classes having element objects. 
  More on this later.
  - Locators for prominent shopping site like Flipkart, Amazon and Snapdeal to navigate these websites 
  and scrap information
  - A Flask api that uses these features to carry out interactive real-time scraping
 
## Requirements:
Install all the required libraries by: 
```
$ pip install -r requirements.txt
```
It is recommended that you create a virtual environment for doing this.
For development purposes, you can also install the packages in requirements-test.txt

## Usage:
You can search for an item on three websites and get the results on a page.

Set the following variables in the configuration file: 
  - PATH: is the path to the browser driver 
    -   (for Firefox, it needs to be downloaded from [here](https://github.com/mozilla/geckodriver/releases))
  - BROWSER: browser type, typically firefox or chrome (not tested)
  - HEADLESS: boolean, whether to carry out the search in an open browser, True if headless
  - PAGE_LOAD_STRATEGY: 'normal', 'eager' or 'none', 'eager' recommended
  - TIMEOUT: waiting time for elements on a page
  - SEARCH_RESERVE: number of search results to be saved in the database

Setup the api as such:
```
$ chmod +x flask_db_setup
$ ./flask_db_setup
$ chmod +x flask_run
$ ./flask_run
```

Now open a browser and browse to: 
localhost:5000/

Framwork:
For getting to know the framework, please refer to main.py in the source directory for example usage.

The framework is structured into three major classes:
- Driver, which wraps around the Selenium webdriver
- Element, which map the elements on a page
- Page, this has the functionality to navigate to a URL, open links in new tab and holds the elements in it.

Please keep up for further enhancements.
