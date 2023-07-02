from src.channel import Channel


class Video:
    """
    Класс для получения информации о видео.
    """

    def __init__(self, video_id):
        """
        Инициализирует экземпляр класса Video.
        """
        self.__video_id = video_id
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None
        self.video_response()

    def video_response(self):
        """
        Метод получает данные и статистику видео по его id.
        """
        youtube = Channel.get_service().videos().list(
            part='snippet,statistics', id=self.__video_id
        ).execute()
        video_data = youtube.get('items')[0]
        self.title = video_data.get('snippet').get('title')
        self.url = f'https://www.youtube.com/watch?v={self.__video_id}'
        self.view_count = int(video_data.get('statistics').get('viewCount'))
        self.like_count = int(video_data.get('statistics').get('likeCount'))

    @property
    def video_id(self):
        """
        Метод для доступа к приватному атрибуту с геттером.
        """
        return self.__video_id

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей.
        """
        return self.title


class PLVideo(Video):
    """
    Класс для получения информации о видео в плейлистe.
    """

    def __init__(self, video_id, playlist_id):
        """
        Инициализирует экземпляр класса PLVideo.
        """
        self.playlist_id = playlist_id
        super().__init__(video_id)
