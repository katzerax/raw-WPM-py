from pynput import keyboard
import time
keys = 0

def on_press(key):
    global keys
    if key == keyboard.Key.esc:
        return False
    keys += 1

def measure_wpm():
    global keys
    start_time = time.time()
    with keyboard.Listener(on_press=on_press) as listener:
        while listener.running:
            kps = keys / (time.time() - start_time)
            wpm = (kps / 5) * 60
            print("Current WPM: ", round(wpm, 2), "Keystroke Count:", keys, "Time elapsed:", round(time.time() - start_time,1))
            time.sleep(1)
    end_time = time.time()
    avg_wpm = (keys/5) / (end_time - start_time) * 60
    print("Average WPM:", round(avg_wpm, 2))
    return avg_wpm

print("Measuring words... Press esc to stop")
while True:
    avg_wpm = measure_wpm()
    print("Do you want to restart the test? Press y to restart or any other key to exit.")
    if input() != 'y':
        break