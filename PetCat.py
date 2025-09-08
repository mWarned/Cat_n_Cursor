import cv2
import math
import time

class PetCat:
    def __init__(self):
        self.img = None
        self.window_visible = False
        self.window_name = "cat"
        self.load_image()

    def load_image(self) -> None:
        self.img = cv2.imread("img/pngegg.png", cv2.IMREAD_UNCHANGED)
        if self.img is None:
            print("Error: Could not load the image.")

    def show_cat(self) -> None:
        if self.img is None:
            return

        if not self.window_visible:
            cv2.namedWindow(self.window_name, flags=(cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_FREERATIO))
            cv2.setWindowProperty(self.window_name, cv2.WND_PROP_TOPMOST, 0)
            cv2.setWindowProperty(self.window_name, cv2.WND_PROP_FULLSCREEN, 1)
            cv2.resizeWindow(self.window_name, 100, 100)
            cv2.moveWindow(self.window_name, 910, 750)
            self.window_visible = True

        cv2.imshow(self.window_name, self.img)
        cv2.waitKey(1)

    def hide_cat(self) -> None:
        if self.window_visible:
            cv2.destroyWindow(self.window_name)
            self.window_visible = False

    def chases(self, cursorX: int, cursorY: int, speed: float = 8) -> None:
        cords = cv2.getWindowImageRect("cat")
        catX = cords[0] + int(cords[2] / 2)
        catY = cords[1] + int(cords[3] / 2)

        dx = cursorX - catX
        dy = cursorY - catY

        chase_distance = math.sqrt(dx*dx + dy*dy)

        if chase_distance > 50:
            new_x = int(catX + ((dx/chase_distance) * speed)) - 50
            new_y = int(catY + ((dy/chase_distance) * speed)) - 50

            cv2.moveWindow(self.window_name, new_x, new_y)