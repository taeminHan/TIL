from pystray import MenuItem as item
from multiprocessing import Process, Queue
from PIL import Image
import pystray
import rotatescreen
import keyboard


def func1(q):
    if (not q.empty()) and str(q.get()) == 'stop':
        return False
    pass


def action():
    icon.stop()
    q.put('stop')


if __name__ == '__main__':
    q = Queue()
    p_func1 = Process(target=func1, args=(q,))
    p_func1.start()

    ##Below : Tray
    image = Image.open("result.jpg")
    menu = (item('종료', action),)
    icon = pystray.Icon("name", image, 'title', menu)
    icon.run()
    ##Up : Tray

    q.close()
    q.join_thread()

screen1 = rotatescreen.get_primary_display()
screen2 = rotatescreen.get_secondary_displays()

keyboard.add_hotkey('ctrl+alt+up', screen1.set_landscape, suppress=True)
keyboard.add_hotkey('ctrl+alt+right', screen1.set_portrait_flipped, suppress=True)
keyboard.add_hotkey('ctrl+alt+down', screen1.set_landscape_flipped, suppress=True)
keyboard.add_hotkey('ctrl+alt+left', screen1.set_portrait, suppress=True)

keyboard.add_hotkey('ctrl+shift+up', screen2[0].set_landscape, suppress=True)
keyboard.add_hotkey('ctrl+shift+right', screen2[0].set_portrait_flipped, suppress=True)
keyboard.add_hotkey('ctrl+shift+down', screen2[0].set_landscape_flipped, suppress=True)
keyboard.add_hotkey('ctrl+shift+left', screen2[0].set_portrait)

keyboard.wait()
