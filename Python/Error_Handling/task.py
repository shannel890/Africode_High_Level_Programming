class MySlrError(Exception):
    pass

def admission_number(check_admission):
    if not check_admission.isdigit() or len(check_admission) < 5:
        raise MySlrError("Admission number must be at least 5 digits")
    else:
        print("Access Granted")

try:
    admission_number("2435")
except MySlrError as e:
    print(f"Error: {e}")
