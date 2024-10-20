// Create Rule Handler
document.getElementById('create-rule-btn').addEventListener('click', async () => {
    const ruleString = document.getElementById('rule-input').value;
    
    if (!ruleString) {
        document.getElementById('create-rule-response').innerText = 'Please enter a rule.';
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/create_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rule_string: ruleString })
    });

    const data = await response.json();
    
    if (response.ok) {
        document.getElementById('create-rule-response').innerText = `Rule created successfully: ${JSON.stringify(data.rule_ast)}`;
    } else {
        document.getElementById('create-rule-response').innerText = `Error: ${data.error}`;
    }
});

// Evaluate Rule Handler
document.getElementById('evaluate-rule-btn').addEventListener('click', async () => {
    const ruleId = document.getElementById('rule-id-input').value;
    const userData = document.getElementById('user-data-input').value;

    if (!ruleId || !userData) {
        document.getElementById('evaluate-rule-response').innerText = 'Please enter rule ID and user data.';
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/evaluate_rule', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            rule_id: ruleId,
            user_data: JSON.parse(userData)
        })
    });

    const data = await response.json();
    
    if (response.ok) {
        document.getElementById('evaluate-rule-response').innerText = `Eligibility: ${data.eligible}`;
    } else {
        document.getElementById('evaluate-rule-response').innerText = `Error: ${data.error}`;
    }
});
