with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)
    
    final_names = names.strip("\n")
    print(final_names)
    

#with open("./Input/Letters/starting_letter.txt") as 