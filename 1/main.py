# main.py
from target_combination import generate_target_combinations
from test_generator import TestGenerator
from parser import parse_parameters, parse_constraints
import time

def main(input_text):

    start_time = time.time()

    parameters = parse_parameters(input_text)
    constraints = parse_constraints(input_text)
    # Parse the input constraints and objectives from the paper
    target_combinations = generate_target_combinations(parameters, constraints)

    
    # Instantiate a TestGenerator with the parsed target combinations
    test_generator = TestGenerator(parameters, target_combinations, constraints)
    
    # Generate the test cases
    test_suite = test_generator.generate_test_cases()

    end_time = time.time()
    time_taken = end_time - start_time
    print("The test suite:\n")
    for i, test_case in enumerate(test_suite.test_cases, 1):
        print(f"Test Case {i}: {test_case}")

    print("\nTime taken to generate the test suite: {:.2f} seconds".format(time_taken))


# Run the main function if this script is executed
if __name__ == "__main__":
    with open("apache-short.txt", "r") as file:
        for line in file:
            if line.startswith('Name'):
                _, name = line.split(':')
                print("System:", name.strip())
                break

    with open("apache.txt", "r") as file:
        input_text = file.read()
    main(input_text)

