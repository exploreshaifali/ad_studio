# About

# Setup

* Using Python 3.9.0
* Install virtualenvwrapper
* Create a new virtual environment `mkvirtualenv ad_studio`
* Install poetry inside virtual environment `pip install poetry`
* Clone the project, ad_studio `git clone https://github.com/exploreshaifali/ad_studio.git`
* cd to ad_studio `cd ad_studio`
* Install dependencies via poetry `poetry install`
* Run app server `uvicorn ad_studio.main:app --reload`

# Tests

Run test cases by running `pytest`.