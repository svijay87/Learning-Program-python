from abc import ABC, abstractmethod

class ThreeDaysTrip(ABC):

    #All method remain abstract except one which will decide the flow of execution
    @abstractmethod
    def transport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def checkout(self):
        pass

    def itinerary(self):
        # In Template pattern, such function defined the execution way of methods
        print("Trip is started")
        self.transport()
        self.day1()
        self.day2()
        self.day3()
        # self.back_to_home()
        print("Trip is over")



class NorthTrip(ThreeDaysTrip):
    def transport(self):
        print("Choose the transport mode as per the location distance form home and as per holiday plan")

    def day1(self):
        print("Day-1: Activity")

    def day2(self):
        print("Day-2: Activity")

    def day3(self):
        print("Day-3: Activity")

    def checkout(self):
        print("Check out and go Home by air!")

    # def __call__(self, *args, **kwargs):
    #     print('NorthTrip Call method called')


if __name__ == "__main__":
    northtrip_obj = NorthTrip()
    northtrip_obj.itinerary()