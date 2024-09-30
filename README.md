## Setup:

1. Connecting the thermal sensor (MLX90460) to the PI(5):
    - Check the following links:
    - [Setting up](https://www.raspberrypi.com/documentation/computers/getting-started.html) the Raspberry PI.
    - [Pinout](https://www.hackatronic.com/raspberry-pi-5-pinout-specifications-pricing-a-complete-guide/) of Raspberry Pi 5
    - [Specification](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-mlx90640-ir-thermal-camera.pdf) of the Adafruit MLX90460 thermal array senor

2. Set up environment and download dependencies:
    
    - Update and upgrade available packages:
        ```
        $ sudo apt-get update
        $ sudo apt-get upgrade
        ```

    - Install the python-smbus package, necessary for accessing the I2C bus via Python.
        ```
        $ sudo apt-get install -y python3-smbus
        ```
    
    - Install i2c-tools, useful for probing and debugging I2C communications:
        ```
        sudo apt-get install -y i2c-tools
        ```
        You can run the following command to verify that your sensor is properly connected:
        ```
        $ sudo i2cdetect -y 1
             0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
        00:                          -- -- -- -- -- -- -- --    
        10:  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        20:  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        30:  -- -- -- 33 -- -- -- -- -- -- -- -- -- -- -- --
        40:  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        50:  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        60:  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        70:  -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
        ```
    
    - Open the Raspberry Pi’s boot configuration file in nano text editor using the following command:
        ```
        sudo nano /boot/config.txt
        ```
        Add `dtparam=i2c_arm=on, i2c_arm_baudrate=400000` to enable the I2C interface and set the baud rate for faster data transfer. Save it and go back to terminal.
    
    - Create a python virtual environment:
        ```
        $ mkdir project-name && cd project-name
        $ python3 -m venv .venv
        $ source .venv/bin/activate
        ```
        And install the relevant packages below:
        ```
        $ pip3 install adafruit-circuitpython-mlx90640
        $ pip3 install RPI.GPIO adafruit-blinka
        $ pip3 install numpy
        $ pip3 install opencv-contrib-python
        ```
## Files:
- test.py: simple script that connect to the thermal sensor and collects the raw data.
- visualize.py: processes the raw data obtained from the sensor and creates a thermal image.

## Useful Links:
- https://docs.circuitpython.org/projects/mlx90640/en/latest/api.html
- https://github.com/adafruit/Adafruit_CircuitPython_MLX90640
- https://how2electronics.com/thermal-fever-detector-with-mlx90640-opencv-raspberry-pi/
- https://cdn-learn.adafruit.com/downloads/pdf/adafruit-mlx90640-ir-thermal-camera.pdf
- 
