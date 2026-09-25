# Todo API

A simple Python command-line Todo application built to practice backend development fundamentals, database operations, and application structure.

## Features

* Create, view, update, and delete todos
* Create and manage users
* Find todos by user
* Store data using SQLite
* User-to-todo relationships using foreign keys
* Database constraints and error handling
* Separate database and business logic

## Project Structure

```text
Todo API/
├── database/
│   └── db.py
├── service/
│   └── todo_logic.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jamieleeuw/Todo-API.git
cd Todo-API
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

The SQLite database is created automatically when the application starts.

## What I Learned

This project helped me practice:

* Python project structure and modules
* Functions and application logic
* Working with SQLite and SQL
* CRUD database operations
* Primary and foreign keys
* Database constraints
* Parameterized SQL queries
* Error handling
* Separating business logic from database operations
* Virtual environments and dependencies
* Git and GitHub workflow

## Status

**Completed**

This project was built as part of my backend/software engineering learning journey. The focus was on understanding backend fundamentals before moving on to larger, more production-oriented projects.
