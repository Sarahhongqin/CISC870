
def is_combination_valid(combination, constraints):
    # Check if a given combination violates any constraint
    for constraint in constraints:
        if all(combination[param] == value for param, value in constraint):
            return False
    return True

def generate_target_combinations(parameters, constraints):
    from itertools import combinations

    # Generate all pairs of parameters for coverage strength t = 2
    parameter_pairs = combinations(sorted(parameters), 2)

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