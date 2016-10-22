import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
leap_dir = 'LeapSDK/lib/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, leap_dir)))

import Leap

pyAutoGUI_dir = 'PyAutoGUI-0.9.33/'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, pyAutoGUI_dir)))
import pyautogui

screenWidth, screenHeight = pyautogui.size()


prevFingers = 0

class PointerListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        global prevFingers
        hands = frame.hands
        if(hands):
            hand = hands[0]
            hand_center = hand.stabilized_palm_position

            # Click functionality
            fingers = hand.fingers
            extended = 0
            for finger in fingers:
                if finger.is_extended:
                    extended += 1
            if (extended == 5 and prevFingers == 5 and hand.confidence > .9):
                pyautogui.click()
                time.sleep(.5)

            elif (extended == 3 and prevFingers == 3 and hand.confidence > .9):
                pyautogui.click(button="right")
                time.sleep(.5)

            prevFingers = extended
            #print('Fingers:' + str(extended) + ' Confidence: ' + str(hand.confidence))

            if (extended < 1):
                xRadius = 100
                yRadius = 80
                pyautogui.moveTo((hand_center.x + xRadius) * screenWidth / (2 * xRadius), screenHeight - (hand_center.y - 150) * screenHeight / (2 * yRadius))


            # Click functionality
            fingers = hand.fingers
            extended = 0
            for finger in fingers:
                if finger.is_extended:
                    extended += 1
            if (extended == 5 and prevFingers == 5 and hand.confidence > .9):
                pyautogui.click()
                time.sleep(.5)

            elif (extended == 3 and prevFingers == 3 and hand.confidence > .9):
                pyautogui.click(button="right")
                time.sleep(.5)

            prevFingers = extended
            #print('Fingers:' + str(extended) + ' Confidence: ' + str(hand.confidence))

            if (extended < 1):
                xRadius = 100
                yRadius = 80
                pyautogui.moveTo((hand_center.x + xRadius) * screenWidth / (2 * xRadius), screenHeight - (hand_center.y - 150) * screenHeight / (2 * yRadius))

            # scrolling functionality
            gestures = frame.gestures()
            for gesture in gestures:
                circle = Leap.CircleGesture(gesture)
                if (circle):
                    if (circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2):
                        pyautogui.scroll(-5)
                    else:
                        pyautogui.scroll(5)

def main():
    listener = PointerListener()
    controller = Leap.Controller()
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    controller.add_listener(listener)
    controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
    pyautogui.FAILSAFE = False

    while (True):
        None

    controller.remove_listener(listener)

if __name__ == "__main__":
    main()
