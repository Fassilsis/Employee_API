import os
from employeeApp import employees, error
from employeeApp.app import app
from flask import jsonify, request, make_response, render_template


@app.route('/')
def home():
    return 'Home for EmployeeApp Backend'

import string
from typing import List, Tuple


class Employee(object):

    def __init__(self, name: str, age: int,
                 gender: str, salary: float, department: str):
        self._name = name
        self._age = age
        self._gender = gender
        self._salary = salary
        self._department = department

    @property
    def name(self): return self._name

    @property
    def age(self): return self._age

    @property
    def gender(self): return self._gender

    @property
    def salary(self): return self._salary

    @property
    def department(self): return self._department

    def __str__(self):
        return f"{self.name}, age {self.age}, {self.gender}, " \
               f"from department {self._department}, earning ${self.salary}"


@app.route('/employee-data')
def read_employees(filepath: string) -> List[Employee]:
    result = []
    with open(filepath, 'r') as file_emp:
        for line in file_emp:
            values = line.rstrip().split(' ')
            employee = Employee(
                values[0], int(values[1]), values[2],
                float(values[3]), values[4])
            result.append(employee)
    return result

