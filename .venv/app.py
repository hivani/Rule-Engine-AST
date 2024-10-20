from flask import Flask, request, jsonify, render_template
from rule_engine import create_rule, evaluate_rule, Node
import psycopg2
import json

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

# Database connection function
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="rule_engine",
        user="postgres",
        password="shivani@28"
    )

# API to create a rule from a string
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule_string')
    if not rule_string:
        return jsonify({"error": "Rule string is required"}), 400

    # Create the rule and get the AST
    rule_ast = create_rule(rule_string)
    
    # Convert Node to dictionary before storing in DB
    rule_ast_dict = rule_ast.to_dict()

    # Store the rule in the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO rules (rule_name, rule_ast) VALUES (%s, %s)",
                ("Sample Rule", json.dumps(rule_ast_dict)))  # Serialize Node to JSON as a dictionary
    conn.commit()
    cur.close()
    conn.close()
    
    # Return the AST as JSON (already a dictionary)
    return jsonify({"message": "Rule created successfully", "rule_ast": rule_ast_dict}), 201

# API to evaluate a rule against user data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_id = request.json.get('rule_id')
    user_data = request.json.get('user_data')
    
    if not rule_id or not user_data:
        return jsonify({"error": "rule_id and user_data are required"}), 400
    
    # Fetch the rule AST from the database
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT rule_ast FROM rules WHERE id = %s", (rule_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()

    if result is None:
        return jsonify({"error": "Rule not found"}), 404

    # Use the result directly since it's already a dictionary
    rule_ast_dict = result[0]

    # Convert the dictionary back to a Node object
    rule_ast = Node.from_dict(rule_ast_dict)

    # Evaluate the rule with the user data
    is_eligible = evaluate_rule(rule_ast, user_data)
    
    return jsonify({"eligible": is_eligible}), 200

if __name__ == '__main__':
    app.run(debug=True)
