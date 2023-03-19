!/usr/bin/python

import argparse
import ipinfo
import csv


def main(ip_address=None, file_path=None):
    ipInfo_token = 'add your ipinfo token here'
    handler = ipinfo.getHandler(ipInfo_token)
    ips = []

    if ip_address:
        ips = [ip_address]
    elif file_path:
        with open(file_path, "r") as file:
            if file_path.endswith(".csv"):
                reader = csv.reader(file)
                for row in reader:
                    ips.extend(row)
            else:
                ips = file.readlines()
                ips = [ip.strip() for ip in ips]
    else:
        print("Please provide an IP address or a file path.")
        return

    for ip in ips:
        details = handler.getDetails(ip)
        print(f"Details for IP address {ip}:")
        for key, value in details.all.items():
            print(f"  {key}: {value}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-ip", "--ip-address", help="IP address to retrieve details for")
    group.add_argument("-file", "--file-path", help="File path to a CSV or text file containing IP addresses")
    args = parser.parse_args()

    main(ip_address=args.ip_address, file_path=args.file_path)
