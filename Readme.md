# YouTube Analytics and Reporting API Guide

## Overview

This repository contains code examples and instructions on using YouTube Analytics and Reporting APIs to unlock insights from your YouTube channel data. The examples demonstrate setting up API credentials using a service account and accessing key metrics like video views and custom reports.

For additional insights and practical use cases, please see [this article on YouTube Analytics and Reporting API Guide]().

## Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/YouTube-Analytics-and-Reporting-APIs.git
```

### Navigate to the Project Directory

```bash
cd YouTube-Analytics-and-Reporting-APIs
```

### Install Required Libraries

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Set Environment Variable
Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the path of your service account key:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-file.json
```

## Usage

### Retrieve Video Views
Run the Python script read.py to retrieve video views:

```bash
python analyze.py
```

### Create and Download Custom Reports
Run the script to create and download custom reports:

```bash
python report.py
```
If you would like more information on generating custom reports, please refer to the practical guide in [this article]().

