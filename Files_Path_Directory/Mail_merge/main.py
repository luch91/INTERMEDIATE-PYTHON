# TODO: Create a letter using starting_letter.txt
# Replace the [name] in the placeholder with the actual name
# Save the letters in the folder "Ready to Send"

PLACEHOLDER= "[name]"

with open("../Mail_merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # prints out names as list

with open("../Mail_merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()  # saves the content of the letter to letter_content
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"../Mail_merge/Output/Ready to Send/letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)




