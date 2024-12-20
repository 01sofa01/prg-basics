class SocialMediaProfile:
    def __init__(self, username):
        """Initializes the social media profile with a username and an empty list of posts."""
        self.username = username
        self.posts = []

    def add_post(self, content):
        """Adds a new post to the profile."""
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        """Displays the user's timeline with numbered posts."""
        print(f"{self.username}'s Timeline:")
        if self.posts:
            for i, post in enumerate(self.posts, 1):  # Enumerate for numbering the posts starting from 1
                print(f"{i}. {post}")
        else:
            print(f"{self.username} has no posts yet.")
        
# Create a social media profile for the user 'johndoe'
johndoe = SocialMediaProfile("johndoe")

# Add posts to 'johndoe's profile
johndoe.add_post("Hello, world!")
johndoe.add_post("Had a great day at the park!")
johndoe.add_post("What's up, Natalie? How are you?")

# Display 'johndoe's timeline
johndoe.display_timeline()
