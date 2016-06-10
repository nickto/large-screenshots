# Map extractor
This is a small python script to make screenshots of web-sites. It is called Map extractor, because there are some maps providers that make their maps available in web-based verions only, this allows to make screenshots of larger areas than fit onto a screen for more convenient use. Note that in some cases this might be illegal.

# Requirements
The script is writted in Python 3 and uses Selenium package with a PhantomJS driver. Therefore, the requirements are:

- Python 3
- Selenium
- PhantomJS

This repo contains short scripts for installing them on Ubuntu 15.10. 

1. Python 3 is already installed in standard Ubuntu.
2. To install Selenium, run `install-pip.sh`, which installs pip3. Then run `install-selenium.sh`, which installs Selenium for python, using pip3.
3. To install PhantomJS, run `install-phantomjs.sh`
