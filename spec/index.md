# Spec: demo-selenium-python

## Summary

This spec describes the exact Selenium WebDriver walkthrough that
`src/demo.py` performs against https://testingexamples.github.io/en-001/practice/.

## Scope

This spec covers the demo script's target site, every locator it uses, and
every form interaction it performs, so that the code and this document can
be checked against each other.

This spec does not cover installing Python, Selenium, or ChromeDriver, or
troubleshooting driver/browser version mismatches — see `README.md` for
that.

## Principles and rules

* This is a walkthrough script, not a test suite. It demonstrates locator
  strategies and form interactions by printing HTML with `print`; it does
  not make assertions.
* The script targets exactly one page: https://testingexamples.github.io/en-001/practice/.

## Detail

Target URL: `https://testingexamples.github.io/en-001/practice/`

Locators (verbatim from `src/demo.py`):

1. `By.ID, "id-example-1"` — finds `<p id="id-example-1">Lorem Ipsum</p>`,
   demonstrates `By.ID`.
2. `By.NAME, "name-example-1"` — finds
   `<p name="name-example-1">Lorem Ipsum</p>`, demonstrates `By.NAME`.
3. `By.CLASS_NAME, "class-example-1"` — finds
   `<p class="class-example-1">Lorem Ipsum</p>`, demonstrates
   `By.CLASS_NAME`.
4. `By.LINK_TEXT, "Link Example 1"` — finds
   `<a href="https://example.com">Link Example 1</a>`, demonstrates
   `By.LINK_TEXT`.
5. `By.XPATH, "//input[@type='submit']"` — finds `<input type=submit>`,
   demonstrates `By.XPATH`.

Form interactions (verbatim from `src/demo.py`):

* Text input: `By.ID, "text-example-1-id"`, then `send_keys("hello")`.
* Checkbox: `By.ID, "checkbox-example-1-id"`, then `click()`.
* Radio button: `By.ID, "radio-example-1-option-1-id"`, then `click()`.
* Select: `By.ID, "select-example-1-id"`, then
  `Select(select_element).select_by_index(0)`, then
  `select.first_selected_option`.

## Acceptance criteria

This demo still works when: the script completes without raising, and every
locator resolves — each `find_element` call succeeds and each `print` shows
real `outerHTML` rather than an error.

## Related topics

* [../README.md](../README.md)
* [../AGENTS.md](../AGENTS.md)

## Sources

* <https://testingexamples.github.io/en-001/practice/>
