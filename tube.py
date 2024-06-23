from user import User
from video import Video
from time import sleep


class UrTube:
    users: list[User] = []
    videos: list[Video] = []
    video_titles: list[str] = []
    current_user: User = None

    @classmethod
    def register_new_user(cls, new_user: User):
        for i in cls.users:
            if i == new_user:
                print(f'user {new_user.user_name} already exists. '
                      f'Try another nickname\n'
                      f'_____________________')
                return
        cls.users.append(new_user)
        cls.current_user = new_user

    @classmethod
    def log_in(cls, nick_name, password):
        for i in cls.users:
            if i.user_name == nick_name:
                if i.user_hash == hash(password):
                    cls.current_user = i
                    return
                print(f'incorrect password.\n'
                      f'try another one')
                return
            print(f'user {nick_name} not found.\n'
                  f'check spelling or try to register')
            return

    @classmethod
    def log_out(cls):
        cls.current_user = None

    def __str__(self) -> object:
        return (f'Users registered: {len(self.users)}\n'
                f'Videos uploaded: {len(self.videos)}\n')

    @classmethod
    def add_video(cls, *videos: Video):
        for i in videos:
            if i.title in cls.video_titles:
                print(f'Video {i.title} already exists. Try another one')
                continue
            cls.videos.append(i)
            cls.video_titles.append(i.title)

    @classmethod
    def add_video(cls, *videos: tuple):
        for i in videos:
            if i[0] in cls.video_titles:
                print(f'Video {i[0]} already exists. Try another one')
                continue
            cls.videos.append(Video(*i))
            cls.video_titles.append(i[0])

    @classmethod
    def get_videos(cls, search: str):
        search_result: list[str] = []
        for i in cls.video_titles:
            if i.lower().__contains__(search.lower()):
                search_result.append(i)
        return search_result

    @classmethod
    def watch_video(cls, title):

        current_time = 0
        print('the movie is on for:\n')
        while(1):
            sleep(1)
            current_time += 1
            print(f'{current_time} seconds')
            if input():
                continue

    @classmethod
    def users_info(cls):
        return cls.users

    @classmethod
    def video_info(cls):
        return cls.video_titles
