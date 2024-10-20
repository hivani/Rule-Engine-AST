# Rule Engine with AST
# Overview
This project is a simple 3-tier rule engine application that determines user eligibility based on specific rules. The rules are represented using an Abstract Syntax Tree (AST) that allows dynamic creation, combination, and modification of rules. The application features a backend built with Flask, a frontend using HTML, CSS, and JavaScript, and a simple rule evaluation engine.
# Features:
Create dynamic rules using an Abstract Syntax Tree (AST).
Evaluate rules against user data.
Frontend interface for creating and evaluating rules.
Simple REST API to create and evaluate rules.
Custom error handling for invalid inputs.
# project-root/
├── app.py                  # Flask app to handle API and frontend routes
├── rule_engine.py          # Core rule engine logic with AST representation
├── test_rule_engine.py     # Unit tests for rule engine
├── static/
│   ├── style.css           # Frontend styling
│   └── script.js           # Frontend JavaScript for API calls
└── templates/
    └── index.html          # Frontend HTML template
