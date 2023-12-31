# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

code_dict = {row.letter:row.code for (index, row) in data.iterrows()}
def generate_phonetic():
    answer = input("Enter a word? ").upper()

    try:
        result_list = [code_dict[letter] for letter in answer]
    except KeyError:
        print("Sorry only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(result_list)

generate_phonetic()
