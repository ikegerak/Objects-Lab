class Song:
    def __init__(self, title, artist, length):
        self.title = title
        self.artist = artist
        self.length = int(length)
        
class Playlist:
    songs = {}
    def __init__(self,playlist):
        self.title = playlist

    def load_songs(self,list):
        with open(list, "r") as f:
            lines = f.readlines()

        count = 1
        for line in lines:
            temp = line.replace("\n","").split(",")
            self.songs["song" + str(count)] = Song(temp[0].strip(),temp[1].strip(),temp[2].strip())
            count += 1

    def add_song(self,song):
        self.songs["song" + str(len(self.songs)+1)] = song

    def print_playlist(self):
        print(f"{str(self.title).upper()}\n--------------------")
        for song in self.songs:
            print(f"{self.songs[song].title},{self.songs[song].artist}")

    def get_total_duration(self):
        seconds = 0
        minutes = 0
        for song in self.songs:
            seconds += self.songs[song].length      
        while seconds >= 60:
            seconds -= 60
            minutes += 1
        seconds = str(seconds)
        if len(seconds) == 1:
            seconds = "0" + seconds
        print(f"{minutes}:{seconds}")

    def find_by_artist(self,artist):
        artists_songs = []
        for song in self.songs:
            if self.songs[song].artist == artist:
                artists_songs.append(f"{self.songs[song].title},{self.songs[song].artist}")
        print(f"SONGS BY {str(artist).upper()}\n--------------------")
        for song in artists_songs:
            print(song)


playlist = Playlist("My Playlist")
playlist.load_songs("songs.csv")
playlist.add_song(Song("My Fav Song", "Megabytes", 250))
playlist.print_playlist()
playlist.get_total_duration()
playlist.find_by_artist("Null Pointer")