class Games:
    def __init__(self, title):
        self.title = title

    def play_cricket(self):
        print("Gentleman game")

    def play_hockey(self):
        print("National game")

    def coaching_football(self):
        print("Football coaching for everyone in east india.")

# This class is fine, just changing the guitar and lyrics
class PlayRockSongs(Games):
    def play_hockey(self):
        print("*Playing hockey on national level*")

    def coaching_football(self):
        print("I wanna teach football over this weekend")

# This breaks the ISP, we don't have football program for north India
class PlayFootballNorthIndia(Games):
    def coaching_football(self):
        raise Exception("No program for North India")
