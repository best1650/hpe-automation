# Robot Framework Interview Questions (Server Platform Integration Test Engineering)

These questions focus on using Robot Framework for keyword-driven automation in server environments.

## 1. What is Robot Framework and why is it used for HPE server integration testing?
**Answer:** Robot Framework is an open-source automation framework that uses a keyword-driven approach. It's ideal for server validation because it allows engineers (even those with less programming experience) to write tests in human-readable language. Its modular library system easily integrates with SSH, Redfish, and Selenium, making it the "gold standard" for cross-disciplinary platform testing at HPE.

## 2. Explain the difference between "Library" and "Resource" in Robot Framework.
**Answer:**
- **Library:** Usually a Python file or Java class that provides low-level keyword implementations (e.g., `RequestsLibrary`).
- **Resource:** A file (usually `.resource` or `.robot`) containing higher-level user-defined keywords, variables, and setting imports to be shared across multiple test suites.

## 3. How do you pass arguments to a keyword?
**Answer:** Arguments are passed in cells after the keyword name.
```robot
Login To iLO    ${USERNAME}    ${PASSWORD}
```

## 4. What are "Setup" and "Teardown," and why are they critical in platform testing?
**Answer:**
- **Setup:** Runs before a test/suite (e.g., opening a browser or initializing a Redfish session).
- **Teardown:** Runs after a test/suite (e.g., closing connections, collecting logs, or resetting server power).
Teardown is critical because it ensures the server is left in a "known good state" regardless of whether the test passed or failed.

## 5. How do you handle failure in Robot Framework?
**Answer:** By default, if a step fails, the test stops. However, you can use:
- `Run Keyword And Ignore Error`: Continues execution even if the keyword fails.
- `Run Keyword And Return Status`: Returns a boolean for logic checks.
- `Wait Until Keyword Succeeds`: Retries a keyword until it passes (useful for slow BIOS operations).

## 6. What are the different types of variables in Robot Framework?
**Answer:**
- `${SCALAR}`: Single value.
- `@{LIST}`: List of values.
- `&{DICTIONARY}`: Key-value pairs (excellent for Redfish JSON responses).

## 7. How do you implement data-driven testing in Robot Framework?
**Answer:** Use `Test Template`. This allows you to run the same test logic multiple times with different input data (e.g., testing multiple server SKU models with the same firmware update test).

## 8. What is the "BuiltIn" library?
**Answer:** A standard library that is always available. It provides essential keywords like `Log`, `Should Be Equal`, `Set Variable`, and `Run Keyword If`.

## 9. How do you interface Robot Framework with Python?
**Answer:** By creating a Python class or module. Methods in the Python class automatically become keywords in Robot Framework if the library is imported. This is how specialized HPE hardware libraries are usually integrated.

## 10. Explain "Variable Scopes" (Global, Suite, Test, Local).
**Answer:** 
- **Global:** Across all suites.
- **Suite:** Visible within the current file and its sub-suites.
- **Test:** Visible within one test case.
- **Local:** Only within a keyword.

## 11. How do you use "Tags" in Robot Framework?
**Answer:** Tags categorize tests (e.g., `Critical`, `Regression`, `BIOS`). They allow you to selectively run tests: `robot --include BIOS tests/`.

## 12. What is `Evaluate` keyword used for?
**Answer:** It allows executing Python expressions directly within Robot Framework. Useful for complex logic or math that doesn't have a specific keyword.

## 13. How do you handle conditional logic (`IF/ELSE`)?
**Answer:** Modern Robot Framework (v4.0+) uses native `IF`, `ELSE IF`, and `ELSE` blocks:
```robot
IF    "${status}" == "On"
    Power Off Server
ELSE
    Power On Server
END
```

## 14. What are "User Keywords"?
**Answer:** Keywords created by combining other keywords. They help in abstraction and making tests more readable (e.g., `Verify BIOS Settings After Update`).

## 15. How do you manage sensitive data like passwords?
**Answer:** Use `Variable Files` (YAML or Python) or command-line arguments (`--variable PASSWORD:secret`). In professional settings, integrating with a Secrets Vault (like HashiCorp) is best.

## 16. What is the `Wait Until Keyword Succeeds` keyword, and why is it useful for BIOS tests?
**Answer:** It retries a keyword for a specific duration. Useful for things like waiting for a server to finish POSTing or a firmware update to complete, which can take several minutes.

## 17. How do you generate reports and logs?
**Answer:** Robot automatically generates `output.xml`, `log.html`, and `report.html`. `log.html` provides detailed step-by-step execution details, while `report.html` gives a high-level summary.

## 18. What is a "Static" vs "Dynamic" library?
**Answer:** 
- **Static:** Keywords are mapped from method names.
- **Dynamic:** The library tells Robot at runtime which keywords it provides (using `get_keyword_names` etc.). Dynamic is used for very complex integrations.

## 19. Can you use Robot Framework for Parallel Execution?
**Answer:** Yes, using the `Pabot` tool. It splits tests across multiple processes, which is essential when validating a fleet of ProLiant servers simultaneously.

## 20. How do you organize a large test project?
**Answer:** 
- Separate logic into `Resources`.
- Separate data into `Data Files`.
- Use a directory-based suite structure.
- Follow naming conventions (Clear, descriptive keyword names).
