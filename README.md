The scope of this application is to test the search functionalities of the emag.ro website.

Prerequisites

To run the application, you need python 3.12, behave and selenium

1. python 3.12 
You need to have Python installed, at least the version 3.12. Check if you already have Python installed by running the Terminal command: python --version. If you can see the version number, then Python is already installed. If you can't see the version number, then you have to download here https://www.python.org/downloads/
2. behave
behave is a library that allows the definition and execution of test scenarios, using the Gherkin syntax, which is a behave-driven-development(BDD) language. You can check if you have already installed behave by running the Terminal command: behave --version. If the result shows a version number, behave is installed and there is no need for further actions. If not, instructions for downloading the latest version of behave can be installed by accessing Manage packages, then search by "behave" and click on install.
3. selenium
Selenium is a suite of tools for automating web browsers.It's primarily used for automated testing of web applications but can also be utilized to automate repetitive tasks in the browser or to extract data from web pages. You can install selenium by typing pip install selenium in command.

The application goes to the emag.ro website, it searches any inputted word, such as 'iphone', and it shows all the results that have been found on the website.
In order to get a report for the run tests, you can use the Terminal command behave -f html -o behave-report.html

![raport executie](D:\Prezentare\Proiect final\pythonProject3\raport.png)

