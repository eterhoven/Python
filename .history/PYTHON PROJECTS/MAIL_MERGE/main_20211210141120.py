with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    
final_names = []
for name in names:
    name = name.strip("\n")
    final_names.append(name)

for name in final_names:
    with open(name + "./Input/Letters/starting_letter.txt", mode="w") as letter_template:
        letter_template.replace("[name]", name)
        
    