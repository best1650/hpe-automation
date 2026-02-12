# Selenium Interview Questions (Server Platform Integration Test Engineering)

These questions focus on using Selenium for UI automation of server management interfaces like HPE iLO.

## 1. What is Selenium, and how is it used in server validation?
**Answer:** Selenium is a suite of tools for automating web browsers. In server validation, it's used to test the BMC (Baseboard Management Controller) web interface (like iLO), ensuring that administrators can manually configure settings, monitor health, and view remote consoles via the web.

## 2. What are the different types of locators in Selenium?
**Answer:**
- ID (Most preferred, if unique)
- Name
- Class Name
- Tag Name
- Link Text / Partial Link Text
- CSS Selector
- XPath (Most flexible, used when others fail)

## 3. Why is "ID" the preferred locator for iLO UI automation?
**Answer:** IDs are usually unique and less likely to change compared to text or structure-based locators like XPath. This makes the tests more stable across different firmware versions.

## 4. Explain the difference between "Implicit Wait" and "Explicit Wait."
**Answer:**
- **Implicit Wait:** Sets a global timeout for the driver to wait for an element to appear.
- **Explicit Wait:** Tells the driver to wait for a *specific condition* (e.g., `element_to_be_clickable`) for a certain element. 
In iLO testing, Explicit Waits are better for handling slow-loading pages like the "Software & Firmware" inventory.

## 5. How do you handle "SSL Certificate Errors" in Selenium?
**Answer:** By using browser options. For Chrome:
```python
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
```
This is essential because iLO often uses self-signed certificates in test environments.

## 6. What is the Page Object Model (POM)?
**Answer:** It's a design pattern where each web page is represented as a class. It separates the page's locators and actions from the test logic, improving maintainability.

## 7. How do you handle alerts/pop-ups in Selenium?
**Answer:** Use `driver.switch_to.alert`. You can then use `.accept()`, `.dismiss()`, or `.text`. Useful for iLO prompts like "Confirm Reset."

## 8. How do you handle iframes?
**Answer:** Use `driver.switch_to.frame(id_or_name)`. BMC interfaces often use iframes for remote console windows or embedded applets.

## 9. What is "Fluent Wait"?
**Answer:** A type of wait that defines the maximum amount of time to wait for a condition, as well as the frequency with which to check it. It can also ignore specific exceptions (like `NoSuchElementException`).

## 10. How do you perform "Drag and Drop" or "Hover"?
**Answer:** Use the `ActionChains` class. Hover is common in modern responsive UIs like iLO 5/6 to reveal sub-menus.

## 11. How do you take a screenshot on failure?
**Answer:** `driver.get_screenshot_as_file("error.png")`. In server testing, screenshots are invaluable for recording the state of the UI during a crash or a configuration timeout.

## 12. Explain the difference between `/` and `//` in XPath.
**Answer:**
- `/`: Absolute path (from the root).
- `//`: Relative path (searches anywhere in the DOM).

## 13. How do you handle multiple windows or tabs?
**Answer:** Use `driver.window_handles` and `driver.switch_to.window(handle)`. This is common when clicking a "Launch Remote Console" button that opens in a new window.

## 14. What are "Shadow DOM" elements, and can Selenium interact with them?
**Answer:** Shadow DOM Encapsulates DOM nodes. Selenium can interact with them using JavaScript execution or by switching context in modern versions. iLO's dashboard widgets might use such technologies.

## 15. How do you execute JavaScript in Selenium?
**Answer:** Use `driver.execute_script("your_js_code")`. Useful for scrolling to an element or interacting with elements that are hidden by other transparent layers.

## 16. What is the "WebDriver Manager" library?
**Answer:** It automatically manages the download and setup of browser drivers (like `chromedriver`), ensuring the driver version matches the browser version.

## 17. How do you handle drop-down menus?
**Answer:** Use the `Select` class for `<select>` tags, or click-and-wait for custom div-based dropdowns common in modern UIs.

## 18. What is "Headless" mode?
**Answer:** Running the browser without a GUI. It's faster and uses fewer resources, making it ideal for CI/CD pipelines where you don't need to actually see the screen.

## 19. How do you verify if an element is displayed, enabled, or selected?
**Answer:** `.is_displayed()`, `.is_enabled()`, `.is_selected()`. 

## 20. How do you refresh a page?
**Answer:** `driver.refresh()`. Sometimes necessary after a server-side setting change to see the updated status on the iLO dashboard.
