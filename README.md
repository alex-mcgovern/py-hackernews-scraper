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
Replace **[OUTPUT_FILEPATH]** with the **full path** to write the JSON output to.

Replace **[NUMBER_OF_POSTS]** with the number of posts to scrape. (Requires a positive integer <=100)

Any errors with arguments will be printed into the terminal.

Once the process is complete, the fetched data will be written to **hackerNewsTopPosts.json** at the specified directory.

## Technologies Used


[python]: https://www.python.org
[requests]: https://pypi.org/project/requests/2.7.0/
[hn]: http://news.ycombinator.com
[dockerinstall]:  https://docs.docker.com/engine/installation
