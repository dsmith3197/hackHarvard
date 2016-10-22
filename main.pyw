import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
leap_dir = 'LeapSDK/lib/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))

import Leap

pyAutoGUI_dir = 'PyAutoGUI-0.9.33/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, pyAutoGUI_dir)))
import pyautogui

screenWidth, screenHeight = pyautogui.size()

timeMax = 5
timeout = timeMax

class PointerListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        global timeout, timeMax
        hands = frame.hands
        if(hands):
            hand = hands[0]
            hand_center = hand.stabilized_palm_position
            xRadius = 100
            yRadius = 80
            pyautogui.moveTo((hand_center.x + xRadius) * screenWidth / (2 * xRadius), screenHeight - (hand_center.y - 150) * screenHeight / (2 * yRadius))

            # if (len(hands) == 2):
            #     pyautogui.mouseDown()
            #
            # else:
            #     pyautogui.mouseUp()


            #checking for clicking if all fingers are extended
            # fingers = hand.fingers
            # if fingers:
            #     print(fingers.length)
            # extendedCounter = 0
            #
            # for x in fingers:
            #     if x.extended():
            #         extendedCounter += 1
            #
            # if extendedCounter == 5:
            #     pyautogui.click()




def main():
    listener = PointerListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    pyautogui.FAILSAFE = False

    while (True):
        None

    controller.remove_listener(listener)

if __name__ == "__main__":
    main()
