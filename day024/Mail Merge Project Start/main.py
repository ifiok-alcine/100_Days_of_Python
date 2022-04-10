# Code after looking at the solution. Less repitive.
with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    name_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    content = starting_letter.read()
    for name in name_list:
        stripped_text = name.strip()
        letter = content.replace("[name]", stripped_text)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_text}.txt", mode="w") as ready_letters:
            ready_letters.write(letter)

# # Code I wrote entirely by myself. Functional but not code be done in less lines.
# with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
#     content = starting_letter.read()
#
# with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
#     name_list = invited_names.readlines()
#     names = []
#     for name in name_list:
#         stripped_text = name.strip()
#         names.append(stripped_text)
#
# for name in names:
#     with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as ready_letters:
#         letter = content.replace("[name]", name)
#         ready_letters.write(letter)
