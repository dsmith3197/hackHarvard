import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
leap_dir = 'LeapSDK/lib/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))

import Leap

pyAutoGUI_dir = 'PyAutoGUI-0.9.33/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, pyAutoGUI_dir)))
import pyautogui

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        screenWidth, screenHeight = pyautogui.size()

        hands = frame.hands
        if(hands):
            hand = hands[0]
            hand_center = hand.stabilized_palm_position
            xRadius = 150
            yRadius = 100
            pyautogui.moveTo((hand_center.x + xRadius) * screenWidth / (2 * xRadius), screenHeight - (hand_center.y - yRadius) * screenHeight / (2 * yRadius))


            #checking for clicking if all fingers are extended
            fingers = hand.fingers

            extendedCounter = 0
            for x in fingers:
                if x.extended:
                    extendedCounter++

            if extendedCounter == 5:
                pyautogui.click()



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
