#!/usr/bin/python3
import logging
import os
import time

import click
from selenium import webdriver


@click.command()
@click.argument("url", type=click.STRING)
@click.option("-o",
              "--output",
              type=click.STRING,
              required=True,
              help="Output file name.")
@click.option("-w",
              "--width",
              type=click.INT,
              required=False,
              default=4096,
              help="Width of the virtual screen.")
@click.option("-h",
              "--height",
              type=click.INT,
              required=False,
              default=2160,
              help="Height of the virtual screen.")
@click.option("-s",
              "--sleep",
              type=click.INT,
              required=False,
              default=5,
              help="Seconds to wait until the page is assumed to be loaded.")
@click.option("--pop-up",
              type=click.STRING,
              required=False,
              default=None,
              help="XPath of a button to close a popup.")              
@click.option("--log",
              type=click.Choice(["error", "warning", "info", "debug"],
                                case_sensitive=False),
              required=False,
              default="info",
              help="Seconds to wait until the page is assumed to be loaded.")
def screenshot(url, output, width, height, sleep, pop_up, log):
    """This script takes a screenshot of a page at URL.
    
    Example usage:

    ./screenshot.py --output=google.png --width=800 --height=600 --sleep=1 --log=debug "https://google.com"
    """
    # Set up logger
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging_levels = {
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG
    }
    logger = logging.getLogger("Screenshot")
    logger.setLevel(logging_levels[log.lower()])
    logger.debug("Script started.")

    # Create driver
    options = webdriver.FirefoxOptions()
    options.headless = True
    logger.debug("Starting Firefox browser.")
    driver = webdriver.Firefox(options=options)

    # Set up window size
    logger.debug(f"Setting screen size to {width:d}x{height:d}.")
    driver.set_window_size(width, height)

    # Load URL
    logger.debug(f"Loading {url:s}")
    driver.get(url)

    logger.info(f"Waiting {sleep:d} seconds for page to be assumed loaded.")
    time.sleep(sleep)

    # Click pop up if needed
    if pop_up:
        logger.info(f"Pop-up provider, clicking XPath {pop_up:s}.")
        driver.find_element_by_xpath(pop_up).click()
        logger.info(f"Waiting {sleep:d} seconds for page to be assumed loaded.")
        time.sleep(sleep)
    else:
        logger.debug("No pop up to close specified.")


    # Take and save screenshot
    logger.info(f"Saving screenshot to {output:s}.")
    driver.save_screenshot(output)
    driver.quit()
    logger.debug("Script finished.")


if __name__ == "__main__":
    screenshot()  # pylint: disable=no-value-for-parameter
