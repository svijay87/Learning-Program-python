
class PropertyLearn1:

    def __init__(self):
        self._subject = 'Bio'

    @property
    def subj(self):
        print('Getter method called')
        return self._subject

    @subj.setter
    def subj(self, val):
        if val is None:
            raise ValueError('Subject can not be empty')
        print('Setter method called')
        self._subject = val

subject = PropertyLearn1()
subject.subj = 'English Honors'

print(subject.subj)