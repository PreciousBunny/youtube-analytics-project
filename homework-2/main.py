from src.channel import Channel
from src.config import CHANNEL_ID

if __name__ == '__main__':
    moscowpython = Channel(CHANNEL_ID)

    # получаем значения атрибутов
    print(moscowpython.channel_title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.channel_url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # moscowpython.print_info()

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')
