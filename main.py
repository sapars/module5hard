from user import User
from video import Video
from tube import UrTube
from notes_v import *


# def add_video(*movs: tuple):
#     videos: list[Video] = []
#     for i in movs:
#         videos.append(Video(*i))
#     return videos
#
# videos = add_video(*movs)



tube = UrTube()
tube.add_video(*movs)
print(tube.get_videos('z'))
tube.watch_video()
#
# print(tube.video_titles)
# # tube.register_new_user(user1)
# print(tube)
