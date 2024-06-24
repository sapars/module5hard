view_modes = {True: 'Viewer discretion is advised',
              False: 'Appropriate for all ages'
              }
if __name__ == "__main__":
    import keyboard
    from time import sleep

    current_time = 0
    print('the movie is on for:\n')
    while 1:
        sleep(1)
        current_time += 1
        print(f'{current_time} seconds')
        keyboard.wait('1')


