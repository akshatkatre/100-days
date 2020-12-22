#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('Input/Names/invited_names.txt') as file_with_names:
    name_list = file_with_names.readlines()

template_letter: str = None
with open('Input/Letters/starting_letter.docx') as letter_template:
    template_list = letter_template.readlines()
    template_letter = "".join(template_list)
    print(template_letter)

for name in name_list:
    file_name = f'Output/ReadyToSend/letter_for_{name.strip()}.txt'
    letter_output = template_letter.replace('[name]', name.strip())
    print(file_name)
    print(letter_output)
    with open(file_name, mode='w') as output_file:
        output_file.write(letter_output)