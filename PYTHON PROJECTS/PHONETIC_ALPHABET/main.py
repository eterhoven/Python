import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

phonetic_dict = pandas.read_csv("./nato_phonetic_alphabet.csv", header=0, index_col=0, squeeze=True).to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

request = input("Please enter your word").upper()
request_split = list(request)

final_answer = []
for letter in request_split:
    if letter in phonetic_dict.keys():
        final_answer.append(phonetic_dict[letter])

print(final_answer)
