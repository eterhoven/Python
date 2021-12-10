with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    
final_names = []
for name in names:
    name = name.strip("\n")
    final_names.append(name)

with open("./Input/Letters/starting_letter.txt") as letter_template:
    letter = letter_template.read()

for name in final_names:
    f = open(name + letter, mode="w"):
    f.replace("[name]", name)
    f.close
        
    