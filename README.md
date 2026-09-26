# Android Application Penetration Testing

A cybersecurity internship project focused on setting up an Android application penetration testing environment and analyzing a deliberately vulnerable Android application using Genymotion, Kali Linux, ADB, Burp Suite, and InsecureBankv2.

---

## Project Overview

This project demonstrates the basic workflow used for Android application security testing in a controlled laboratory environment.

The lab consists of:

- **Genymotion** — Android virtual device
- **Kali Linux** — Security testing environment
- **InsecureBankv2** — Deliberately vulnerable Android application
- **ADB** — Android Debug Bridge for device communication
- **Burp Suite** — Interception and analysis of HTTP requests
- **Android Lab Server** — Backend server used by the application

The environment was configured to allow communication between the Android emulator and Kali Linux so that application traffic could be observed during testing.

---

## Project Objectives

The main objectives of this project were:

- Set up a controlled Android penetration testing environment.
- Configure a Genymotion Android virtual device.
- Connect the Android device with the Kali Linux environment.
- Use ADB to communicate with the Android device.
- Deploy the InsecureBankv2 application.
- Configure and run the Android Lab Server.
- Configure Burp Suite for HTTP traffic interception.
- Configure the Android emulator to use the Burp Suite proxy.
- Capture and inspect application requests.
- Understand the basic workflow of Android application penetration testing.

---

## Lab Architecture

