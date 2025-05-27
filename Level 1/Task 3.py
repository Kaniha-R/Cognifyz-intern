import re
def email_validator(email):
    pattern= r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

email=input("Enter an email address: ").strip()
if email_validator(email):
    print("valid email address.")
else:
    print("Invalid email address.")
    