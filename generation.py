print("GENERATION IDENTIFIER\n")
response = input("Which year were you born? \n")

def validate_input(response):
    if response.isdigit and len(response) == 4:
        year = int(response.strip())
        get_generation(year)
    else:
        print("Invalid entry.")

def get_generation(year):
    if year >= 1883 and year < 1901:
        generation = "Lost Generation"
        comment = "Born too late for the Renaissance, too early for the cocktail parties"
        get_message(generation, comment)
    if year >= 1901 and year < 1928:
        generation = "Greatest Generation"
        comment = "\"It is, I believe, the greatest generation any society has ever produced\" - Tom Brokaw"
        get_message(generation, comment)
    if year >= 1928 and year < 1946:
        generation = "Silent Generation"
        comment = "Born quiet, raised quieter, and still not telling you the secret to a good recipe"
        get_message(generation, comment)
    if year >= 1946 and year < 1965:
        generation = "Baby Boomers"
        comment = "Baby boomers are like fine wine - they get better with age, but still make you wonder what you'll pay for it"
        get_message(generation, comment)
    if year >= 1965 and year < 1981:
        generation = "Generation X"
        comment = "The original slackers who grew up to be professionals...but still sleep in until noon"
        get_message(generation, comment)
    if year >= 1981 and year < 1997:
        generation = "Millenials"
        comment = "Avocado toast and Starbucks much?"
        get_message(generation, comment)
    if year >= 1997 and year < 2013:
        generation = "Generation Z"
        comment = "Where participation trophies and social media followers are the ultimate currency"
        get_message(generation, comment)
    if year >= 2013:
        generation = "Generation Alpha"
        comment = "They're growing up with Alexa, not Encyclopedia Britannica."
        get_message(generation, comment)

    else:
        return

def get_message(generation, comment):
    message = (f"Hah! {generation}! {comment}!\n")
    print(message)

validate_input(response)