from maix import camera, display, app, image, time, sys

print("MaixPy:", sys.maixpy_version(), "OS:", sys.os_version())

cam = None
try:
    disp = display.Display()
    cam = camera.Camera(640, 480)
    fps = getattr(time, "fps", None)
    if callable(fps):
        fps()  # Start measuring preview loop intervals.
    print("Preview started. Use MaixVision Stop to exit.")

    while not app.need_exit():
        img = cam.read()
        if img is None:
            continue

        width = img.width()
        height = img.height()
        img.draw_cross(width // 2, height // 2, image.COLOR_GREEN,
                       size=20, thickness=2)
        img.draw_string(8, 8, "W: {}  H: {}".format(width, height),
                        image.COLOR_WHITE)
        if callable(fps):
            img.draw_string(8, 32, "Loop FPS: {:.1f}".format(fps()),
                            image.COLOR_WHITE)
        disp.show(img)
except KeyboardInterrupt:
    print("Preview interrupted.")
finally:
    if cam is not None:
        cam.close()
        print("Camera closed.")
