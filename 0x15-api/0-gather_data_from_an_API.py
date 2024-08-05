#!/usr/bin/python3
import json
import sys
def get_employee_todo_list(employee ID):
try:
	user.response = request.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
	user = user.response.json()
	employee_name=user(name)

total_tasks = len(tasks)
done_tasks = (for task in tasks if task ['completed']))
num_of_done_tasks = len (done-tasks)
if __name__ == "__main__":
    if len(sys.argv) != 2:
	print("Usage: python script.py <employee_id>")
else:
	try:
	employee_id = int(sys.argv[1])
	get_employee_todo_progress(employee_id)
	except ValueError:
	print("Please provide a valid integer for the employee ID.")







