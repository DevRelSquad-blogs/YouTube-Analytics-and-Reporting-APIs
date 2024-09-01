# YouTube Analytics and Reporting API Guide

## Overview

This repository contains code examples and instructions on how to use YouTube Analytics and Reporting APIs to unlock insights from your YouTube channel data. The examples demonstrate how to set up API credentials using a service account and access key metrics like video views and custom reports.

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
