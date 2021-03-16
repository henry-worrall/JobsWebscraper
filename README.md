# Jobs Web Scraper

## Aim
This project aims to scrape job descriptions. This uses a package called selenium to interact with web pages. This has the advantage of being able to interact with web pages like a human does, i.e. by clicking on an element and loading different pieces of data. This is especially useful with modern websites which load content dynamically with JavaScript.

## Requirements
You will need to install the Python Selenium package and also a webdriver. I use the Google Chrome webdriver with this code, which allows selenium to load up Google Chrome and interact with web pages. You can download ChromeDriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). *Note that you will need to download the correct version of the webdriver so that it corresponds to the version of Google Chrome you have downloaded on your computer. The ChromeDriver executable file referenced in the main.py file under the PATH variable.*