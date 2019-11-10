# Hacker News Scraper Test
---

*A [`python`][python] & [`requests`][requests]-based [Hacker News][hn] scraper.*

## Introduction

hackernews is a simple, dockerised [`python`][python] scraper that pulls top stories using the [Hacker News][hn] API and parses key info into JSON format.

## Usage Guide

hackernews requires Docker to be configured on your system in order to run. [Docker Installation Guide][dockerinstall]

### Download Local Copy

Once Docker is  installed and configured you can download a copy of this docker image using the following command.

```bash
$ docker pull lxdesign/hackernews[:v1]
```
### How to Run

To run hacker news use the following command:

```bash
$ docker run -v [OUTPUT_FILEPATH]:/src hackernews --posts [NUMBER_OF_POSTS]
```
Replace **[OUTPUT_FILEPATH]** with the **full path** to write the JSON output to e.g.
```
Users/lx/hackernews/result
```

Replace **[NUMBER_OF_POSTS]** with the number of posts to scrape. (Requires a positive integer <=100)

#### Example command

```bash
$ docker run -v /Users/lx/hackernews/:/src hackernews --posts 125
```

Any errors with arguments will be printed into the terminal.

* **Integers >100** will be limited to 100.
* **Negative Integers** will be changed to 1
* **Floats, Strings or other invalid arguments** will be rejected and cause the program to end.

Once the process is complete, the fetched data will be written to **hackerNewsTopPosts.json** at the specified directory.

## Libraries Used

* [`python`][python] — Used the included argparse & json libraries to handle basic arguments, parsing responses from HN & writing JSON output.
* [`requests`][requests] — HTTP library for Python. Useful as it handles encoding and decoding with little effort from the programmer.
* [`validators`][validators] — collection of validators for Python. Used to validate URI from HN posts.



[python]: https://www.python.org
[requests]: https://pypi.org/project/requests/2.7.0/
[hn]: http://news.ycombinator.com
[dockerinstall]:  https://docs.docker.com/engine/installation
[validators]: https://validator-collection.readthedocs.io/en/latest/index.html
