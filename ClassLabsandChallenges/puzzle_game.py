stars = [5, 10, 20, 50, 100, 200, 500, 100]
messages = [
    "Great start! You're getting the hang of it.",
    "Nice work! Keep solving those puzzles.",
    "Impressive! Your puzzle skills are growing.",
    "Amazing! You’re becoming a true puzzle master.",
    "Outstanding! You’ve reached a major milestone.",
    "Incredible dedication! Few players make it this far.",
    "Legendary performance! You are among the best.",
    "Ultimate Champion! You’ve conquered the puzzle world!"
]

# For loop initialization
for star in stars:
    # Access congratulatory message using index
    message = messages[stars.index(star)]
    # Show output
    print(message)