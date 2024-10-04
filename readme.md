# Project Setup Instructions

Follow these steps to clone and set up the project on Windows or macOS.

## Prerequisites

-  [Python installed (preferably the latest version)](https://www.python.org/downloads/)
-  [Git installed](https://git-scm.com/downloads)
-  [NodeJS installed](https://nodejs.org/en/download/)

## Clone the Repository

Open your terminal and run the following command:

```sh
git clone https://github.com/yourusername/SHOBAI.git
cd SHOBAI
```

## Create a Virtual Environment

### On Windows

```sh
python -m venv .venv
.venv\Scripts\activate
```

### On macOS

```sh
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```sh
pip install -r requirements.txt
```

```sh
python manage.py tailwind install
```

## Run the Project

To start both the Django development server and Tailwind watch mode, run the following commands:

### Start Django Development Server

```sh
python manage.py runserver
```

### Start Tailwind

```sh
python manage.py tailwind start
```

## Additional Notes

-  Ensure all environment variables are set up as required.
-  Refer to the documentation for any additional setup or configuration.
