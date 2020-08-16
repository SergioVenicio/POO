from abc import ABCMeta, abstractproperty


class Moody(metaclass=ABCMeta):
    @abstractproperty
    def mood():
        raise Exception('mood not found!')

    def query_mood(self):
        print(f"I'm feel {self.mood} today!!!")


class Happy(Moody):
    @property
    def mood(self):
        return 'happy'

    def laugh(self):
        print('jkjdhhhhqiwhdqdui')


class Sad(Moody):
    @property
    def mood(self):
        return 'sad'

    def cry(self):
        print('wahhhhhhh boooo hoooo')


class Psychiatrist:
    def examine(self, patient: Moody):
        print('DOCTOR: How d u feel ?')
        print('PATIENT:')
        patient.query_mood()

    def observe(self, patient: Moody):
        if isinstance(patient, Happy):
            patient.laugh()
        else:
            patient.cry()

        print(f'This patient is {patient.mood}')

    def comment(self):
        print('U are crazy!')
