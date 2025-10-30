gpa = float(input("what is your gpa?: "))
activities = input("are you involved in any extracurricular activities?(y/n): ").lower() == 'y'

if gpa >= 3.8:
    print("you are eligible for a full scholarship.")
elif 3.5 <= gpa < 3.8 and activities:
    print("you are eligible for a partial scholarship.")
else:
    print("no scholarships are granted")