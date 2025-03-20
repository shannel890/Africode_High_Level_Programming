# is_present = False
# if is_present:
#     print("Start the lesson")

# else:
#     print("skip the lesson")

# age = 18
# is_citizen = False
# has_passport = False
# if age >= 18 and is_citizen:
#     print("You are eligible to vote")
# elif not is_citizen and has_passport:
#     print("You can vote but you are not a citizen")

# else:
#     print("you are not eligible to vote")

# monthly_income = int(input("Enter your monthly income: "))
# rent = int(input("Enter your monthly rent: "))
# takeout_budget = int(input("Enter your takeout budget: "))
# actual_takeout = int(input("Enter your actual takeout: "))
# savings_goal = int(input("Enter your savings goal: "))

# if rent > monthly_income * 0.3:
#     print("Your rent is eating your paycheck like a hungry hippo")
#     if takeout_budget < actual_takeout:
#         print("You are eating out more than you should")
#         print(f"You've blown your takeout bugdet by ksh.{actual_takeout - takeout_budget}")

# elif monthly_income - rent - actual_takeout < savings_goal:
#     print("Your saving goal is more of a saving fantacy at this rate")
#     print(f"Your saving goal is {savings_goal} but you are saving {monthly_income - rent - actual_takeout}")

# else:
#     print("Your budget is actually balanced!Are your a wizard?3")

# ***************Shopping Cart Decision tree***********
# cart_total = 78
# distance_to_free_shipping = 22
# items_in_cart = ["Sensible Shoes","Questionable fashion choice","items you don't need"]
# bank_account_status = "crying"

# if cart_total < 100 and distance_to_free_shipping > 0:
#     print(f"Only ksh.{distance_to_free_shipping}")

# **************Calculator*************
numbers = int(input("Enter a number: "))
operator = input("Enter an operator: ")
numbers2 = int(input("Enter another number: "))
if operator == "+":
    print(numbers + numbers2)
elif operator == "-":
    print(numbers - numbers2)
elif operator == "*":
    print(numbers * numbers2)
elif operator == "/":
    print(numbers / numbers2)
else:
        print("syntax error")