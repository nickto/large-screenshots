# Map extractor
This is a small python script to make screenshots of web-sites. It is called Map extractor, because there are some maps providers that make their maps available in web-based verions only, this allows to make screenshots of larger areas than fit onto a screen for more convenient use. Note that in some cases this might be illegal.

# Requirements
The script is writted in Python 3 and uses Selenium package with a PhantomJS driver. Therefore, the requirements are:

- Python 3
- Selenium
- Firefox 
- Firefox WebDriver (geckodriver)

## Firefox and Selenium
```
apt install python-pip firefox
pip install selenium
```

## Firefox WebDriver
1. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases)
2. Add it to PATH (as shown [here](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu))

## Running Firefox headlessly
Follow suggestions from [here](http://agiletesting.blogspot.se/2016/01/running-selenium-webdriver-tests-using.html):
1. Install xvfb: `apt install Xvfbq`
2. Start it at display 10: `Xvfb :10 -ac &`
3. Set display to 10: `export DISPLAY=:10`
4. Now run this script from the same terminal


