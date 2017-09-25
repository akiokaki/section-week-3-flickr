import json

class Photo(object):
    def __init__(self, photo_dictionary):
        self.owner = {
            'username':
            photo_dictionary['owner']['username'],
            'realname':
            photo_dictionary['owner']['realname'],
            'location':
            photo_dictionary['owner']['username']
        }
        self.title = photo_dictionary['title']['_content']
        self.tags =[]
        for tag in photo_dictionary['tags']['tag']:
            self.tags.append(tag['raw'])
        self.views = photo_dictionary['views']
        self.url = photo_dictionary['urls']['url'][0]['_content']
        self.license = photo_dictionary['license']

    def __str__(self):
        return "Title is {0}, URL at {1}".format(self.title,self.url)

    def __repr__(self):
        return "ID = {0}, Title = {1}, URL = {2}".format(self.id, self.title, self.url)

    def __contains__(self, test_string):
        # enables in operator for this object
        return (
            test_string in self.tags 
            or test_string in self.title
        )

with open("sample_diction.json","r") as f:
    # all the stuff below can access f, but outside, it cannot
    # this no longer requires you to close the file everytime
    f_string = f.read()
    response_diction = json.loads(f_string)

pd = response_diction["photo"]
photo = Photo(pd)
print(photo)
if "Nature" in photo:
    print('Nature is in photo')