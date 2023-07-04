import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    print(pl.title)
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"
    print(pl.url)

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    print(str(duration))
    assert isinstance(duration, datetime.timedelta)
    print(isinstance(duration, datetime.timedelta))
    assert duration.total_seconds() == 6592.0
    print(duration.total_seconds())

    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
    print(pl.show_best_video())
