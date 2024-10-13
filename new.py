import cv2
import numpy as np
import board
import busio
import adafruit_mlx90640
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
# Setup MLX90640
i2c = busio.I2C(board.SCL, board.SDA)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ  # Adjust as needed
w, h = 32, 24
data_array = np.zeros((24*32,))

def nothing(x):
    pass

cv2.namedWindow('Thermal Image')
cv2.createTrackbar('Emissivity', 'Thermal Image', 95, 100, nothing)
cv2.createTrackbar('Ta shift', 'Thermal Image', 8, 38, nothing)
cv2.createTrackbar('Min Thresh', 'Thermal Image', 20, 50, nothing)
cv2.createTrackbar('Max Thresh', 'Thermal Image', 35, 50, nothing)
 
def get_thermal_image(emissivity, ta_shift):
    frame = np.zeros((24*32,))
    mlx.getFrame(frame, emissivity, ta_shift)
    data_array = np.reshape(frame, (24, 32))
    return data_array

def apply_thresholds(data_array, min_thresh, max_thresh):
    data_array[data_array > max_thresh] = max_thresh    
    data_array[data_array < min_thresh] = min_thresh
    
    return data_array

def process_image(data_array, min_thresh, max_thresh):
    data_array = apply_thresholds(data_array, min_thresh, max_thresh)

    # min_val, max_val = np.min(data_array), np.max(data_array)
    # image = (data_array - min_val) / (max_val - min_val) * 255
    # image = cv2.normalize(data_array, None, 0, 255, cv2.NORM_MINMAX)
    image = cv2.normalize(data_array, None, 0, 255, cv2.NORM_MINMAX)
    image = np.uint8(image)

    # image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    # image = cv2.applyColorMap(image, cv2.COLORMAP_BONE)
    # image = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
    # image = cv2.applyColorMap(image, cv2.COLORMAP_TWILIGHT)
    
    image = cv2.resize(image, (w*20, h*20), interpolation=cv2.INTER_CUBIC)
    return image

def save_image(image, filename):
    cv2.imwrite(filename, image)

def plot_histogram(data_array, ax):
    """ Plot a histogram for the temperature data using matplotlib (non-blocking). """
    # Flatten the 2D array to 1D for the histogram
    flat_data = data_array.flatten()
    
    # Clear the previous plot to update it without blocking
    ax.clear()
    
    # Plot the histogram
    ax.hist(flat_data, bins=20, color='blue', edgecolor='black')
    
    # Add titles and labels
    ax.set_title('Temperature Distribution Histogram')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    
    # Set limits if necessary to ensure consistency across updates
    ax.set_xlim([0, 50])  # Adjust according to the expected range of temperatures
    ax.set_ylim([0, 760])  # Adjust this as needed to fit the data

    # Pause to allow the plot to update
    plt.pause(0.01)

def main():
    frame_count = 0
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Turn on interactive mode in Matplotlib
    plt.ion()

    while True:
        emissivity = cv2.getTrackbarPos('Emissivity', 'Thermal Image')/100
        ta_shift = cv2.getTrackbarPos('Ta shift', 'Thermal Image')
        min_thresh = cv2.getTrackbarPos('Min Thresh', 'Thermal Image')
        max_thresh = cv2.getTrackbarPos('Max Thresh', 'Thermal Image')

        data_array = get_thermal_image(emissivity, ta_shift)
        image = process_image(data_array, min_thresh, max_thresh)

        cv2.rectangle(image, (0, 520), (640, 560), (50, 50, 50), -1)
        cv2.imshow('Thermal Image', image)

        if frame_count % 10 == 0:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"images/thermal_image_{timestamp}.png"
            plot_histogram(data_array, ax)
            # save_image(image, filename)
            # print(f"Saved: {filename}")

        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    plt.ioff()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    main()