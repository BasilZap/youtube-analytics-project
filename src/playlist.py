import datetime
import src.channel


class PlayList:

    def __init__(self, playlist_id):
        playlist_data = src.channel.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails,snippet',
                                                                 maxResults=50,
                                                                 ).execute()
        self.title = playlist_data['items'][0]['snippet']['title']
        self.__id = playlist_id
        self.url = f"https://www.youtube.com/playlist?list={self.__id}"


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(pl.title)
print(pl.url)
print(src.channel.youtube.playlists().list(playlistId='PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw',
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute())
