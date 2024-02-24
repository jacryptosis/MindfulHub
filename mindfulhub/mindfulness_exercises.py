class MindfulnessExercises:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, title, description, duration, audio_url):
        exercise = {
            'title': title,
            'description': description,
            'duration': duration,
            'audio_url': audio_url
        }
        self.exercises.append(exercise)

    def get_exercises(self):
        return self.exercises

    def customize_exercise(self, title, duration):
        for exercise in self.exercises:
            if exercise['title'] == title:
                exercise['duration'] = duration
                break
