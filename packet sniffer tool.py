from scapy.all import sniff, IP, TCP
import os

print("--------------- SREERAM'S PACKET SNIFFER TOOL ---------------")
print("This tool captures network packets for educational purposes only.\n")
print("Use this tool only on your own network or with explicit permission.\n")

# Output file path
output_file = "packet_sniffer_results.txt"

# Clear existing content
open(output_file, 'w').close()

# Analyze and log packet info
def packet_sniff(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        protocol = packet[IP].proto
        payload = str(packet[TCP].payload)

        log = (
            f"Source IP       : {src_ip}\n"
            f"Destination IP  : {dst_ip}\n"
            f"Source Port     : {src_port}\n"
            f"Destination Port: {dst_port}\n"
            f"Protocol        : {protocol}\n"
            f"Payload         : {payload[:50]}...\n"
            f"{'-'*60}\n"
        )

        print(log, end='')

        with open(output_file, 'a') as file:
            file.write(log)

# Start sniffing
print("Packet sniffing started...\n")
sniff(filter="tcp", prn=packet_sniff, store=False, count=10)

# Completion message
print("\nPacket capture complete.")
print(f"Results saved to: {os.path.abspath(output_file)}")
