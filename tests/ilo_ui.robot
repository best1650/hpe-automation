*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}             http://localhost:5000
${BROWSER}         chrome
${USERNAME}        admin
${PASSWORD}        password

*** Test Cases ***
Verify iLO Login And Dashboard
    [Documentation]    Test to verify login and dashboard accessibility
    Open Browser To Login Page
    Login With Valid Credentials
    Verify Dashboard Loaded
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    Open Browser    ${URL}    ${BROWSER}    options=${options}
    Maximize Browser Window
    Title Should Contain    HPE iLO

Login With Valid Credentials
    Input Text      id=username    ${USERNAME}
    Input Password  id=password    ${PASSWORD}
    Click Button    id=loginButton

Verify Dashboard Loaded
    Wait Until Page Contains Element    id=systemSummary    timeout=5s
    Element Text Should Be             id=sysName          HPE ProLiant DL380 Gen10
    Element Text Should Be             id=healthStatus     OK
    Log    Successfully logged in and verified dashboard
