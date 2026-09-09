## 🛠️ Raspberry Pi Node-RED GPIO Relay & Button Controller

------------------------------
## 📌 Core Features

* Bidirectional Control Loop: Activates a 5-second countdown timer via either the Node-RED Dashboard switch or a physical hardware button.
* Software Debouncing Layer: Implements a 300ms software lockout mechanism inside a function node to completely prevent false-triggering and contact bounce.
* Live Metrics Dashboard: Tracks and displays operational relay states, live remaining countdown seconds, and lifetime button press cycles.
* Native OS Execution: Controls hardware directly through standard Linux system commands via native CLI utilities rather than relying on outdated root libraries.

------------------------------
## 🎛️ Hardware Configuration & Wiring
Connect the components to the Raspberry Pi 40-pin GPIO header using the physical pin locations listed below.


| Device Component | Connection Target | Raspberry Pi Header Location | Function |
| :--- | :--- | :--- | :--- |
| **Main Ground Wire** | Breadboard Blue Rail (-) | Top row, 3rd pin from left (Pin 6) | Supplies Ground (0V) to the breadboard rail |
| **Main 5V Power Wire** | Breadboard Red Rail (+) | Top row, 1st pin from left (Pin 2) | Supplies 5V Power to the breadboard rail |
| **Relay VCC** | Breadboard Red Rail (+) | None (Powered via Red Rail) | 5V Power for relay coil |
| **Relay GND** | Breadboard Blue Rail (-) | None (GND via Blue Rail) | Circuit Ground |
| **Relay IN** | Physical Pin 16 (GPIO 23) | Top row, 8th pin from left | Active-LOW control signal |
| **Relay NO** | Jumper Wire to Leg 1 of Resistor | None (Direct connection) | Switched power line to LED load |
| **Relay COM** | Breadboard Red Rail (+) | None (Powered via Red Rail) | Safe 5V power source for the switched load |
| **Relay NC** | Empty | None | Leave unconnected |
| **LED Anode (+)** | Connects to Leg 2 of Resistor | None (Direct connection) | Positive leg of LED |
| **LED Cathode (-)** | Breadboard Blue Rail (-) | None (GND via Blue Rail) | Ground return line |
| **Button Leg 1** | Physical Pin 12 (GPIO 18) | Top row, 6th pin from left | Input signal with internal pull-up |
| **Button Leg 2** | Breadboard Blue Rail (-) | None (GND via Blue Rail) | Ground contact when pressed |

------------------------------
## 🚀 Dependencies
Ensure your Node-RED instance has the following project modules installed:

* @flowfuse/node-red-dashboard (v1.31.0 or higher)
* node-red-node-pi-gpio (v2.0.7 or higher)

------------------------------
## 💻 Installation and Deployment
## 1. Host System Environment Check

sudo run.py

## 2. Import the JSON Flow

   1. Open your Node-RED instance in a web browser.
   2. Open the menu in the top right corner and select Import.
   3. Import the raw JSON array string provided in your source configuration file.
   4. Click Import.

## 3. Deploy and Access

   1. Click the Deploy button in the top right corner of the Node-RED editor.
   2. Access the user control panel at the dedicated endpoint url:
   
   http://<YOUR_PI_IP_ADDRESS>:1880/dashboard/home
