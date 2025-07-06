# numbers = [1, 2, 3]
# print([i+1 for i in numbers])

# range_list = [item for item in range(1,5)]
# print([item*2 for item in range_list])

#names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie Dredd']
# print([name.upper() for name in names if len(name) > 5])

# from random import randint
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie Dredd']
# students_score = {student:randint(1, 100) for student in names}
# passed_student = {student:score for (student, score) in students_score.items() if score > 50}
# print(students_score)
# print(passed_student)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# # for (key, value) in student_dict.items():
# #     print(value)

# import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for(index, row) in student_data_frame.iterrows():
#     print(row['student'])
