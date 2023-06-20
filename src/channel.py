import json
import os
import isodate
from googleapiclient.discovery import build
from src.config import YOUTUBE_API_KEY


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel_title = self.youtube['items'][0]['snippet']['title']
        self.channel_description = self.youtube['items'][0]['snippet']['description']
        self.channel_url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(self.youtube['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.youtube['items'][0]['statistics']['videoCount'])
        self.total_view_count = int(self.youtube['items'][0]['statistics']['viewCount'])

    @classmethod
    def get_service(cls):
        """
        Метод возвращает объект для работы с YouTube API.
        """
        return build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    def to_json(self, file_path: str) -> None:
        """
        Метод сохраняет в JSON-файлe значения атрибутов экземпляра "Channel".
        """
        channel_data = {
            'channel_id': self.channel_id,
            'channel_title': self.channel_title,
            'channel_description': self.channel_description,
            'channel_url': self.channel_url,
            'subscriberCount': self.subscriber_count,
            'videoCount': self.video_count,
            'viewCount': self.total_view_count
        }
        with open(file_path, 'w') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube, indent=2, ensure_ascii=False))
