#the string we want to replace in our letter to make each letter personal
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    #save all contents of letter as a string
    letter_contents = letter_file.read()
    #go through lettero contents and replace the placeholder with the names
    for name in names:
        #remove new lines from names list
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        #write new letters into a new file..python will create for you
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
