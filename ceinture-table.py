from random import randrange
from typing import List, Tuple
from datetime import datetime


def get_values(min: int, max: int):
    value1:int = randrange(min, max + 1)
    value2:int = randrange(5, max + 1)
    value3:int = randrange(min - 1, value1)
    if value2 == 5: value2 = randrange(3, 5) # Reduce the probability to have a number less than 6
    if value3 == 0: value3 = value2 - 1 

    result:int = value1 * value2 + value3

    return (result, value1, value2, value3)

def get_calculus(min: int, max: int, list_previous_values: List[Tuple[int]]):

    new_tuple:Tuple[int] = ()
    recalculate: bool = True
    while recalculate:
        recalculate = False
        new_tuple = get_values(min, max)
        new_result: int = new_tuple[0]
        if len(list_previous_values) > 0:
            recalculate = abs(list_previous_values[-1] - new_result) < 10 or \
                          new_result in list_previous_values

    (result, value1, value2, value3) = new_tuple
    list_previous_values.append(result)

    return f'{result:>3} : {value1:>2} = __ reste __', \
           f'{result:>3} : {value1:>2} = {value2:>2} reste {value3:>2}', \
           list_previous_values

def get_line_exercice_solution():
    exercises:List[int] = []
    solutions:List[int] = []
    list_previous_values: List[Tuple] = []
    for line in range(3):
        exercise, solution, list_previous_values = get_calculus(6, 12, list_previous_values)
        exercises.append(exercise)
        solutions.append(solution)
    return  "  |  ".join(exercises), "  |  ".join(solutions)

def print_per_step(array_string: List[str], lines_per_groups: int, date_time: datetime):
    print(f"**** Version: {date_time} ****\n")
    for index in range(0, len(array_string), lines_per_groups):
        print("\n".join(array_string[index: index+lines_per_groups]))
        print("\n")

exercises:List[str] = []
solutions:List[str] = []
number_groups:int = 7
lines_per_groups:int = 7
number_lines:int = number_groups * lines_per_groups
for line in range(number_lines):
    exercise, solution = get_line_exercice_solution()
    exercises.append(exercise)
    solutions.append(solution)
    #print(f"Generated {line + 1} lines")
date_time = datetime.now()
print_per_step(exercises, lines_per_groups, date_time)
print_per_step(solutions, lines_per_groups, date_time)



    


        