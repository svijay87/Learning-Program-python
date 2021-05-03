
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} got message {message}')



class Publisher:
    def __init__(self):
        self.subscriber = set()

    def register(self, user):
        self.subscriber.add(user)

    def unregister(self, user):
        self.subscriber.discard(user)

    def dispatch(self, msg):
        for sub in self.subscriber:
            sub.update(msg)

