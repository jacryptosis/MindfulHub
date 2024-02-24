class DailyInspiration:
    def __init__(self):
        self.inspirations = []

    def add_inspiration(self, quote, author, date):
        inspiration = {
            'quote': quote,
            'author': author,
            'date': date
        }
        self.inspirations.append(inspiration)

    def get_inspirations(self):
        return self.inspirations

    def personalize_inspirations(self, user_preferences):
        # Implement personalization logic here
        pass
