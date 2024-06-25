from MD_file import view_modes


class Video:
    video_count = 0

    def __init__(self, title: str = "Yet another video", duration: int = 600, time_now: int = 0, adult_mode: bool = False):
        print(f'New video {title} was added')
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.video_count += 1

    def info(self):
        print(self.title, self.time_now)

    def __str__(self):
        return (f'Video: {self.title}\n'
                f'Duration: {self.duration}'
                f'\n{view_modes[self.adult_mode]}\n'
                f'_________________________')

    def __del__(self):
        if Video.video_count:
            # print(f'Video {self.title} was deleted')
            Video.video_count -= 1
