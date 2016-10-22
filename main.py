import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
leap_dir = 'LeapSDK/lib/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))

import Leap

pyAutoGUI_dir = 'PyAutoGUI-0.9.33/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, pyAutoGUI_dir)))
import pyautogui

class SampleListener(Leap.Listener):
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()


    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()

        hands = frame.hands
        if(hands):
            hand = hands[0]
            hand_center = hand.palm_position;
            pyautogui.moveTo(hand_center.x, screenHeight - hand_center.y)

def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    pyautogui.FAILSAFE = False

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
