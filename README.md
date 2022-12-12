# fm_yoga_backend

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#description">Description</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
It contains the backend app build with Django and Django rest framework the Python framework.<br>
It uses the MySql as database and is hosted on pythonanywhere.com and the hosted url is: https://abhi2404.pythonanywhere.com.<br>
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* https://www.django-rest-framework.org/
* https://www.djangoproject.com/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Note:- This installation is for Linux.
This is an example of how to list things you need to use the software and how to install them.
Install python version 3.8 and pip.
1. Install python 
   ```sh
   sudo apt-get install python3.8
   ```
2. Install pip
   ```sh
   python get-pip.py
   ```

### Installation

_Below is an example of how to install and set up the app._

1. Clone the repo
   ```sh
   git clone https://github.com/abhi2404/fm_yoga_backend.git
   ```
2. Install virtual env
   ```sh
   pip install virtualenv
   ```
3. Create virtual env using 
   ```sh
   virtualenv virtualenv_name
   ```
4. Activate your virtual env using 
   ```sh
   source virtualenv_name/bin/activate
   ```
5. Now move to the project directory and run
   ```sh
   pip install -r  requirements.txt
   ```
6. Migrate your project
   ```sh
   python3 mange.py migrate
   ```
7. Run the dev server
   ```sh
   python3 manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--Description  -->
## Description
Django can be (and has been) used to build almost any type of website — from content management systems and wikis, through to social networks and news sites. It can work with any client-side framework, and can deliver content in almost any format (including HTML, RSS feeds, JSON, and XML).

Internally, while it provides choices for almost any functionality you might want (e.g. several popular databases, templating engines, etc.), it can also be extended to use other components if needed.
Django web applications typically group the code that handles each of these steps into separate files:

<img src="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png">

There are four main table used in the project auth_user, Shifts , UserDetails and the PaymentStatus.<br>
The auth_user table is used to store the username, credentails ,Lastlogin, etc information.<br>
The Shifts table is used to store the sessions avaliable to do the yoga. They can be dynamically handled if any change is required in the table.<br>
The UserDetails Table contains details of the reqistered user and the PaymentStatus table stores the latest payment status of each month.<br>
The main functions are written in views.py. The models.py hold tables as classes.

## Note:- The relations of the table is upload in the repo as:-https://github.com/abhi2404/fm_yoga_backend/blob/master/ERD_fm.pdf

<p align="right">(<a href="#readme-top">back to top</a>)</p>
