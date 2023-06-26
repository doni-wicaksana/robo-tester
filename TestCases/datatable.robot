
*** Test Cases ***    method    url
test    
    [Template]    Call api
    x    y
    m    d


*** Keywords ***
Call api
    [Arguments]    ${method}    ${url}
    Log To Console    ${method}${url}

