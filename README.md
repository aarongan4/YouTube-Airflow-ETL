# YouTube Comments ETL Project

This project is an ETL (Extract, Transform, Load) process that ingests YouTube video comments, transforms the data into CSV format, and uploads the CSV to an AWS S3 bucket. It utilizes Python for data transformation, Apache Airflow on an EC2 Ubuntu instance for orchestration, and various other tools and services.

Inspired by this [video](https://www.youtube.com/watch?v=q8q3OFFfY6c&t=994s). Thanks to the creator!

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Execution](#execution)

## Description

This project automates the extraction of comments from YouTube videos, processes the data to a CSV format, and stores the result in an AWS S3 bucket. It is a data engineering solution that can be used for various data analysis and machine learning tasks.

## Prerequisites

Before you get started, ensure you have the following prerequisites in place:

1. **Google Developer Account**: You'll need to set up a Google Developer Account and obtain API keys to access the YouTube API.

2. **AWS Account**: Configure an AWS account and create an S3 bucket for storing the processed data.

## Execution

1. **Create Python Script to Extract YouTube Comments Data:** [YouTube API Docs](https://developers.google.com/youtube/v3/docs)

    - Develop a Python script that uses the YouTube API to extract comments data from videos. You can use libraries like googleapiclient to interact with the API. Store the extracted data in a structured format, such as a csv file. [Example](https://github.com/aarongan4/YouTube-Airflow-ETL/blob/main/youtube_etl.py)

2. **Configure an EC2 Instance with t3.medium and Ubuntu:**

    - Log in to your AWS Management Console.
    - Launch a new EC2 instance with the desired specifications (t3.medium and Ubuntu).
    - Configure security groups to allow necessary traffic (e.g., SSH, HTTP).
    - Download the private key file to access the EC2 instance.

3. **Install Python Packages on EC2 Instance:**

    - Connect to your EC2 instance using SSH.
    - Update the package [list](https://github.com/aarongan4/YouTube-Airflow-ETL/blob/main/ubuntu_packages.txt). 
    - Install Python and other dependencies.

4. **Configure Airflow Standalone Instance and Access UI:**

    - Follow the Airflow installation guide for setting up a standalone Airflow instance on your EC2 instance.
      `airflow standalone`
    - Access the Airflow UI by navigating to the Airflow web interface URL (usually port **8080**). Ensure the necessary ports are open in your security group.
  
5. **Create a Python Script for the DAG:**

    - Write a Python script that defines an Airflow DAG for your ETL process. The DAG should include tasks to run your YouTube comments extraction script and necessary configruations. [Example](https://github.com/aarongan4/YouTube-Airflow-ETL/blob/main/youtube_dag.py)

6. **Create an S3 Bucket:**

    - Log in to your AWS Management Console.
    - Create a new S3 bucket to store the processed data. Configure the bucket's permissions and access controls as needed.
  
7. **Upload Python Script to EC2 Instance and Create Folder Structure:**
```bash
~/
│
├── airflow/
│   ├── youtube_dags/
│   │   ├── youtube_dag.py
│   │   ├── youtube_etl.py

```

9. **Trigger the DAG:**

    - In the Airflow UI, enable and trigger your DAG manually. You can also set up scheduling for periodic execution as needed.
Remember to replace placeholders with actual paths, filenames, and other specific details that apply to your project. Additionally, ensure that your EC2 instance's security group and IAM roles are correctly configured to interact with S3 and the YouTube API.





