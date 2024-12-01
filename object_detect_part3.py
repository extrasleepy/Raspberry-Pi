from gpiozero import LED
from picamera2 import Picamera2
import cv2
import numpy as np
import time

# Initialize the LED
red_led = LED(21)

# Start with LED off
red_led.off()
led_on = False

# Initialize the camera
print("[INFO] Waiting for camera to warm up...")
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(camera_config)
picam2.start()
time.sleep(2.0)

# Define the lower and upper boundaries of the object
color_lower = (167, 100, 100)
color_upper = (187, 255, 255)

print("[INFO] Starting video stream...")
try:
    while True:
        # Capture a frame from the camera
        frame = picam2.capture_array()

        # Rotate and correct colors
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to HSV and create mask
        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv, color_lower, color_upper)

        # Display mask for debugging
        cv2.imshow("Mask", mask)

        # Process contours
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Debugging: Check if contours are found
        if len(contours) > 0:
            print(f"Contours found: {len(contours)}")

            # Find the largest contour
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Debugging: Print radius and center information
            print(f"Radius: {radius}, Center: ({x}, {y})")

            # Compute moments to find the center
            M = cv2.moments(c)
            if M["m00"] > 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                print(f"Object center: {center}")

                # Only proceed if the radius meets a minimum size
                if radius > 5:  # Adjusted radius threshold
                    # Draw the circle and centroid on the frame
                    cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)

                    # Turn the LED on if it is not already on
                    if not led_on:
                        red_led.on()
                        led_on = True
            else:
                print("Contour moments invalid (M['m00'] == 0)")

        # Turn the LED off if no object is detected
        elif led_on:
            print("No contours detected.")
            red_led.off()
            led_on = False

        # Show the frame
        cv2.imshow("Frame", frame)

        # Break the loop if [ESC] key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC key
            break

finally:
    # Cleanup
    print("\n[INFO] Exiting program and cleaning up...")
    red_led.off()
    cv2.destroyAllWindows()
    picam2.stop()
