# prices
This repo implements a selenium scrapper to get prices for an item from three major online shopping sites from India

It has primarily three major components:
  - Python Selenium framework which wraps around the Webdriver to give Page classes having element objects. More on this later.
  - Locators for prominent shopping site like Flipkart, Amazon and Snapdeal to navigate these websites and scrap information
  - A Flask api that uses these features to carry out interactive real-time scraping
 
 How to use:
 clone this repo using the command:
 
 git clone https://github.com/vivekadishankara/prices.git
 
 enter the prices folder and run the command:
 
 pip install -r requirements.txt
 
 This install all the required libraries. 
 
 Currently the major functionality is searching for an item on any of the websites and presenting the results. 
 Please refer to main.py in the source directory for an example usage.
 
 The framework is structured into three major classes:
  - Driver, which wraps around the Selenium webdriver
  - Element, which map the elements on a page
  - Page, this has the functionality to navigate to a URL, open links in new tab and holds the elements in it.
 
 The Flask API is under construction. Please keep up for further enhancements.
