# Rule Engine with AST
URL: http://127.0.0.1:5000/
# Overview
This project is a simple 3-tier rule engine application that determines user eligibility based on specific rules. The rules are represented using an Abstract Syntax Tree (AST) that allows dynamic creation, combination, and modification of rules. The application features a backend built with Flask, a frontend using HTML, CSS, and JavaScript, and a simple rule evaluation engine.
## Features

- **Create Rules**: Allows users to create rules in a user-friendly interface.
  
- **Evaluate Rules**: Evaluate user data against created rules to determine eligibility.
- **Abstract Syntax Tree**: Utilizes an AST to represent rules and perform evaluations efficiently.
- **Frontend**: A simple and interactive web interface built using HTML, CSS, and JavaScript.
- **API Integration**: RESTful API endpoints for creating and evaluating rules.
- **Unit Tests**: Basic unit tests to ensure the functionality of the rule engine.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Testing**: unittest (Python)

## Installation

To set up and run this project locally, follow these steps:

### Prerequisites

- Python 3.x installed on your machine.
- `pip` for installing Python packages.
- Virtual environment (recommended) for managing dependencies.
### Step-by-Step Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/rule-engine.git
   cd rule-engine

   
2. **Create a Virtual Environment**:
    ```
    python -m venv .venv
   .venv\Scripts\activate

3. **Install Dependencies**:
  ``` pip install Flask```
4.**Run the Application**:
  ``` python app.py```

# project-root/
```
├── app.py                  # Flask app to handle API and frontend routes
├── rule_engine.py          # Core rule engine logic with AST representation
├── test_rule_engine.py     # Unit tests for rule engine
├── static/
│   ├── style.css           # Frontend styling
│   └── script.js           # Frontend JavaScript for API calls
└── templates/
    └── index.html          # Frontend HTML template
