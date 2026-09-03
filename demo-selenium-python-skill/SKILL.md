---
name: demo-selenium-python
description: Explains and adapts the demo-selenium-python Selenium WebDriver walkthrough (locating elements by id/name/class/link-text/xpath, filling a text input, checking a checkbox/radio, selecting a dropdown option) against https://testingexamples.github.io; invoke when asked to run, explain, extend, or port this demo, or to adapt it to a different site or Selenium version.
---

This skill covers the `demo-selenium-python` repo: a small Python script
(`src/demo.py`) that teaches the core Selenium WebDriver locator strategies
(`By.ID`, `By.NAME`, `By.CLASS_NAME`, `By.LINK_TEXT`, `By.XPATH`) and the
basic form interactions (typing into a text input, checking a checkbox,
checking a radio button, selecting a dropdown option) against the public
demo site https://testingexamples.github.io.

To run it: install Python and pip, then `pip install selenium` and a
matching `chromedriver` on your `PATH` (see README.md's Install section),
then run `python3 src/demo.py`. It launches a visible local Chrome window,
prints the outer HTML of each located element, fills in the form, and
quits.

To adapt this demo to a different site: change the URL passed to
`driver.get(...)` and update every selector to match the new site's markup,
then update `spec/index.md` to match — the spec and the code must always
agree. To adapt to a newer `selenium` version: update the dependency and
re-check the `By`, `Select`, and `Options` APIs used here for breaking
changes; the locator and interaction sequence itself maps 1:1 to Selenium's
stable core API and is unlikely to need to change.

This skill summarizes the repo. `AGENTS.md` and `spec/index.md` are the
source of truth — if this skill's summary ever disagrees with those, they
win.
