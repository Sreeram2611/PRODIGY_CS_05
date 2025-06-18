# Task - 5
```bash
# 📡 SREERAM'S PACKET SNIFFER TOOL

A simple TCP packet sniffer written in Python using the Scapy library. This tool captures and logs TCP packets on your network and saves relevant details such as IPs, ports, protocols, and payload data into a text file.

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical use only**. You are **only allowed to use it** on networks:
- That you own, or
- For which you have **explicit permission**.

Misuse of this tool for intercepting or disrupting unauthorized networks is illegal and unethical.

---

## 📁 Features

- Captures TCP packets on your local network
- Displays and logs:
  - Source IP
  - Destination IP
  - Source and Destination Ports
  - Protocol number
  - First 50 characters of the TCP payload
- Saves all logs to `packet_sniffer_results.txt`

---

## 🛠️ Requirements

- Python 3.8 or later
- [Scapy](https://scapy.net/)
- [Npcap](https://npcap.com/) (for Windows only, required for raw packet capture)

### ✅ Install dependencies:

```bash
pip install scapy
````

> On **Windows**, you must install **Npcap**:
>
> * Download: [https://npcap.com/](https://npcap.com/)
> * During installation, ensure:
>
>   * "Install Npcap in WinPcap API-compatible Mode" is **checked**
>   * Install as Admin

---

## ▶️ How to Run

```bash
python packet.py
```

The tool will capture 10 TCP packets and save the results to a file.

---

## 📄 Output

All packet logs will be saved to:

```
packet_sniffer_results.txt
```

Sample log entry:

```
Source IP       : 192.168.0.10
Destination IP  : 142.250.64.78
Source Port     : 54321
Destination Port: 443
Protocol        : 6
Payload         : b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'...
------------------------------------------------------------
```


## 📌 License

This project is licensed for **educational use only**. Redistribution or modification must include proper attribution and adhere to ethical guidelines.
