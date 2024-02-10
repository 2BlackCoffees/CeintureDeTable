from random import randrange
from typing import List

def get_calculus(min: int, max: int):
    value1 = randrange(min, max + 1)
    value2= randrange(5, max + 1)
    value3 = randrange(min - 1, value1)

    if value2 == 5: value2 = randrange(3, 5) # Reduce the probability to have a number less than 6
    if value3 == 0: value3 = value2 - 1 
    result = value1 * value2 + value3

    return f'{result:>3} : {value1:>2} = __ reste __', \
           f'{result:>3} : {value1:>2} = {value2:>2} reste {value3:>2}'

def get_line_exercice_solution():
    exercises = []
    solutions = []
    for line in range(3):
        exercise, solution = get_calculus(6, 12)
        exercises.append(exercise)
        solutions.append(solution)
    return  "  |  ".join(exercises), "  |  ".join(solutions)

def print_per_step(array_string: List[str], lines_per_groups: int):
    for index in range(0, len(array_string), lines_per_groups):
        print("\n".join(array_string[index: index+lines_per_groups]))
        print("\n")

exercises = []
solutions = []
number_groups = 7
lines_per_groups = 7
number_lines = number_groups * lines_per_groups
for line in range(number_lines):
    exercise, solution = get_line_exercice_solution()
    exercises.append(exercise)
    solutions.append(solution)

print_per_step(exercises, lines_per_groups)
print_per_step(solutions, lines_per_groups)



    


        