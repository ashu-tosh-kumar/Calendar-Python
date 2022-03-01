# Calendar

This project aims to use Python as a back-end to build a sample Calendar application. We aim not to use any external library for any purpose except very native standard libraries like `logging` in Python etc.

The application accepts a date string in `YYYY-MM-DD` format and returns a calendar for that month filled with previous and/or next month dates to fulfill a `7x6` matrix.

For example, for the input `2022-01-31` , the calendar representation is below:

```
    S       M       T       W       T       F       S
    26     27      28       29      30      31      1
    2       3       4       5       6       7       8
    9       10      11      12      13      14      15
    16      17      18      19      20      21      22
    23      24      25      26      27      28      29
    30      31      1       2       3       4        5
```

## Tech Stack

1. Python for back-end
2. Flask for web server

## Features

1. The above date matrix is `7x6`
2. 100% unit test coverage

JavaScript version of this project: [Calendar-JS](https://github.com/ashu-tosh-kumar/Calendar-JS)


## Run Application
1. Working directory required: `Calendar-Python`
2. Run `python app.py`
3. Hit the REST End point `localhost:8080/{YYYY-MM-DD}`

## Run Tests
1. Working directory required: `Calendar-Python`
2. Run `python -m tests.{test-file-name-without-extension}`

## Check coverage of individual test file
1. Working directory required: `Calendar-Python`
2. Run `coverage run -m tests.{test-file-name-without-extension}`
3. Run `coverage html`
4. Check the generated html file at location `htmlcov\index.html`