class SongLink(object):

    def __init__(self,url,songTitle,songArtist,songAlbum="",songAlbumArtist=""):
        self.__url = url
        self.__songTitle = songTitle
        self.__songArtist = songArtist
        self.__songAlbum = songAlbum
        self.__songAlbumArtist = songAlbumArtist
        self.__youtube_dl_Output_Name = songArtist + " - " + songTitle

    def get__url(self):
        return self.__url

    def set__url(self, url):
        self.__url = url

    def get__songTitle(self):
        return self.__songTitle

    def set__songTitle(self, songTitle):
        self.__songTitle = songTitle

    def get__songArtist(self):
        return self.__songArtist

    def set__songArtist(self,songArtist):
        self.__songArtist = songArtist

    def get__songAlbum(self):
        return self.__songAlbum

    def set__songAlbum(self,songAlbum):
        self.__songAlbum - songAlbum

    def get__songAlbumArtist(self):
        return self.__songAlbumArtist

    def set__songAlbumArtist(self,songAlbumArtist):
        self.__songAlbumArtist = songAlbumArtist

    def get__youtube_dl_Output_Name(self):
        return self.__youtube_dl_Output_Name

    def set__youtube_dl_Output_Name(self,youtube_dl_Output_Name):
        self.__youtube_dl_Output_Name = youtube_dl_Output_Name
