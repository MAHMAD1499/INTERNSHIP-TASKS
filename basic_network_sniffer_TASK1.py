from scapy.all import sniff, IP, TCP, UDP, ICMP
import sys

class NetworkSniffer:
    def __init__(self, interface=None):
        self.interface = interface

    def packet_handler(self, packet):
        if packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)
            protocol = "PROTOCOL"
            
            if packet.haslayer(TCP):
                protocol = "TCP"
            elif packet.haslayer(UDP):
                protocol = "UDP"
            elif packet.haslayer(ICMP):
                protocol = "ICMP"
            else:
                protocol = f"IP (Proto: {ip_layer.proto})"

            print(f"[{protocol}] {ip_layer.src} -> {ip_layer.dst}")

            if packet.haslayer(TCP) or packet.haslayer(UDP):
                payload = bytes(packet.payload)
                if payload:
                    print(f"   | Payload: {payload[:40].hex()}...")

    def start(self):
        """Starts the sniffing process."""
        print(f"[*] Starting sniffer on {self.interface if self.interface else 'default interface'}...")
        print("[*] Press Ctrl+C to stop.")
        try:
            sniff(iface=self.interface, prn=self.packet_handler, store=False)
        except PermissionError:
            print("[!] Error: Root/Admin permissions required.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n[*] Sniffer stopped by user.")
            sys.exit(0)

if __name__ == "__main__":
    sniffer = NetworkSniffer()
    sniffer.start()