#taking a series of input from the user
charname1 = input("Give me a character name:")
charname2 = input("Give me another character name:")
place = input("Give me name of a place:")
yr = input("Mention a year:")
verb1 = input("Give me a verb (present tense):")
noun1 = input("Give me a noun:")
noun2 = input("Give me another noun:")
verb2 = input("Give me a verb (present tense, in third person):")
verb3 = input("Give me a verb (present tense, in third person):")
charname3 = input("Give me another character name:")
verb4 = input("Give me a verb (present tense):")
noun3 = input("Give me another noun:")
adj = input("Give me an adjective:")
showname = input("Mention name of a show:")
noun4 = input("Give me another noun:")

#arrange the data in madlib variable

madlib = f"Newlywed couple {charname1} and {charname2} move into the town of {place} in a black-and-white {yr}s setting.One day they {verb1} a heart drawn on their {noun1}, but neither can remember what the {noun2} is.\nWhile Vision {verb2} his job at Computational Services Inc., Wanda decides that the heart {verb3} their anniversary.Their neighbor {charname3} introduces herself to Wanda and helps her prepare to {verb4} that night.Vision amazes his co-workers with his {noun3} but is unsure what his company actually does.All of this takes place in the {adj} sitcom {showname} which someone is watching on a {noun4}."

#to display the output
print(madlib)
