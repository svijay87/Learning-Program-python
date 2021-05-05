'''
Command Design Pattern (Behavioral Design Pattern)
Source : http://www.aaravtech.com/articles/
'''

from abc import ABC, abstractmethod


class BaseCommannd(ABC):

    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")


class EMailCommand(BaseCommannd):

    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_email(self.data)


class SMSCommand(BaseCommannd):

    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_sms(self.data)


class NotificationService:

    def send_email(self, data):
        print("Sending email", data)

    def send_sms(self, data):
        print("Sending short message", data)


class NotificationInvoker:

    def __init__(self):
        self.notification_history = []

    def invoke(self, command):
        print(command)
        self.notification_history.append(command)
        command.execute()


if __name__ == "__main__":

    invoker = NotificationInvoker()
    sender = NotificationService()
    invoker.invoke(EMailCommand(sender, {"subject": "Test Email"}))
    invoker.invoke(SMSCommand(sender, {"subject": "Test SMS"}))
