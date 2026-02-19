# Learning about dictionaries
artist_songs = {  # Initial dictionary structure
    # specify artist names separated by commas, followed by a colon : 
    # and then a list of their popular songs enclosed in square brackets [].
    # artist's name - key, songs - value
    "The Beatles": ["Hey Jude", "Let It Be", "Yesterday"],
    "Taylor Swift": ["Shake It Off", "Love Story", "Blank Space"],
    "Ed Sheeran": ["Perfect", "Thinking Out Loud", "Photograph"]
} 

# Accessing data - Use the artist name (key) enclosed in 
# square brackets [] to retrieve the corresponding value (song list).
beatle_songs = artist_songs["The Beatles"]
# print(beatle_songs)
# Iterate through beatle songs
for song in beatle_songs:
    print(f"-{song}")
    print("")

swift_songs = artist_songs["Taylor Swift"]
print(swift_songs)

sheeran_songs = artist_songs["Ed Sheeran"]
print(sheeran_songs)

# check on recommendation logic
# Get user input
favorite_artist = input("Please enter your favorite artist:\n")

# Check for favorite artist
if favorite_artist in artist_songs:
    recommended_songs = artist_songs[favorite_artist]
    print(f"Here are some recommendations from your {favorite_artist}")
    for song in recommended_songs:
        print(f"- {song}")

else:
    print(f"Sorry we do not have songs from {favorite_artist} yet. Here are some recommendations from similar artists.")
    # Add logic to recommend songs from similar artists - for now lets have a placeholder
    print("- Similar artist song 1")
    print("- Similar artist song 2")