# Advent of Code 2021

It's that time of year again. Featuring:

* Python 3.10 - let's do some pattern matching!
* Golang 1.16 - cause that's what's in Fedora 35's repos. And it's awesome.

## Python conventions
* Code formatted with `black` (with one exception: line length == 120 because 21:9 gaming monitor).
* 10/10 Pylint with as few exceptions as possible.
* Only Python code goes in the `aoc2021` folder. All puzzle input is saved in fixtures.
* Everything should be runnable as a module from within the `python` folder - e.g. `python -m aoc2021.day1`
* Remember that your input is not necessarily going to match mine. That being said, tests will contain spoilers. Tread carefully.