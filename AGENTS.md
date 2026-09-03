# Agent instructions: demo-selenium-python

Demo Selenium Python is a small beginner walkthrough script that uses
Selenium WebDriver (with ChromeDriver) to demonstrate locating elements on
https://testingexamples.github.io by id, name, class name, link text, and
XPath, then filling a text input, checking a checkbox, checking a radio
button, and selecting an option from a dropdown.

`spec/index.md` is the single source of truth for the exact scenario this
demo walks through: the target URL, every selector/locator used, and the
expected values. If the code in `src/demo.py` and `spec/index.md` ever
disagree, that is a defect in one of them — fix it before doing anything
else.

For how to install dependencies and run the script, see the Install and Run
sections in `README.md` rather than duplicating those steps here.

Non-negotiable: this repo is a walkthrough script, not a test suite. It uses
`print` to show what it found, not assertions. Do not add strict pass/fail
assertions or convert this into a test framework — that would change what
the demo is for. (For assertion-based Selenium/Python demos, see the
sibling repos `demo-selenium-python-for-nhs-wales`,
`demo-selenium-python-for-google-search`, and
`demo-selenium-python-for-google-maps`.)

CLAUDE.md is a pointer to this file — it is the single source of truth for
agent instructions.
