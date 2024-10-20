# test_rule_engine.py
from rule_engine import create_rule, evaluate_rule

# Create a sample rule
rule_ast = create_rule("age > 30 AND department = 'Sales'")

# Create sample user data
user_data = {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 5
}

# Evaluate the rule against the user data
result = evaluate_rule(rule_ast, user_data)
print("User eligible:", result)
