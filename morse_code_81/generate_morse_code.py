import json

data_dict = {}
with open('data.json') as file_handle:
    data_dict = json.load(file_handle)

# print(data_dict)
raw_string = input('Enter string to convert to morse code\n:').upper()
new_list = [x for x in raw_string]
# print(new_list)

morse_code = ""
for character in new_list:
    # print(f'{character} : {data_dict[character]}')
    if character == " ":
        morse_code = morse_code[:-2] + data_dict[character]
    else:
        morse_code += data_dict[character] + "  "

print('The morse code is:')
print(morse_code)