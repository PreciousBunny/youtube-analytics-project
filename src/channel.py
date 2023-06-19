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
        self.youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY).channels(). \
            list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube, indent=2, ensure_ascii=False))
