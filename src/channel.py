import os.path
import json
from googleapiclient.discovery import build

JSON_FILE_PATH = '../src/moscowpython.json'

api_key: str = os.getenv('YOUTUBE_EXCHANGE_DATA_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel_data = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.__channel_data["items"][0]["snippet"]["title"]
        self.description = self.__channel_data["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = int(self.__channel_data["items"][0]["statistics"]["subscriberCount"])
        self.video_count = self.__channel_data["items"][0]["statistics"]["videoCount"]
        self.view_count = self.__channel_data["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        """
        Вывод информации о канале
        """
        return f"'{self.title} ({self.url})'"

    def __add__(self, other):
        """
        Операция сложения каналов
        """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """
        Операция вычитания каналов
        """
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        """
        Операция сравнения каналов <
        """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """
        Операция сравнения каналов <=
        """
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """
        Операция сравнения каналов >
        """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """
        Операция сравнения каналов >=
        """
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        """
        Операция сравнения каналов ==
        """
        return self.subscriber_count == other.subscriber_count

    @classmethod
    def get_service(cls):
        return youtube

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel_data, indent=2, ensure_ascii=False))

    def to_json(self, json_file_name) -> None:
        """
        Формирование строки с данными и запись в json
        """
        json_path = '../src/' + json_file_name      # Формируем путь к файлу

        # Формируем строку для записи
        json_str = {
                   "channel_id": {self.__channel_id},
                   "title": {self.title},
                   "description": {self.description},
                   "url": {self.url},
                   "subscriber_count": {str(self.subscriber_count)},
                   "video_count": {self.video_count},
                   "view_count": self.view_count
                   }

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(json_str, json_file, ensure_ascii=False, indent=4)
            json_file.close()
