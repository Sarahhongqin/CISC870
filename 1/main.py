# main.py
from target_combination import generate_target_combinations
from test_generator import TestGenerator
from parser import parse_parameters, parse_constraints

def is_combination_valid(combination, constraints):
    # Check if a given combination violates any constraint
    # print('combination:', combination)
    for constraint in constraints:
        # print('constraint:', constraint)
        if all(combination.get(param) == value for param, value in constraint):
            return False
    return True

def generate_target_combinations(parameters, constraints):
    from itertools import combinations

    # Generate all pairs of parameters for coverage strength t = 2
    parameter_pairs = list(combinations(sorted(parameters), 2))
    # print(parameter_pairs)

    # Generate all valid combinations for each pair
    target_combinations = []
    for param1, param2 in parameter_pairs:
        values1 = parameters[param1]
        values2 = parameters[param2]

        # Generate all possible combinations for this pair
        for value1 in values1:
            for value2 in values2:
                combination = {param1: value1, param2: value2}

                # Check if the combination is valid against the constraints
                if is_combination_valid(combination, constraints):
                    target_combinations.append(combination)

    return target_combinations

def main(input_text):

    parameters = parse_parameters(input_text)
    constraints = parse_constraints(input_text)
    # Parse the input constraints and objectives from the paper
    target_combinations = generate_target_combinations(parameters, constraints)

    
    # Instantiate a TestGenerator with the parsed target combinations
    test_generator = TestGenerator(parameters, target_combinations, constraints)
    
    # Generate the test cases
    test_suite = test_generator.generate_test_cases()

    # Output the test suite - For now, just print the test cases
    for test_case in test_suite.test_cases:
        print('test_case:', test_case)

# Run the main function if this script is executed
if __name__ == "__main__":
    with open("apache.txt", "r") as file:
        input_text = file.read()
    main(input_text)

