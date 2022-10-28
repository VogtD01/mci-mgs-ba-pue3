# VS Code Setup guide

The following tutorial was made for Windows users with. The process might be different for any other operating system.

## Download the Ressources

- Download the 'HWSE.zip'from the SAKAI Ressources folder or from the [drive](https://drive.google.com/drive/folders/1Us2nApnVqCk2eESj3GP7jM6fATm70s_C?usp=sharing). 

- Unzip the archive and confirm that your 'HWSE' directory conains the following folders with the size of about 500MB:

 
```
HWSE/
  |-- vscode/
  |-- installationfiles
  |-- my_projects
```

- Enter the folder "installationfiles".

## NodeJS

- In the "installationfiles" folder, install Node JS by executing the file 'node-v16.18.0-x64.msi'

- :warning: No extra check boxes need to be checked in the installation process of Node JS

## Python

- Install Python 3.10.8 by executing the file 'python-3.10.8-amd64.exe'
- :warning: At the beginning of the installation process check the checkbox that Python is added the the PATH (this enables an easier use for python within out VS Code Setup)

- :warning: At the end of the installation process you have the option to disable the path length limit of Windows. Make sure to disable the path length limit.

## ESP32 Driver

- Plug in the ESP32 board with the USB Cable. Depending on your system the drivers are installed automatically. Make sure to check, whether the driver installation worked by following the following steps:

    - press the 'Windows key' + 'X'
    - click on the item 'Device Manager' (in german 'Gerätemanager')
    
- If the CP2102 Device is listed under 'Ports' (in german 'Anschlüsse'), showing a corresponding COM port (e.g. COM3, COM6, etc.), the driver installation was done automatically. If this is not the case, you have to manually instal the driver. To do so follow the following steps:

    - Have a look at the devices that are listed under 'Other devices' (in german 'Andere Geräte')

    - There might be a device called 'CP2102 USB to UART Bridge Controller' or 'Serial Device' or similar.

    - Right click the device and click on properties (in german 'Eigenschaften'). The pop up window shows a button to named 'Update Driver...'
    
    - Left click the button and follow the instructions till you can choose to browse the computer for driver software.

    - After left clicking the option, brows to the folder 'CP210x_Universal_Windows_Driver' within your extracted installation files and start the driver installation

## esptool and pylint

- Open the command line by pressing "Windows+R" to open the "Run" box. Type "CMD" and press okay.

- In the command prompt window enter the following:

```
pip3 install esptool pylint
```

- Wait until the download and installation finish and close the window.


Well done! You have finished the VS Code Setup.
Now we can create our first project.

# Create a new Project

- Open the folder "vscode" and run "Code.exe" to open the IDE.

- On the left sidebar, click on the "Pymakr" Icon. 

- Click on the "Create project" panel and navigate to "my_projects" folder in the "HWSE" directory.

- Create a new folder where your project will be located. Your folder structure should now look like this:

```
    mpy_projects/
    |-- micropython-stubs
    |-- myFirstProject/
        |-- boot.py
        |-- main.py
        |-- pymakr.conf
```

- In the "micropython-stubs" folder go to "docs/samples"

- Copy the folder ".vscode" and "plintrc" and paste it to your project folder.

Your folder structure should now look like this:

```
    mpy_projects/
    |-- micropython-stubs
    |-- myFirstProject/
        |--.vscode
        |-- pylintrc
        |-- boot.py
        |-- main.py
        |-- pymakr.conf
```

# Deploy your project

- Open the main.py file by left clicking it and change the content to:

```
import time
from machine import Pin

# Set GPIO2 to output
led_pin = Pin(2, Pin.OUT)

while 1:
  print('Congratulation, the setup works')
  
  led_pin.value(1)
  time.sleep(1)

  led_pin.value(0)
  time.sleep(1)
```

- Navigate back to the 'PyMakr' view and click the sync to device button within the empty project

- Open the PyMakr terminal by left clicking the create terminal button within the empty project

- Press the EN button on the ESP32 board and see if the terminal in the IDE shows you the message 'Congratulation, the setup works' and the blue LED on the ESP32 is blinking every second.

### Congratulations, you have finished the last step of the Setup. Now we can start developing :rocket:
