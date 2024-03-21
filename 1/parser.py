# parser.py
import re

def parse_parameters(input_text):
    # Logic to parse parameters from the input text
    parameters = {}
    param_regex = re.compile(r'(p\d+)\(int\): ([\d,]+)')

    matches = param_regex.findall(input_text)
    for match in matches:
        param_id, values = match
        parameters[param_id] = [int(v) for v in values.split(',')]
    return parameters

def parse_constraints(input_text):
    # Logic to parse constraints from the input text
    constraints = []
    # Detect constraints sections, assuming it starts with '[Constraint]' in the text.
    constraints_section = re.search(r'\[Constraint\](.*?)$', input_text, re.DOTALL)
    if constraints_section:
        constraints_text = constraints_section.group(1)
        # Each line in this section is a separate constraint
        for line in constraints_text.strip().split('\n'):
            # Clean the line from any potential leading/trailing whitespaces
            line = line.strip()
            if line:  # Make sure the line is not empty
                # Break the line into conditions split by '||'
                conditions = line.split('||')
                constraint_conditions = []
                for condition in conditions:
                    # Assuming conditions are in the form of 'p<number>!=<value>'
                    param, value = re.match(r'(p\d+)!=(\d+)', condition.strip()).groups()
                    constraint_conditions.append((param, int(value)))
                constraints.append(constraint_conditions)

    return constraints
