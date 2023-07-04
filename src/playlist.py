from src.channel import Channel
from datetime import timedelta


class PlayList:
    """
    Класс для отображения информации о плейлисте.
    """

    def __init__(self, playlist_id):
        """
        Инициализирует экземпляр класса PlayList.
        """
        self.__playlist_id = playlist_id
        self.title = None
        self.url = None
        self.videos = None
        self.get_playlist_data()

    def get_playlist_data(self):
        """
        Метод получает данные и статистику плейлиста по его id.
        """
        youtube = Channel.get_service().playlistItems().list(
            playlistId=self.__playlist_id,
            part='snippet,contentDetails,id,status',
            maxResults=50,
        ).execute()

        playlist_data = youtube.get('items')[0]
        self.title = playlist_data.get('snippet').get('title').split(".")[0]
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

        video_ids = [video['contentDetails']['videoId'] for video in youtube['items']]
        video_response = Channel.get_service().videos().list(
            part='contentDetails,statistics',
            id=','.join(video_ids)
        ).execute()
        self.videos = video_response.get('items')

    @property
    def playlist_id(self):
        """
        Метод для доступа к приватному атрибуту с геттером для идентификатора плейлиста.
        """
        return self.__playlist_id

    @property
    def total_duration(self):
        """
        Метод возвращает объект класса "datetime.timedelta" с суммарной длительность плейлиста.
        """
        total_duration = timedelta()
        for video in self.videos:
            duration = video.get('contentDetails').get('duration')
            video_duration = self.transform_duration(duration)
            total_duration += video_duration
        return total_duration

    def transform_duration(self, duration):
        """
        Метод преобразует длительность видео в объект класса "timedelta".
        """
        parts = duration.split('T')
        time_part = parts[1]
        hours = int(time_part.split('H')[0]) if 'H' in time_part else 0
        minutes = int(time_part.split('M')[0].split('H')[-1]) if 'M' in time_part else 0
        seconds = int(time_part.split('S')[0].split('M')[-1]) if 'S' in time_part else 0
        video_duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return video_duration

    def show_best_video(self):
        """
        Метод возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков).
        """
        best_video = max(self.videos, key=lambda video: video.get('statistics').get('likeCount'))
        video_id = best_video.get('id')
        return f'https://youtu.be/{video_id}'
