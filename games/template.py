from src.TwitchPlays_KeyCodes import *
import pydirectinput

def handle_message(msg):  # do not rename this function. it has to be "handle_message"
    # Now that you have a chat message, this is where you add your game logic.
    # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
    # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
    # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
    # Use the pydirectinput library to press or move the mouse

    # If the chat message is "left", then hold down the A key for 2 seconds
    if msg == "left":
        HoldAndReleaseKey(A, 2)

    # If the chat message is "right", then hold down the D key for 2 seconds
    if msg == "right":
        HoldAndReleaseKey(D, 2)

    # If message is "drive", then permanently hold down the W key
    if msg == "drive":
        ReleaseKey(S)  # release brake key first
        HoldKey(W)  # start permanently driving

    # If message is "reverse", then permanently hold down the S key
    if msg == "reverse":
        ReleaseKey(W)  # release drive key first
        HoldKey(S)  # start permanently reversing

    # Release both the "drive" and "reverse" keys
    if msg == "stop":
        ReleaseKey(W)
        ReleaseKey(S)

    # Press the spacebar for 0.7 seconds
    if msg == "brake":
        HoldAndReleaseKey(SPACE, 0.7)

    # Press the left mouse button down for 1 second, then release it
    if msg == "shoot":
        pydirectinput.mouseDown(button="left")
        time.sleep(1)
        pydirectinput.mouseUp(button="left")

    # Move the mouse up by 30 pixels
    if msg == "aim up":
        pydirectinput.moveRel(0, -30, relative=True)

    # Move the mouse right by 200 pixels
    if msg == "aim right":
        pydirectinput.moveRel(200, 0, relative=True)