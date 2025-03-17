age = int(input("Please Enter Age: "))

if age <= 19:
    print("qualified for student discount")
elif 20 <= age <= 54:
    print("qualified for no discount")
else:
    print("qualified for senior discount")
