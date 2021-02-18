class StudentClass:

    def __init__(self, name, major, gpa):  # what attributes a student have - constructor
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
