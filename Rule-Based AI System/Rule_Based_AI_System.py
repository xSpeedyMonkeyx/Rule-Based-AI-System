# Rule-Based Book or Music Recommendation System
# This program recommends books or songs based on user input using predefined rules.

def recommend_item(user_input):
    """
    Function to recommend a book or song based on user input.
    The system checks the input for keywords and returns relevant recommendations.
    """
    user_input = user_input.lower()  # Convert input to lowercase for uniform matching

    # Rule-based recommendations dictionary
    recommendations = {
        "fantasy": ["Harry Potter by J.K. Rowling", "The Chronicles of Narnia by C.S. Lewis"],
        "mystery": ["The Girl With the Dragon Tattoo by Stieg Larsson", "Sherlock Holmes by Arthur Conan Doyle"],
        "science fiction": ["Dune by Frank Herbert", "Ender's Game by Orson Scott Card"],
        "romance": ["Pride and Prejudice by Jane Austen", "The Notebook by Nicholas Sparks"],
        "horror": ["It by Stephen King", "The Haunting of Hill House by Shirley Jackson"],
        "rock": ["Bohemian Rhapsody by Queen", "Blue Orchid by The White Stripes"],
        "pop": ["Shape of You by Ed Sheeran", "Blinding Lights by The Weeknd"],
        "classical": ["Moonlight Sonata by Beethoven", "Clair de Lune by Debussy"],
        "jazz": ["Take Five by Dave Brubeck", "So What by Miles Davis"],
        "happy": ["Happy by Pharrell Williams", "Can't Stop the Feeling by Justin Timberlake"],
        "sad": ["Someone Like You by Adele", "Fix You by Coldplay"],
        "relaxing": ["Weightless by Marconi Union", "Banana Pancakes by Jack Johnson"],
        "energetic": ["Eye of the Tiger by Survivor", "Stronger by Kanye West"],
        "j.k. rowling": ["Harry Potter series"],
        "stephen king": ["The Shining", "It"],
        "george orwell": ["1984", "Animal Farm"],
        "the beatles": ["Hey Jude", "Let It Be"],
        "queen": ["Bohemian Rhapsody", "We Will Rock You"],
        "taylor swift": ["Love Story", "Blank Space"]
    }

    # Check if any keyword in user_input matches predefined rules
    for keyword, items in recommendations.items():
        if keyword in user_input:
            return f"I recommend: {', '.join(items)}"

    # Default response if no match is found
    return "I'm sorry, I don't have a recommendation for that. Try another genre, mood, or artist."

# Interactive user input loop
def main():
    print("Welcome to the Book & Music Recommendation System!")
    print("Tell me what genre, mood, author, or artist you like, and I'll recommend something the best I can!")
    print("Type 'exit' to quit the program.\n")

    while True:
        user_query = input("What are you in the mood for? (book/music/artist/genre): ")
        
        if user_query.lower() == "exit":
            print("Goodbye! Enjoy your recommendations. 🎵📚")
            break

        # Get recommendation based on user input
        response = recommend_item(user_query)
        print(response, "\n")  # Display recommendation

# Run the system
if __name__ == "__main__":
    main()

