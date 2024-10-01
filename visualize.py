import cv2
import numpy as np
import board
import busio
import adafruit_mlx90640
import time
 
# Setup MLX90640
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_32_HZ  # Adjust as needed
w, h = 32, 24
 
def get_thermal_image():
    frame = np.zeros((24*32,))
    mlx.getFrame(frame)
    data_array = np.reshape(frame, (24, 32))
    return data_array
 
def process_image(data_array):
    # Normalize data_array to 0-255 for image processing
    min_val, max_val = np.min(data_array), np.max(data_array)
    image = (data_array - min_val) / (max_val - min_val) * 255
    image = np.uint8(image)
    image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    # image = cv2.applyColorMap(image, cv2.COLORMAP_BONE)
    # image = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
    # image = cv2.applyColorMap(image, cv2.COLORMAP_TWILIGHT)
    image = cv2.resize(image, (w*20, h*20), interpolation=cv2.INTER_CUBIC)
    return image

def save_image(image, filename):
    cv2.imwrite(filename, image)

def main():
    frame_count = 0

    while True:
        data_array = get_thermal_image()
        image = process_image(data_array)
        cv2.rectangle(image, (0, 520), (640, 560), (50, 50, 50), -1)
        cv2.imshow('Thermal Image', image)

        if frame_count % 10 == 0:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"images/32HZ_thermal_image_{timestamp}.png"
            save_image(image, filename)
            print(f"Saved: {filename}")

        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    main()