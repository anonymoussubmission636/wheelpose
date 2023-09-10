import pyautogui
import mouse
# enforces a pause duration
pyautogui.PAUSE = .3

def get_pos():
    pos = None
    # latch to only collect data after mouse release
    curr_pressed = False
    while True:
        if mouse.is_pressed("right"):
            if not curr_pressed:
                curr_pressed = True
        else:
            if curr_pressed:
                pos = pyautogui.position()
                break
    return pos

print("Hover over the toolbar of the file explorer with the folder of all fbx files generated by our script open. Right Click to select that position")
file_pos = get_pos()
print(f"File Explorer Toolbar Position: {file_pos}")

print("Hover over the toolbar of the inspector view on the fbx files. Right click to select that position.")
inspector_pos = get_pos()
print(f"Apply Position: {inspector_pos}")

print("Hover over the scene hierachy view. Make sure no fbx files need to be saved. Right click to select that position.")
scene_pos = get_pos()
print(f"Apply Position: {scene_pos}")

# actual process
n_fbx_done = 0

pyautogui.click(x=scene_pos[0], y=scene_pos[1])
pyautogui.click(x=file_pos[0], y=file_pos[1])
pyautogui.press("up", presses=1000)
# selects the first file. Hope you dont have too many!

print("Press Ctrl+C in the console when you've converted everything")
while True:
    # convert the animations to humanoid
    pyautogui.click(x=inspector_pos[0], y=inspector_pos[1])
    pyautogui.hotkey("tab", "enter", "down", "down", "down", "down", "enter", interval=.3)
    pyautogui.click(x=scene_pos[0], y=scene_pos[1])
    # break
    pyautogui.sleep(.3)
    pyautogui.hotkey("enter")
    n_fbx_done += 1
    # waiting for any compiling
    pyautogui.sleep(1)

    # go to next
    pyautogui.click(x=file_pos[0], y=file_pos[1])
    pyautogui.hotkey("enter")
    pyautogui.press("down", presses=n_fbx_done+1)