# take screenshots of the user's screen

# dependencies
import os, sys, pyautogui
from pynput import mouse

# TODO del me
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

class Camera:
    def __init__(self):
        self.border_txt_path = ".data/mouse_info/ss_bounds.txt"
        self.ss_img_path = ".data/images/ss.png"

        # try get the ss bounds
        with open(self.border_txt_path, "r") as file_object:
            try:
                x1, y1, x2, y2 = file_object.read().split(",")
                self.bounds_defined = True
            except Exception:
                self.bounds_defined = False

            else:
                self.left = int(x1)
                self.top = int(y1)
                self.width = int(x2)-int(x1)
                self.height = int(y2)-int(y1)

        self.cord_cache = []


    def __on_left_click(self, x, y, button, _pressed):
        """called when mouse click is detected

        Args:
            x ([int]): [mouse's x pos]
            y ([int]): [mouse's y pos]
            button ([no clue check pynput docs]): [tells which mouse button was pressed]
            _pressed ([prolly a bool idk]): [don't use it so I don't care]

        Returns:
            [bool]: [returns false when the mouse listener needs to be terminated]
        """

        # make sure this is a left click
        if button == mouse.Button.left:
            # add left-click position to the cache
            self.cord_cache.append(x)
            self.cord_cache.append(y)

            if len(self.cord_cache) == 4:
                # contruct the line
                line = ""
                for cord in self.cord_cache:
                    line += str(cord) + ','

                # remove hanging comma
                line = line [:len(line)-1]
                
                # write the line to a txt file
                with open(self.border_txt_path, "w") as file_object:
                    file_object.write(line)

                # end the mouse listener
                return False


    def define_borders(self):
        """start a mouse listener that records the (x, y) positions of 2 clciks
        before ending the mouse listener
        """

        # start the mouse listener
        self.listener = mouse.Listener(on_click=self.__on_left_click)
        self.listener.start()
        self.listener.join()

    def take_screen_shot(self):
        """take a screen shot using pyautogui and save it
        """
        if self.bounds_defined:
            pyautogui.screenshot(self.ss_img_path, region=( (self.left, self.top, self.width, self.height) ))
        else:
            print("Cannot take screenshot until bounds are defined")

if __name__ == "__main__":
    cam = Camera()

    cam.define_borders()

    cam.take_screen_shot()
