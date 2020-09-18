# arXiv API Gateway

This project pulls together documentation (including specifications) for the
arXiv API Gateway. The intended audience is arXiv API users, including partner
platforms.

Documentation for individual services is maintained in the respective
repositories for those services. This project largely involves pulling down
those docs into a single resource, which is then published as (almost) static
pages.

## Running for development

1. Install dependencies

```bash
pipenv install
```

2. Build the site index

```bash
pipenv run python build.py
```

3. Run the Flask development server

```bash
LOGLEVEL=10 FLASK_APP=app.py pipenv run flask run
```

You should find the root page at http://127.0.0.1:5000

## TODO:

- [ ] Automate pulling down the latest version of each API's schema
- [ ] Polish styling; make CSS in templates not hard-coded (shame shame).
- [ ] Maybe it would be better to implement the OpenAPI rendering bit as a
  Python-markdown plugin?
