*** Settings ***
Library   Browser
Library    ../Library/py/playwright_lib.py

Resource    browser_config.robot
Suite Setup    Settings Browser


*** Test Cases ***
Example Test
    Http    url
    Example Test

Example Test 2
    Example Test
    Go To    https://google.com
    

*** Keywords ***
Example Test
    New Page    https://playwright.dev
    Get Text    h1    contains    Playwright