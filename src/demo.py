#!/usr/bin/env python3

"""
Demo of Selenium browser automation with Python
Please see the file README.md for more information.

## Tracking

  * Package: demo-selenium-python
  * Version: 1.0.0
  * Created: 2026-09-03T00:00:00Z
  * Updated: 2026-09-03T00:00:00Z
  * License: GPL-2.0-or-greater or for custom license contact us
  * Contact: Joel Parker Henderson (joel@joelparkerhenderson.com)
"""

import sys

# Import Selenium WebDriver parts.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Import chromedriver options that you can set as you wish.
from selenium.webdriver.chrome.options import Options


def demo() -> None:
    """Walk through Selenium locator strategies and form interactions
    against https://testingexamples.github.io."""

    options = Options()
    options.add_argument('--verbose')  # Enable verbose logging.
    options.add_argument('--disable-notifications')  # Disable notifications such as popups.
    options.add_experimental_option(
        "prefs",
        {"profile.default_content_setting_values.cookies": 2},  # Reject cookies.
    )

    # Initialize the driver. Choose other browsers as you wish.
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to a website
        driver.get("https://testingexamples.github.io")

        ###
        # Find elements in various ways.
        ###

        # Find an element by id.
        #
        # This demonstrates `By.ID`.
        #
        # Example HTML:
        #
        #     <p id="id-example-1">Lorem Ipsum</p>
        #
        element_by_id = driver.find_element(By.ID, "id-example-1")
        print(element_by_id.get_attribute("outerHTML"))

        # Find an element by name.
        #
        # This demonstrates `By.NAME`.
        #
        # Example HTML:
        #
        #     <p name="name-example-1">Lorem Ipsum</p>
        #
        element_by_name = driver.find_element(By.NAME, "name-example-1")
        print(element_by_name.get_attribute("outerHTML"))

        # Find an element by class name.
        #
        # This demonstrates `By.CLASS_NAME`.
        #
        # Example HTML:
        #
        #     <p class="class-example-1">Lorem Ipsum</p>
        #
        element_by_class_name = driver.find_element(By.CLASS_NAME, "class-example-1")
        print(element_by_class_name.get_attribute("outerHTML"))

        # Find an element that is a link by its text.
        #
        # This demonstrates `By.LINK_TEXT`.
        #
        # Example HTML:
        #
        #     <a href="https://example.com">Link Example 1</a>
        #
        element_by_link_text = driver.find_element(By.LINK_TEXT, "Link Example 1")
        print(element_by_link_text.get_attribute("outerHTML"))

        # Find an element by XPath query.
        #
        # This demonstrates `By.XPATH`.
        #
        # Example HTML:
        #
        #     <input type=submit>
        #
        element_by_xpath = driver.find_element(By.XPATH, "//input[@type='submit']")
        print(element_by_xpath.get_attribute("outerHTML"))

        ###
        # Interact with form inputs in various ways.
        ###

        # Type in a text input.
        #
        # Example HTML:
        #
        #     <input type="text" id="text-example-1-id">
        #
        text = driver.find_element(By.ID, "text-example-1-id")
        print(text.get_attribute("outerHTML"))
        text.send_keys("hello")

        # Click a checkbox input.
        #
        # Example HTML:
        #
        #     <input type="checkbox" id="checkbox-example-1-id">
        #
        checkbox = driver.find_element(By.ID, "checkbox-example-1-id")
        print(checkbox.get_attribute("outerHTML"))
        checkbox.click()

        # Click a radio input.
        #
        # Example HTML:
        #
        #     <input type="radio" id="radio-example-1-option-1-id">
        #
        radio = driver.find_element(By.ID, "radio-example-1-option-1-id")
        print(radio.get_attribute("outerHTML"))
        radio.click()

        # Choose a select input option.
        #
        # Example HTML:
        #
        #     <select id="select-example-1-id">
        #       <option>alfa</option>
        #       <option>bravo</option>
        #       <option>charlie</option>
        #     </select>
        #
        select_element = driver.find_element(By.ID, "select-example-1-id")
        print(select_element.get_attribute("outerHTML"))
        select = Select(select_element)
        select.select_by_index(0)
        option = select.first_selected_option
        print(option.get_attribute("outerHTML"))

    except Exception as err:
        print(err)

    finally:
        driver.quit()


def main() -> None:
    """Main entry point with error handling."""
    try:
        demo()
    except Exception as err:
        print(f"Fatal error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
