# DevFinder Selenium Testing

## Introduction

This is a testing project for the DevFinder project. It uses Selenium to test the functionality of the DevFinder website.

## Installation

Clone the project:
```
git clone https://github.com/Bit-Lords-1000101/DevFinder-Selenium-Testing.git
```

Install the dependencies:
```
cd DevFinder-Selenium-Testing
pip install -r requirements.txt
```

## Usage

Create .env config file in the root folder:
```
DEVFINDER_USERNAME = <username>
DEVFINDER_PASSWORD = <password>
```

Run the tests:
```
python tests.py
```

Run the tests with the streamlit app:
```
streamlit run app.py
```