**Tests for clients system**

Selenium tests for browsers: _chrome, firefox, IE_.

Project created with Page Object UI testing pattern.

The project is built on pytest + selenium and there are some small developments for connecting Allure

Example of running tests:
`pytest -s -v test_autorization_page.py --browser=ie`

Parameters:
 
 `--browser` `-B`:

    Chrome: `chrome`

    Firefox: `firefox`

    IE: `ie`

`--url` `-U`:
    
    URL for tests