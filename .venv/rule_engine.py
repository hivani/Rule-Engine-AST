# rule_engine.py

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None
        }

    @staticmethod
    def from_dict(data):
        """Static method to create a Node from a dictionary."""
        if data['type'] == 'operator':
            left = Node.from_dict(data['left']) if data['left'] else None
            right = Node.from_dict(data['right']) if data['right'] else None
            return Node(data['type'], data['value'], left, right)
        elif data['type'] == 'operand':
            return Node(data['type'], data['value'])

# Example rule creation function
def create_rule(rule_string):
    # Simplified parsing of the rule string, returning an AST (Node tree)
    if "AND" in rule_string:
        left_part = rule_string.split("AND")[0].strip()
        right_part = rule_string.split("AND")[1].strip()
        return Node("operator", "AND", left=Node("operand", left_part), right=Node("operand", right_part))
    elif "OR" in rule_string:
        left_part = rule_string.split("OR")[0].strip()
        right_part = rule_string.split("OR")[1].strip()
        return Node("operator", "OR", left=Node("operand", left_part), right=Node("operand", right_part))
    else:
        return Node("operand", rule_string)

# Example rule evaluation function
def evaluate_rule(node, user_data):
    if node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, user_data) and evaluate_rule(node.right, user_data)
        elif node.value == "OR":
            return evaluate_rule(node.left, user_data) or evaluate_rule(node.right, user_data)
    elif node.type == "operand":
        # Basic string parsing to determine the condition (simplified for example)
        if ">" in node.value:
            field, value = node.value.split(">")
            field, value = field.strip(), int(value.strip())
            return user_data.get(field) > value
        elif "=" in node.value:
            field, value = node.value.split("=")
            field, value = field.strip(), value.strip().replace("'", "")
            return user_data.get(field) == value
    return False
