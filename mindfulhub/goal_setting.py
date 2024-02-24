class GoalSetting:
    def __init__(self):
        self.goals = []

    def add_goal(self, title, description, deadline):
        goal = {
            'title': title,
            'description': description,
            'deadline': deadline,
            'progress': 0
        }
        self.goals.append(goal)

    def get_goals(self):
        return self.goals

    def update_progress(self, title, progress):
        for goal in self.goals:
            if goal['title'] == title:
                goal['progress'] = progress
                break
