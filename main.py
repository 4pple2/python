#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Input/Names/invited_names.txt") as file:
      line = file.readline()
     # while line:


g = open("Input/Letters/starting_letter.txt","r")
f = open("Input/Names/invited_names.txt", "r")

reps = f.readlines()
gep = g.read()
print(reps)
"""
for i in reps:
      i = i.strip()
      with open(f"Output/ReadyToSend/{i}ToMessage.txt",'w') as file:
            file.write(gep.replace('[name]', i))
"""
