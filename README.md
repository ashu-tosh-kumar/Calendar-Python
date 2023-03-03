# Calendar

- [Calendar](#calendar)
  - [Introduction](#introduction)
  - [Tech Stack](#tech-stack)
  - [Salient Features](#salient-features)
  - [Run Application](#run-application)
  - [Run Tests](#run-tests)
  - [Check Coverage](#check-coverage)

## Introduction

This project aims to showcase the development of a production grade project. We are building an utility to return calendar for respective month for given input date. We have used `Flask` as back-end library and `gunicorn` as web server using `Python`. We aim not to use any external library for any purpose except very native standard libraries. We have written unit-tests using standard `unittest` library.

The application accepts a date string in `YYYY-MM-DD` format and returns a calendar for that month filled with previous and/or next month dates to fulfill a `7x6` matrix.

For example, for the input `2022-01-31` , the calendar representation is below:

```text
    S       M       T       W       T       F       S
    26     27      28       29      30      31      1
    2       3       4       5       6       7       8
    9       10      11      12      13      14      15
    16      17      18      19      20      21      22
    23      24      25      26      27      28      29
    30      31      1       2       3       4        5
```

## Tech Stack

1. Python as programming language
2. Flask for api development
3. Gunicorn as web server
4. Docker to containerize the application

## Salient Features

1. The above date matrix is `7x6`
2. 100% unit test coverage

JavaScript version of this project: [Calendar-JS](https://github.com/ashu-tosh-kumar/Calendar-JS)

## Run Application

1. Install Docker along with Docker Compose
2. `docker compose build`
3. `docker compose up -d`

## Run Tests

1. Working directory required: `Calendar-Python`
2. Run `python -m tests.{test-file-name-without-extension}`

## Check Coverage

1. Working directory required: `Calendar-Python`
2. Run `coverage run -m tests.{test-file-name-without-extension}`
3. Run `coverage html`
4. Check the generated html file at location `htmlcov\index.html`
