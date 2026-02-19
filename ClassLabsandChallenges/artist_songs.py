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
