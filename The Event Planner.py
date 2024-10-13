# Task 1 Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if (attendees >= 100)  else "conference room"
print(venue)


# Task 2 Venue Selection: Furthur enhance your code to recommend additonal things like "audio system" or "projector" based on the number of attendees. 
if attendees <= 100:
    print("Using a projector is ideal.")
elif attendees >= 200:
    print("Test the audio system so everyone can hear.")


# Task 3 Cetering Choices Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

food_preference = input("Would you like vegetarian or something else? ")
food_options = "I recommend Veggie Delight Carriers" if food_preference == "vegitarian" else "Check out Gourmet Meals Caterers" 
print(food_options)