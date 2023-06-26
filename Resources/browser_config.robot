*** Settings ***
Library    Browser
*** Keywords ***
Settings Browser
    New Browser    headless=${False}
    New Context    recordVideo={'size':{'width':1280, 'height':720}}
    Show Keyword Banner     True    top: 5px; bottom: auto; left: 5px; background-color: #00909077; font-size: 9px; color: black;   # Show banner on top left corner with custom styles
