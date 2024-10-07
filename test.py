import time
import board
import busio
import adafruit_mlx90640
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# if using higher refresh rates yields a 'too many retries' exception,
# try decreasing this value to work with certain pi/camera combinations
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ

frame = [0] * 768
while True:
    try:
        mlx.getFrame(frame, 0.95, 8)
    except ValueError:
        print("ERROR retrieving the frame ...")
        continue
    print(np.reshape(frame, (24,32)))
    break
    # print(np.max(frame), np.min(frame))
