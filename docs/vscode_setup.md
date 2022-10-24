# VS Code Setup

The following tutorial was made for Windows users with. The process might be different for any other operating system.

## Initial Installation

For the initial installation you can follow two ways:
- Option A: You have access to the sakai site of the MCI Course 'Hardwarenahe Softwareentwicklung' or 'Programmierübungen 3'. If so, download the 'installationsfiles.zip' file from the resources folder there. All relevant files are part of the .zip file.
- Option B: Download the "installationsfiles.zip" file from the [drive](https://drive.google.com/drive/folders/1Us2nApnVqCk2eESj3GP7jM6fATm70s_C?usp=sharing)

After you went for option A or B you have downloaded the 'installationsfiles.zip'. Unzip the archive as it contains the following files and folders:
  ```
  installationsfiles/
  |-- CP210x_Universal_Windows_Driver/
  |-- node-v16.18.0-x64.msi
  |-- python-3.10.8-amd64.exe
  |-- VSCodeUserSetup-x64-1.72.2.exe
  ```


### Node JS

- Install Node JS by executing the file 'node-v16.18.0-x64.msi'
- No extra check boxes need to be checked in the installation process of Node JS

### Python

- Install Python 3.10.8 by executing the file 'python-3.10.8-amd64.exe'
- At the beginning of the installation process check the checkbox that Python is added the the PATH (this enables an easier use for python within out VS Code Setup)
- At the end of the installation process you have the option to disable the path length limit of Windows. Make sure to disable the path length limit.

### Visual Studio Code

- Install VS Code by executing 'VSCodeUserSetup-x64-1.72.2.exe'
- Optional: If you want to have a dektop icon for VS Code make sure to check the checkbox during the installation process

### Install the driver for ESP32 Board

- Plug in the ESP32 board with the USB Cable. Depending on your system the drivers are installed automatically. Make sure to check, whether the driver installation worked by following the following steps:
	-  press the 'Windows key' + 'X'
	-  click on the item 'Device Manager' (in german 'Gerätemanager')

- If the CP2102 Device is listed under 'Ports' (in german 'Anschlüsse'), showing a corresponding COM port (e.g. COM3, COM6, etc.), the driver installation was done automatically. If this is not the case, you have to manually instal the driver. To do so follow the following steps:
	-  Have a look at the devices that are listed under 'Other devices' (in german 'Andere Geräte')
	-  There might be a device called 'CP2102 USB to UART Bridge Controller' or 'Serial Device' or simial
	-  Right click the device and click on properties (in german 'Eigenschaften'). The pop up window shows a button to named 'Update Driver...'
	-  Left click the button and follow the instructions till you can choose to browse the computer for driver software.
	-  After left clicking the option, brows to the folder 'CP210x_Universal_Windows_Driver' within your extracted installation files and start the driver installation

Congratulations, you have finished the first step of the VS Code Setup. Now we can start the second step.


## VS Code Configuration

After starting VS Code for the first time you have to install several extension so VS Code is capable to develop project with Micropython and ESP32 boards. Follow the setps below to enable this:
- Either navigate to the 'extension' view by left clicking the button on the leftmost coloumn, which lists the 'explorer', 'search', 'source control', 'run and debug' and 'extension' view. Much quicker, you can use the given Shortcuts by pressing 'Ctrl'+'Shift'+'X'
- Within the 'extension' view, you have to install the extensions in the order 'python', 'pylance' and 'pymakr'
- After the successful installation you should have additional views in the leftmost coloumn (one of them is named 'PyMakr')

Congratulations, you have finished the second step of the VS Code Setup. Now we can start our first test project:

## Project Deploymnet
- Creat a workspace directory on your computer which you want to use for all your Micropython projects. You can name the directory as you would like. For easierer expainations we use a directory 'C:/mpy_projects'
- Now add the folder to your workspace...
	- ...by leftclicking the File Button in the topmost bar and the leftclicking the 'Add folder to workspace...' button...
	- ...and the navigate to the respective folder (in this tutorial it is 'C:/mpy_projects')
- Now, check whether the workspace was added correctly either by navigating to the 'explorer' view by left clicking the button on the leftmost coloumn, or you can use the given Shortcuts by pressing 'Ctrl'+'Shift'+'E'
- If the ESP board is not already plugged in, plug it in now
- As a next step choose the PyMakr View and create or add a pymakr project (use the empty project configuration with the Silicon Labs CP210x USB to UART Bridge as selected device)
- Navigate to the 'explorer' view to see, that there are now three files within your project folder:
  ```
  mpy_projects/
  |-- boot.py
  |-- main.py
  |-- pymakr.conf
  ```
  
- Open the main.py file by left clicking it and change the content to:

  ```
  import time

  while 1:
    print('Congratulation, the setup works')
    time.sleep(1)
  ```

- Navigate back to the 'PyMakr' view and click the sync to device button within the empty project
- Open the PyMakr terminal by left clicking the create terminal button within the empty project
- Press the EN button and see whether the terminal shows you the message 'Congratulation, the setup works' every second

Congratulations, you have finished the third step of the VS Code Setup. Now we can start developing.
