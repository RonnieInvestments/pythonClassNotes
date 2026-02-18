'''
Identify the most popular genre:-> genre that appears most frequently across all user listening histories.
Find users who listen to a specific artist for marketing campaigns.
You need to identify the users (by index in the data list) who listened to that artist in the past week.
'''

# Sample user data - each element represents a user's listening history 
# Tuple with two elements - Genre -> string, List of artists -> list of strings
user_data = [
    ("Rock", ["Metallica", "Guns N' Roses", "AC/DC"]),
    ("Pop", ["Taylor Swift", "Ed Sheeran", "BTS"]),
    ("Hip Hop", ["Drake", "Kendrick Lamar", "J. Cole"]),
    ("Rock", ["Led Zeppelin", "Pink Floyd", "The Who"]),
    ("Pop", ["Ariana Grande", "The Weeknd", "Olivia Rodrigo"]),
]

# Finding the most popular genre
genre_counts = {} # empty dictionary to store the frequency of each genre

# To iterate through the data 

for genre, _ in user_data: # Extracts genre from the current user's tuple
    if genre in genre_counts: # Checks for its existence
        genre_counts += 1 # Increments the count of that genre
    else: # Does not exist 
        genre_counts[genre] = 1 # A new key-value pair is added to the dictionary and value set to 1

# Key argument max() specifies a function to use for comparison
# .get -> retrieve value associated with each genre
most_popular_genre = max(genre_counts, key= genre_counts.get)
print("Most popular genre:", most_popular_genre) # Prints genre with highest value

# Finding users who listen to a specific artist
# Define variable target_artist
target_artist = "BTS"

# Empty list to store indices of users who listened to the target artist
users_listening = [] 
for i, (_, artists) in enumerate(user_data): # Iterate through each user's listening history
  if target_artist in artists:
    users_listening.append(i) # Adds index (position) of the user in user_data to users_listening list 

# Check if any users listened to the target artist
if users_listening: # Users found
  print(f"Users who listened to {target_artist}:", users_listening)
else: # No users found
  print(f"No users listened to {target_artist} this week.")