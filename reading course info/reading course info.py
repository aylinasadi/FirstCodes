import csv

def load_courses():
    with open("courses.csv", 'r') as f:
        reader = csv.DictReader(f)
        courses_dict = {}

        for line in reader:
            for key in range(len(line)):
                courses_dict[line["Course Code"]] = {
                    "title": line["Course Title"], 
                    "prereq": [line["Prerequisite"]], 
                    "credits": int(line["Credit Hours"])
                    }
    return courses_dict
    
def count_3_credit_courses(courses_dict):
    count = 0
    for course in courses_dict:
        if courses_dict[course]["credits"] == 3:
            count += 1
    return f"number of courses with 3 credit hours: {count}"

def count_4_credit_courses(courses_dict):
    count = 0
    for course in courses_dict:
        if courses_dict[course]["credits"] == 4:
            count += 1
    return f"number of courses with 4 credit hours: {count}"

def get_prerequisite(courses_dict, course_title):
    for course_code, info in courses_dict.items():
        if info["title"] == course_title:
            prereq = info["prereq"]
            if prereq == ["None"]:
                prereq = "None"
            return f"the prerequisite/s for {course_title} is: {prereq}"
    return "course not found"

def total_credit_hours(courses_dict):
    total = 0
    for code in courses_dict:
        total += courses_dict[code]["credits"]
    return f"the total credit hours of all courses is {total}"

def count_math_courses(courses_dict):
    count = 0
    for code in courses_dict:
        if code.startswith("MTH"):
            count += 1
    #or count = sum(1 for code in courses_dict if code.startswith("MTH"))
    return f"there are {count} math courses"

courses_dict = load_courses()
print(count_3_credit_courses(courses_dict))
print(count_4_credit_courses(courses_dict))
print(get_prerequisite(courses_dict, "Calculus I"))
print(total_credit_hours(courses_dict))
print(count_math_courses(courses_dict))