#======================================#
#             Fictionamer              #
#           by Randall Arms            #
#  github.com/randallarms/fictionamer  #
#======================================#

from random import randint
import os

# Opening text
print("\n\n=========")
print("Fictionamer")
print("=========")
print("Generate a name!")

# Genres (to be added: steampunk)
genres = ["fantasy", "scifi", "horror"]

# Name generation
def name_gen(genre):

    if not genre in genres:
        print("\nGenre not found! ")
        exit()

    # Determine gender
    gender = "male"
    if randint(0,1) == 0:
        gender = "female"
    
    # Get files
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    f_prefix = open(os.path.join(__location__, "names/" + genre + "/prefix_" + gender + ".txt"), "r")
    f_name = open(os.path.join(__location__, "names/" + genre + "/name_" + gender + ".txt"), "r")
    f_suffix = open(os.path.join(__location__, "names/" + genre + "/suffix_" + gender + ".txt"), "r")
    
    # Fill list of possible names from file
    prefixes = []
    names = []
    suffixes = []
    for line in f_prefix:
        prefixes.append(line)
    for line in f_name:
        names.append(line)
    for line in f_suffix:
        suffixes.append(line)

    # Generate name
    name_str = ""
    if randint(0,2) == 0:
        name_str += prefixes[randint(0, len(prefixes)-1)].strip('\n') + " "
    name_str += names[randint(0, len(names)-1)].strip('\n')
    name_str += " " + names[randint(0, len(names)-1)].strip('\n')
    if randint(0,5) == 0:
        name_str += ", " + suffixes[randint(0, len(suffixes)-1)].strip('\n')
    return name_str
        
    file.close()

# Get the genre
print("\nWhich genre do you wish to base the name in? ")
g = input("> ");

# Generate the name
name = name_gen(g)

# Print the results
print("\nGenerated name: ")
print(name + "\n")