
# Here client need to initiate Cooking class and call method ready_food to prepare dish and
# no need to know how all internal processes works(i.e. cutting/boiling/frying).
# So Cooking is facade for client

class Cooking:
    def ready_food(self) -> None:
        self.cutter = Cutter()
        self.cutter.cutvegetables()

        self.boiler = Boiler()
        self.boiler.boilvegetables()

        self.frier = Frier()
        self.frier.fry()


class Cutter:

    def cutvegetables(self) -> None:
        print("All vegetables are cut")


class Boiler:

    def boilvegetables(self) -> None:
        print("All vegetables are boiled")


class Frier:
    def fry(self) -> None:
        print("All vegetables are fried now.")


if __name__ == "__main__":
    cook = Cooking()
    cook.ready_food()
