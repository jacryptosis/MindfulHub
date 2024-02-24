class CommunityForum:
    def __init__(self):
        self.threads = []

    def create_thread(self, title, author, content):
        thread = {
            'title': title,
            'author': author,
            'content': content,
            'comments': []
        }
        self.threads.append(thread)

    def get_threads(self):
        return self.threads

    def add_comment(self, thread_title, author, content):
        for thread in self.threads:
            if thread['title'] == thread_title:
                comment = {
                    'author': author,
                    'content': content
                }
                thread['comments'].append(comment)
                break
