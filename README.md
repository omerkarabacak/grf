# Google Rank Finder (GRF) (SEO Rank)

## What is this

This is a simple script which helps you to find your rank in Google in a specific search term. It can be helpful for your SEO journey. There are couple of parameters you can pass through the command line.

Sometimes finding correct Python version or downloading dependecies could be a proble so I have created Docker image which you can quickly run it from commandline.

## What are these arguments
**search_keyword** -> Search term

**country:** Country or region to focus the search on. Similar to changing the TLD, but does not yield exactly the same results. Only Google knows why...

**tld:** Top level domain.

**lang:** Language.

**num:** Number of results per page.

**stop:** Last result to retrieve. Use None to keep searching forever.

**pause:** Lapse to wait between HTTP requests. A lapse too long will make the search slow, but a lapse too short may cause Google to block your IP.


```
Usage : python3 grf.py <search_keyword> <country> <tld> <lang> <num> <stop> <pause>
```

## How to run it

### How to run with Docker
There are 2 options.
You can build your Docker image with Dockerfile or use ready public Docker image from Docker Hub.

#### Option 1: Build your own Docker image and use it
Build Docker image:
```bash
docker build -t grf:1.0 .
```
Run with built local Docker image:
```bash
docker run --rm grf:1.0 "<keywords>" Turkey com.tr tr 50 99 3 | grep <your_website>
```

#### Option 2: Use public Docker image hosted on Docker Hub
Run with public Docker image:
```bash
docker run --rm omerkarabacak/grf "<keywords>" Turkey com.tr tr 50 99 3 | grep <your_website>
```

### How to run with Python virtual environment
First create virtual environment
```bash
python3 -m venv env
```
Enter virtual environment
```bash
source env/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Run script
```bash
python3 grf.py "<keywords>" Turkey com.tr tr 50 99 3 | grep <your_website>
```

#### Which Python version?
Tested with Python 3.8

#### Requirements
```
beautifulsoup4==4.9.0
google==2.0.3
soupsieve==2.0
```