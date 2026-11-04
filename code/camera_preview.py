from maix import camera, display, app

disp = display.Display()
cam = camera.Camera(640, 480)
while not app.need_exit():
    img = cam.read()
    disp.show(img)
