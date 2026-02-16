from level3 import *

def open_file(path):
    with open(path,'r') as file:
        for line in file:
            lisr_of_lines=[w for w in line.split(",")]
            yield lisr_of_lines


def filter_lines(geni):
    for row in geni:
        if len(running_tests_on_a_line(row))>=1:
            yield row

def returning_suspicions_with_row_details(path):
    for row in path:
        if len(running_tests_on_a_line(row)) >= 1:
            yield (row,running_tests_on_a_line(row))


