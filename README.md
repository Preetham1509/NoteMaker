Note Maker 
A secure, cloud-hosted web application for managing notes, featuring AWS deployment.

Live Demo
(http://notemaker-env.eba-hw3dvqyh.ap-south-1.elasticbeanstalk.com/)

🌟 Features
Note Management: Create, view, and delete personal notes through a clean web interface.

Cloud Native: Fully deployed on AWS Elastic Beanstalk using a Python 3.14 environment.

Database Migrations: Automated database schema updates via Django migrations.

🛠️ Tech Stack
Framework: Django 6.0

Language: Python 3.14

Database: SQLite (Development) / AWS RDS (Production-Ready)

Cloud Hosting: AWS Elastic Beanstalk (EC2, S3)

Version Control: Git & GitHub

💻 Local Setup
To run this project on your MacBook Air:

Clone the repository:

Bash

git clone https://github.com/Preetham1509/NoteMaker.git
cd NoteMaker

Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run migrations & start server:
python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000 to see the app.

☁️ AWS Deployment Details
The project is configured for AWS Elastic Beanstalk using the following structure:

.ebextensions/: Contains django.config for automated migrations on the cloud.
Environment: Python 3.14 running on 64bit Amazon Linux 2023.
