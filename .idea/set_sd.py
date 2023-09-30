morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses = set(morning) ^ afternoon
print(possible_courses)
