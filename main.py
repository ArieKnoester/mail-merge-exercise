
with open("Input/Letters/starting_letter.txt") as starting_letter:
    template = starting_letter.read()

# print(template)

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

# print(names)

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        new_text = template.replace("[name]", name)
        letter.write(new_text)
