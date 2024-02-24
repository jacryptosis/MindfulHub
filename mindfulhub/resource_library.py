class ResourceLibrary:
    def __init__(self):
        self.resources = []

    def add_resource(self, title, author, url, tags):
        resource = {
            'title': title,
            'author': author,
            'url': url,
            'tags': tags
        }
        self.resources.append(resource)

    def browse_resources(self):
        return self.resources

    def search_resources(self, keyword):
        return [resource for resource in self.resources if keyword in resource['title'] or keyword in resource['tags']]

    def rate_resource(self, title, rating):
        for resource in self.resources:
            if resource['title'] == title:
                resource['rating'] = rating
                break

    def review_resource(self, title, review):
        for resource in self.resources:
            if resource['title'] == title:
                if 'reviews' not in resource:
                    resource['reviews'] = []
                resource['reviews'].append(review)
                break
