class student:
    marks_bonus =1.5
    def __init__(self,first_name,last_name,marks):
        self.first_name=first_name
        self.last_name=last_name
        self.marks=marks
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name,self.last_name)
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def dummy(self):
        self.marks