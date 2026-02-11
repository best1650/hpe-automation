*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://localhost:5000
${REDFISH_PATH}    /redfish/v1/Systems/1

*** Test Cases ***
Verify Redfish System Information
    [Documentation]    Test to verify system information from Redfish API
    Create Session    ilo    ${BASE_URL}    verify=False
    ${resp}=    GET On Session    ilo    ${REDFISH_PATH}
    Status Should Be    200    ${resp}
    
    ${json}=    Set Variable    ${resp.json()}
    Should Be Equal As Strings    ${json['Manufacturer']}    HPE
    Should Be Equal As Strings    ${json['Model']}           ProLiant DL380 Gen10
    Should Be Equal As Strings    ${json['Status']['Health']}    OK
    Log    System Health is: ${json['Status']['Health']}
