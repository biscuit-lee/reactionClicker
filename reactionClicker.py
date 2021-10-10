# a simple script for autoclicking that reaction time app
from PIL import ImageGrab 
import mouse

def main():
    while True:
        mouse_pos = mouse.get_position()
        pixel_color = ImageGrab.grab().load()[mouse_pos[0],mouse_pos[1]]
        
        # if color matches
        if pixel_color == (99, 219, 100):
            mouse.click()
            break
        else:
            pass
        print(pixel_color)



if __name__ == "__main__":
    main()