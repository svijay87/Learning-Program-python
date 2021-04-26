
class PropertyLearn:

    def __init__(self):
        self._subject = 'Bio'

    def get_subj(self):
        print('Getter method called')
        return self._subject

    def set_subj(self, val):
        print('Setter method called')
        self._subject = val

    def del_subj(self):
        del self._subject


    subj = property(get_subj,set_subj,del_subj)


subject = PropertyLearn()
subject.subj = 'Math'

print(subject.subj)