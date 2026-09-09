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
|---|---|---|---|
| Relay VCC | Physical Pin 2 | Top row, 2nd pin from left | 5V Power for relay coil |
| Relay GND | Physical Pin 6 | Top row, 3rd pin from left | Circuit Ground |
| Relay IN | Physical Pin 16 (GPIO 23) | Bottom row, 8th pin from left | Active-LOW control signal |
| Relay COM | Physical Pin 1 | Top row, 1st pin on left | 3.3V Power source for LED |
| Relay NO | Breadboard Row 10 | Breadboard | Switched power line |
| Relay NC | Empty | None | Leave unconnected |
| Button Leg 1 | Physical Pin 12 (GPIO 18) | Bottom row, 6th pin from left | Input signal with internal pull-up |
| Button Leg 2 | Physical Pin 20 (GND) | Bottom row, 10th pin from left | Ground contact when pressed |
| LED Cathode | Physical Pin 14 (GND) | Bottom row, 7th pin from left | Ground return line |

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
