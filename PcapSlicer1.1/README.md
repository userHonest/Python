# Packet Slicer

This project includes a script that reads a .pcap file and provides various information about the packets captured in the file.

This script requires Python 3.x and the following Python libraries installed:
- Scapy
- base64
- binascii


You can install these libraries using pip:
type on terminal : 

pip install -r requirements.txt

You can add additional arguments to perform different actions on the pcap file:

python slicer.py -h
usage: slicer.py [-h] -F PCAP_FILE [-udp--print_udp_data] [-ipData]
                 [-hexdump] [-dB64] [-source]

Count the type of packets in the file


  -h, --help            show this help message and exit
  
  
  -F PCAP_FILE, --pcap_file PCAP_FILE
                        Path to the PCAP file
  
  
  -udp--print_udp_data  Print out the data from the UDP protocol
  
  
  -ipData, --print_ip_data
                        Print out the data for the IP
  
  
  -hexdump, --hexdump_data
                        Display hexdump of packet data
  
  
  -dB64, --decode_base64
                        Decode base64 data from pcap file
  
  
  -source, --print_source_info
                        Print source IP and MAC addresses of IP and UDP
                        packets

Usage:
python slicer.py -F <your_pcap_file.pcap>
