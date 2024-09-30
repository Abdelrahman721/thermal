### 1. Increasing the refresh rate:

Adjusting the baudrate in /boot/config.txt:
- https://forums.raspberrypi.com/viewtopic.php?t=360996
- Tried re-running → runtime error

Adjusting the baudrate at runtime:
- `$ sudo dtparam i2c_arm_baudrate=1000000` → `DTOVERLAY[warn]: no matching platform found`
- research the warning → you can ignore
- re-run the code → runtime error

Need to confirm if the baudrate is being correctly set:
- Nothing online found about checking. Need oscilloscope.
- Tried *lower* bauderate and rebooted to check if 4HZ is still possible → Still possible
- Conclusion: baudrate is not being adjusted

Started to read about the /boot/config.txt file:
- https://askubuntu.com/questions/1462320/updating-raspberrypi-4b-from-ubuntu-server-20-04-to-22-04-caused-usercfg-txt-to
- The /boot/firmware/config.txt file being used instead
- Can go up to frames per second

[Observation] The more framerate the more noise there is:
- image of noise to framerate ratio from manual.

### 2. Increase details
- Online search
- Found https://www.sciencedirect.com/science/article/pii/S2542660521001268


### 3. Side-to-side with big camera

### 4. Inference on deepnet

### 5. Presentation slides (DONE)