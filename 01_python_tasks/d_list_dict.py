# Data Structures : Lists and Dictionaries


students = {
    "student_1": {"name": "Jack",
                  "age": 21,
                  "grades": [ ["Math", "A+" ], ["Chemistry", "C" ],  ["Physics", "B"] ]
                },
    
    "student_2": {"name": "John",
                  "age": 20,
                  "grades": [ ["Math", "B" ], ["Chemistry", "C" ],  ["Physics", "D"] ]
                },

    "student_3": {"name": "Jenny",
                  "age": 21,
                  "grades": [ ["Math", "A" ], ["Chemistry", "C" ],  ["Physics", "D"] ]
                },
            
}

# ||||| CRUD Operations |||||


# Create

students["student_2"]["city"] = "Mumbai"        # Output:  {'name': 'John', 'age': 20, 'grades': [['Math', 'B'], 
print(students["student_2"])                    # ['Chemistry', 'C'], ['Physics', 'D']], 'city': 'Mumbai'}               



# Read

print( students["student_1"]["name"] )          # Output: Jack

print( students.get("student_3") )              # Output: {'name': 'Jenny', 'age': 21, 'grades': [['Math', 'A'], 
                                                # ['Chemistry', 'C'], ['Physics', 'D']]}


# Update

students["student_1"]["grades"][2][1] = "D"     # Output: {'name': 'Jack', 'age': 21, 'grades': [['Math', 'A+'], 
print( students["student_1"])                   # ['Chemistry', 'C'], ['Physics', 'D']]}



# Delete

del students["student_3"]["grades"][1]          # {'name': 'Jenny', 'age': 21, 'grades': [['Math', 'A'], ['Physics', 'D']]}
print( students["student_3"] )

