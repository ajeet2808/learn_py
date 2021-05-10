# <, <=, >, >=, ==, !=
# Both of these operators (strict and non-strict), as well as the two others discussed in the next section, are binary operators with left-sided binding, and their priority is greater than that shown by == and !=.

# Priority	Operator	
# 1	        +, -	unary
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	binary
# 5	        <, <=, >, >=	
# 6	        ==, !=	


# Conditions and conditional execution

# if true_or_not:
#     do_this_if_true

the_weather_is_good = True
def go_for_a_walk():
    print("Walking....")
def have_lunch():
    print("Having lunch...")

if the_weather_is_good:
    go_for_a_walk()
have_lunch()

#NOTE: Python 3 does not allow mixing spaces and tabs for indentation.


# if else

# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

#The elif statement
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()