import start_game
import reload_or_stop


while True:
    start_game.start()
    if reload_or_stop.reload_or_stop_game() == '0':
        break
    print('\n' * 12)
