# afdb-scraper

This Python project is designed to scrape data from the [AFDB Hardware Store](https://www.afdb.fr/) website. It uses the Scrapy framework with a CrawlSpider spider model to efficiently collect information from various product pages. The scraped data is then stored in a CSV file named `afdb.csv`.

## Table of Contents
- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Fields Scraped](#fields-scraped)
- [Sample Output](#sample-output)

## Project Description

The main goal of this project is to gather product information from the AFDB Hardware Store website. This information includes details like the product's URL, title, brand, image URLs, description, category, SKU, details, variation, finish, and stock.

## Prerequisites

Before running the scraper, you need to ensure that you have the following dependencies installed:

- Python 3.x
- Scrapy


You can install Scrapy and other dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Installation 
1. Clone this repository to your local machine:
```bash
git clone https://github.com/bensouiciakram/hardware-store-scraper.git
```
