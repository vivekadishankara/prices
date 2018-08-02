# prices
This repo implements a selenium scrapper to get prices for an item from three major online shopping sites from India

It has primarily three major components:
  - Python Selenium framework which wraps around the Webdriver to give Page classes having element objects. More on this later.
  - Locators for prominent shopping site like Flipkart, Amazon and Snapdeal to navigate these websites and scrap information
  - A Flask api that uses these features to carry out interactive real-time scraping
 
Usage:
clone this repo using the command:

git clone https://github.com/vivekadishankara/prices.git

enter the prices folder and run the command:

pip install -r requirements.txt

This install all the required libraries. It is recommended that you create a virtual environment before doing this.

Currently the only functionality is searching for an item on the three websites and presenting the results on a common page.
setup the api as such:
export FLASK_APP=/<path to repo>/prices/api
flask run

Set the following variables in the configuration file: (note the browser driver needs to be downloaded)
  - PATH: is the path to the browser driver
  - BROWSER: browser type, typically firefox or chrome (not tested)
  - HEADLESS: boolean, whether to carry out the search in an open browser, True if headless
  - PAGE_LOAD_STRATEGY: 'normal', 'eager' or 'none', 'eager' recommended
  - TIMEOUT: waiting time for elements on a page

Now open a browser and browse to: 
localhost:5000/

Framwork:
For getting to know the framework, please refer to main.py in the source directory for example usage.

The framework is structured into three major classes:
- Driver, which wraps around the Selenium webdriver
- Element, which map the elements on a page
- Page, this has the functionality to navigate to a URL, open links in new tab and holds the elements in it.

The Flask API is under construction. Please keep up for further enhancements.
