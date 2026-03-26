# IoT Fire Detection and Alarm System

## Overview
This project presents a smart IoT-based fire detection and alarm system developed using Cisco Packet Tracer and Python socket programming.  
It integrates edge sensors, a home gateway,and a cloud server to detect hazards and respond automatically in real-time.

----

## System Architecture

### Edge Layer
- Smoke sensors  
- CO₂ sensors  
- Flame/Fire sensors  
- Deployed in multiple rooms  

### Gateway Layer
- Home Gateway (DLC100)  
- Receives sensor data and applies control rules  

### Cloud Layer
- Python-based server  
- Receives, logs, and monitors system events  

---

## Technologies Used
- Python (Socket Programming)  
- Cisco Packet Tracer  
- IoT Architecture (Edge + Cloud)  
- CSV Data Logging  

---

## System Features
- Real-time smoke and fire detection  
- CO₂ level monitoring  
- Automatic sprinkler activation  
- Alarm (siren) triggering  
- Cloud-based monitoring and logging  

---

## Project Structure:
.
├── cloudServer.py
├── gatewayClient.py
├── assignmentV2Copy.pkt
├── events_1222177.csv
├── Report.pdf
├── Assignment.pdf


---

## How to Run
1. Run the cloud server:
  python cloudServer.py
2. Run the gateway client:
  python gatewayClient.py
3. Open the simulation:
  Open assignmentV2Copy.pkt using Cisco Packet Tracer

---

## Results
The system successfully:
- Detects smoke, fire, and CO₂ hazards
- Activates alarms and sprinklers automatically
- Sends real-time data to the cloud server

---

## Authors
- Sadeen Jihad Faqeeh  
- Lana Ayed Sayes  
- Julnar Naal Assi

---

## Documentation
Full details are available in:
Report.pdf
