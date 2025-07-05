#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file: # Get the name for every invited person
    names = [name.strip('\n') for name in file.readlines()] # Remove the newline character at the end of every name
    for name in names: # For every name in the names list
        with open("Input/Letters/starting_letter.txt") as letter_file:  # Get the text from the template letter file
            letter = letter_file.read() # Store the whole text in a variable
            letter = letter.replace("[name]", name) # Replace the [name] placeholder with the actual name of the person
            with open(f"Output/ReadyToSend/letter_for_{name}.txt", 'w') as output_file: # Create the final letter with person's name
                output_file.write(letter) # Write down the text inside the file with the person's name