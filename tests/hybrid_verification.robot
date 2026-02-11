*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    Collections

*** Variables ***
${URL}             https://localhost:5000
${BROWSER}         chrome
${USERNAME}        admin
${PASSWORD}        password
${API_SYS_PATH}    /redfish/v1/Systems/1
${API_PWR_PATH}    /redfish/v1/Chassis/1/Power
${API_MGR_PATH}    /redfish/v1/Managers/1

*** Test Cases ***
Verify API and UI Consistency
    [Documentation]    Test to verify consistency between Redfish API data and Web UI
    # 1. Fetch data from Redfish API
    Create Session    ilo    ${URL}    verify=False
    ${resp_sys}=    GET On Session    ilo    ${API_SYS_PATH}
    ${resp_pwr}=    GET On Session    ilo    ${API_PWR_PATH}
    ${resp_mgr}=    GET On Session    ilo    ${API_MGR_PATH}
    
    ${api_name}=    Set Variable    ${resp_sys.json()['Name']}
    # Extracting PowerConsumedWatts from the first element of PowerControl list
    ${api_power}=   Set Variable    ${resp_pwr.json()['PowerControl'][0]['PowerConsumedWatts']}
    ${api_fw}=      Set Variable    ${resp_mgr.json()['FirmwareVersion']}

    Log    API Name: ${api_name}
    Log    API Power: ${api_power}
    Log    API Firmware: ${api_fw}

    # 2. Verify on UI via Selenium
    Open Browser To Login Page
    Login With Valid Credentials
    Verify Dashboard UI Data    ${api_name}    ${api_power}    ${api_fw}
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${options}    add_argument    --ignore-certificate-errors
    Call Method    ${options}    add_argument    --allow-insecure-localhost
    Open Browser    ${URL}    ${BROWSER}    options=${options}
    Maximize Browser Window
    Title Should Be    HPE iLO Login

Login With Valid Credentials
    Input Text      id=username    ${USERNAME}
    Input Password  id=password    ${PASSWORD}
    Click Button    id=loginButton

Verify Dashboard UI Data
    [Arguments]    ${expected_name}    ${expected_power}    ${expected_fw}
    Wait Until Page Contains Element    id=systemSummary    timeout=5s
    
    # Check System Name
    Element Text Should Be             id=sysName          ${expected_name}
    
    # Check Power Consumption (UI appends " W")
    Element Text Should Be             id=pwrConsumed      ${expected_power} W
    
    # Check Firmware Version
    Element Text Should Be             id=iloFirmware      ${expected_fw}
    
    Log    Hybrid verification successful: API and UI data matches.
