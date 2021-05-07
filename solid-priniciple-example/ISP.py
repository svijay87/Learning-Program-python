"""
Interface Segregation Principle
Make fine grained interfaces that are client specific
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.
"""

from abc import ABC,abstractmethod

class PlaySongs:
    def __init__(self, title):
        self.title = title

    def play_drums(self):
        print("Ba-dum ts")

    def play_guitar(self):
        print("*Soul-moving guitar solo*")

    def sing_lyrics(self):
        print("NaNaNaNa")

# This class is fine, just changing the guitar and lyrics
class PlayRockSongs(PlaySongs):
    def play_guitar(self):
        print("*Very metal guitar solo*")

    def sing_lyrics(self):
        print("I wanna rock and roll all night")

# This breaks the ISP, we don't have lyrics
class PlayInstrumentalSongs(PlaySongs):
    def sing_lyrics(self):
        raise Exception("No lyrics for instrumental songs")


# A good example
# we only have the interfaces we need, we cannot call sing lyrics on instrumental songs.

class PlaySongsLyrics(ABC):
    @abstractmethod
    def sing_lyrics(self, title):
        pass

class PlaySongsMusic(ABC):
    @abstractmethod
    def play_guitar(self, title):
        pass    @abstractmethod
    def play_drums(self, title):
        pass

class PlayInstrumentalSong(PlaySongsMusic):
    def play_drums(self, title):
        print("Ba-dum ts")

    def play_guitar(self, title):
        print("*Soul-moving guitar solo*")

class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):
    def play_guitar(self):
        print("*Very metal guitar solo*")

    def sing_lyrics(self):
        print("I wanna rock and roll all night")

    def play_drums(self, title):
        print("Ba-dum ts")