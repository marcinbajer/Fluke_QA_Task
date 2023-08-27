# Test Automation Task for FLUKE

This repository contains code for the automated test scenario for Google Search and verifying results.
Script code was created with Python and Pytest as a testing framework.

## How to Run Tests

1. Clone the repository with 'git clone https://github.com/marcinbajer/Fluke_QA_Task.git'
2. Install required dependencies: `pip install -r requirements.txt`
3. Run tests with: 'pytest' command in the terminal

## ADR (Architecture Decision Record)

**Tools**
- Programming language: Python
- Testing framework: Pytest, Selenium
- Browser Driver: ChromeDriver
- Architecture: Page Object Pattern

**Justification**
- Python is a popular and well-supported language with many test automation tools. Its syntax is easy to read for non-programmers as well.
- Pytest is one of the most popular testing frameworks for Pyton, and it's easy to use.
- Selenium is great library with very useful methods for the test automation purposes.
- ChromeDriver is a widely used browser driver that works with Selenium.
- Page Object Pattern is easy to develop and maintain. The architecture is easy to manage and readable. 

## Next Steps

If I had more time, I could:
- Add support for other browsers such as Firefox
- Create config file with environments variables
- Create test-data file with searching phrases or results to compare
- Configure tests to run in parallel on multiple browsers/devices
- Create more test scenarios such as checking the numbers of results, opening search results, using different test data, etc.
