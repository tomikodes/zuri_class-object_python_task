from webbrowser import get


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, newName) :
        self.newName = newName

    def change_age(self, newAge) :
        self.newAge = newAge
    
    def add_track(self, new_track) :
        self.new_track = new_track
        self.tracks.append(new_track)

# i'm, appending the new track to to the tracks list 
        

    def get_score(self, newScore) :
        return self.score
    
# since you did'nt pass a new arguement fot the get_score method,
# i'm returning the student score that was passed in the object instant


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(20.90)