```text
                  ┌─────────────────────────┐
                  │   Genymotion Emulator   │
                  │                         │
                  │    Android Device       │
                  │                         │
                  │     InsecureBankv2      │
                  └────────────┬────────────┘
                               │
                               │ HTTP Traffic
                               ▼
                  ┌─────────────────────────┐
                  │       Burp Suite        │
                  │     Proxy / Intercept   │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │      Kali Linux         │
                  │                         │
                  │  Android Lab Server     │
                  │       + ADB             │
                  └─────────────────────────┘
Tools and Technologies
Tool / Technology	Purpose
Genymotion	Android virtual device
Kali Linux	Security testing environment
InsecureBankv2	Deliberately vulnerable Android application
Android Debug Bridge (ADB)	Android device communication
Burp Suite	HTTP request interception and analysis
Python	Running the Android Lab Server
Flask	Backend server used by the lab
Lab Environment

The project was performed using a controlled virtualized laboratory environment.

Android Environment
Genymotion Android Virtual Device
Android 11 environment
InsecureBankv2 application
Security Testing Environment
Kali Linux
ADB
Burp Suite
Python
Android Lab Server
Project Setup
1. Genymotion Setup

A Genymotion Android virtual device was created and configured for the Android penetration testing laboratory.

The Android emulator was started before beginning the application testing process.

The Android device was configured so that it could communicate with the Kali Linux environment.

2. Kali Linux

Kali Linux was used as the security testing environment.

The Kali Linux machine was started alongside the Genymotion Android emulator.

Network connectivity between Kali Linux and the Android emulator was verified using the Android device IP address.

Example:

ping <ANDROID_DEVICE_IP>
3. Android Debug Bridge

Android Debug Bridge (ADB) was used to communicate with the Android emulator.

The Android device was connected from Kali Linux using its IP address.

Example:

adb connect <ANDROID_DEVICE_IP>

The connected device could then be accessed using ADB commands.

4. InsecureBankv2

InsecureBankv2 was used as the intentionally vulnerable Android application for the penetration testing laboratory.

The application was obtained as part of the Android security testing environment and installed on the Genymotion emulator using ADB.

Example:

adb install <INSECUREBANKV2_APK>

After installation, the InsecureBankv2 application was available on the Android emulator.

5. Android Lab Server

The Android Lab Server was used as the backend server for the InsecureBankv2 application.

The server application was opened and configured to listen on all network interfaces.

The Flask application was configured with:

host = "0.0.0.0"

The server was started using:

python app.py

The server IP address was then used for communication between the Android application and the backend server.

6. Burp Suite Configuration

Burp Suite was configured to intercept the HTTP traffic generated by the Android application.

The Burp Suite proxy listener was configured using the Kali Linux machine's IP address and port 8080.

Example:

Proxy Host: <KALI_IP>
Proxy Port: 8080

The Android emulator was then configured to use Kali Linux as its Wi-Fi proxy.

Example:

Proxy Server: <KALI_IP>
Proxy Port: 8080

This configuration allowed application traffic to pass through Burp Suite for inspection.

Testing Workflow

The overall testing workflow followed these stages:

Genymotion Setup
       │
       ▼
Start Android Emulator
       │
       ▼
Start Kali Linux
       │
       ▼
Verify Network Connectivity
       │
       ▼
Connect Android Device using ADB
       │
       ▼
Install InsecureBankv2
       │
       ▼
Start Android Lab Server
       │
       ▼
Configure Burp Suite
       │
       ▼
Configure Android Proxy
       │
       ▼
Launch InsecureBankv2
       │
       ▼
Configure Application Server
       │
       ▼
Generate Application Traffic
       │
       ▼
Capture Requests in Burp Suite
       │
       ▼
Analyze Application Traffic
Application Testing

After the environment was configured, the InsecureBankv2 application was launched on the Genymotion Android emulator.

The application was configured to communicate with the Android Lab Server.

Burp Suite was used as the interception proxy.

Application requests were generated while interacting with the application, allowing the requests to be captured and inspected through Burp Suite.

The testing process focused on understanding how the Android application communicated with its backend server and how HTTP requests could be observed during security testing.

Evidence and Screenshots

Screenshots were captured throughout the project to document the different stages of the practical implementation.

The evidence includes:

Genymotion Android emulator setup
Android virtual device
Kali Linux environment
Network connectivity between Kali Linux and Android
ADB connection
InsecureBankv2 installation
InsecureBankv2 application
Android Lab Server
Burp Suite configuration
Proxy configuration
Intercepted HTTP requests
Application testing

The screenshots are included in the project repository as supporting evidence.

Project Structure
Android-InsecureBankv2/
│
├── Android-Lab-Server/
│   │
│   └── app.py
│
├── InsecureBankv2/
│   │
│   └── Android application files
│
├── screenshots/
│   │
│   └── Project screenshots and evidence
│
├── report/
│   │
│   └── Project report
│
└── README.md

The exact filenames and directories may vary depending on the files included in the project repository.

Key Concepts Practiced

This project provided practical exposure to the following concepts:

Android application security testing
Android virtual machine setup
Genymotion
Kali Linux
Android Debug Bridge (ADB)
Android device connectivity
Network configuration
Vulnerable Android application deployment
Backend server configuration
Flask application execution
HTTP proxy configuration
Burp Suite
HTTP request interception
Application traffic analysis
Basic Android penetration testing workflow
Learning Outcomes

Through this project, the following practical skills were developed:

Setting up an Android security testing environment.
Creating and configuring an Android virtual device.
Connecting an Android emulator with Kali Linux.
Using ADB to communicate with an Android device.
Installing an Android application using ADB.
Running the Android Lab Server.
Configuring Burp Suite as an interception proxy.
Configuring an Android device to use a proxy.
Capturing application requests.
Observing and analyzing application traffic.
Understanding the basic workflow involved in Android application penetration testing.
Project Scope

This project focuses on the setup and basic testing workflow of an Android application penetration testing environment.

The project demonstrates:

Environment preparation
Android emulator configuration
Application deployment
Backend server setup
Proxy configuration
HTTP traffic interception
Basic request analysis

Testing was performed within a controlled laboratory environment using an intentionally vulnerable application.

Security and Ethical Considerations

This project was conducted for educational and cybersecurity training purposes.

The InsecureBankv2 application is intentionally vulnerable and is used in controlled security testing environments.

Security testing should only be performed against applications, systems, devices, and networks for which appropriate authorization has been obtained.

Do not use the techniques demonstrated in this project against systems without permission.

References
Genymotion
https://www.genymotion.com/
Kali Linux
https://www.kali.org/
Burp Suite
https://portswigger.net/burp
Android Developers
https://developer.android.com/
InsecureBankv2
https://github.com/dineshshetty/Android-InsecureBankv2
Author

Vanamala Srithan

Cybersecurity Student

Areas of Interest:

Cybersecurity
Android Application Security
Penetration Testing
Security Operations
Cloud Security

GitHub:

https://github.com/Vanamala-Srithan

Disclaimer

This repository is intended strictly for educational and cybersecurity training purposes.

The project uses a deliberately vulnerable Android application in a controlled laboratory environment.

The author does not support or encourage unauthorized access, exploitation, or testing of systems without explicit permission.
