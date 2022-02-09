name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_name = name1.lower() + name2.lower()

t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")

true_count = t_count + r_count + u_count + e_count

l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")
e_count2 = combined_name.count("e")

love_count = l_count + o_count + v_count + e_count2

love_percentage = str(true_count) + str(love_count)
love_percentage = int(love_percentage)

if love_percentage < 10 or love_percentage > 90:
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")
elif 40 <= love_percentage <= 50:
    print(f" Your score is {love_percentage}, you are alright together. ")
else:
    print(f"Your score is {love_percentage}.")
