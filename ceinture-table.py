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

    new_tuple: Tuple[int] = ()
    recalculate: bool = True
    while recalculate:
        new_tuple: Tuple[int] = get_values(min, max)
        new_result: int = new_tuple[0]
        divisor: int = new_tuple[1]
        # Recalculate as long as the difference with previous result is less or equal to 10
        # or the same result and divisor already exists in the list
        recalculate = False
        if len(list_previous_values) > 0:
            if abs(list_previous_values[-1][0] - new_result) < 10:
                 recalculate = True
            else:
                result_divisor: List[int] = [[x,y] for x, y in list_previous_values if [x,y] == [new_result, divisor]]
                #print(f"result_divisor: {result_divisor}")
                recalculate = len(result_divisor) > 0

    (result, value1, value2, value3) = new_tuple
    list_previous_values.append((result, value1))

    return f'{result:>3} : {value1:>2} = __ reste __', \
           f'{result:>3} : {value1:>2} = {value2:>2} reste {value3:>2}', \
           list_previous_values

def get_line_exercice_solution():
    exercises: List[int] = []
    solutions: List[int] = []
    list_previous_values: List[Tuple] = []
    for _ in range(3):
        exercise, solution, list_previous_values = get_calculus(6, 12, list_previous_values)
        exercises.append(exercise)
        solutions.append(solution)
    return  "  |  ".join(exercises), "  |  ".join(solutions)

def print_per_step(array_string: List[str], lines_per_groups: int, date_time: datetime):
    print(f"**** Version: {date_time} ****\n")
    for index in range(0, len(array_string), lines_per_groups):
        print("\n".join(array_string[index: index+lines_per_groups]))
        print("\n")
    print("\n")
    print("\n")

exercises: List[str] = []
solutions: List[str] = []
number_groups: int = 7
lines_per_groups: int = 7
number_lines: int = number_groups * lines_per_groups
for line in range(number_lines):
    exercise, solution = get_line_exercice_solution()
    exercises.append(exercise)
    solutions.append(solution)
    #print(f"Generated {line + 1} lines")
date_time: datetime = datetime.now()
print_per_step(exercises, lines_per_groups, date_time)
print_per_step(solutions, lines_per_groups, date_time)



    


        