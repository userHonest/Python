"""
---------------------------------------------
Program: PhoneNumbers Information Gathering
Date: Update 23/03/23
Author: u$3r_h0n3$t
Version 1.1
---------------------------------------------
"""
# Modules ========================== #
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from opencage.geocoder import OpenCageGeocode
import argparse
import pyfiglet
import logging
import colorama
from colorama import Fore, Style

# ======================================= #
API_KEY = "ADD YOUR OPENCAGE API HERE"
LANGUAGE_CODE = "en"
BANNER = pyfiglet.figlet_format("Creep", font="roman")


## ========= GET LOCATION ========= ##
def get_location(number):
    try:
        number = phonenumbers.parse(number, LANGUAGE_CODE)
        return geocoder.description_for_number(number, LANGUAGE_CODE)
    except phonenumbers.NumberParseException:
        logging.error(f"Invalid phone number: {number}")
        return None


## ====== GET CARRIER ========= ##
def get_carrier(number):
    try:
        number = phonenumbers.parse(number, LANGUAGE_CODE)
        return carrier.name_for_number(number, LANGUAGE_CODE)
    except phonenumbers.NumberParseException:
        logging.error(f"Invalid phone-number: {number}")
        return None


## ======= Getting timezones === ##
def get_time_zones(number):
    try:
        number = phonenumbers.parse(number, LANGUAGE_CODE)
        return carrier.name_for_number(number, LANGUAGE_CODE)
    except phonenumbers.NumberParseException:
        logging.error(f"Invalid phone-number: {number}")
        return None


## ============= number is is valid ? = #
def is_valid_number(number):
    try:
        number = phonenumbers.parse(number, LANGUAGE_CODE)
        return phonenumbers.is_valid_number(number)
    except phonenumbers.NumberParseException:
        logging.error(f"Invalid phone number: {number}")
        return False


## =============== numbers exist?  #
def is_possible_number(number):
    try:
        number = phonenumbers.parse(number, LANGUAGE_CODE)
        return phonenumbers.is_possible_number(number)
    except phonenumbers.NumberParseException:
        logging.error(f"Invalid phone number: {number}")
        return False


## ========== Geolocation #
def get_geolocation(location):
    geocoder01 = OpenCageGeocode(API_KEY)
    try:
        results = geocoder01.geocode(location)
        return results
    except Exception as e:
        logging.error(f"Failed to geocode location: {location}. Error: {e}")
        return None


## ======= printing results with the geolocation functionality ============= #
def print_results(results, all_results=False):
    if all_results:
        for i, result in enumerate(results):
            print(f"\nResult {i + 1}:")
            print(f"- Formatted address: {result['formatted']}")
            try:
                print(f"- City: {result['components']['city']}")
            except KeyError:
                print("- City: Not available")
            print(f"- Country: {result['components']['country']}")
            print(f"- Latitude: {result['geometry']['lat']}")
            print(f"- Longitude: {result['geometry']['lng']}")
            print(f"- OSM URL: {result['annotations']['OSM']['url']}")
    else:
        if results:
            print(f"- Formatted address: {results[0]['formatted']}")
            try:
                print(f"- City: {results[0]['components']['city']}")
            except KeyError:
                print("- City: Not available")
            print(f"- Country: {results[0]['components']['country']}")
            print(f"- Latitude: {results[0]['geometry']['lat']}")
            print(f"- Longitude: {results[0]['geometry']['lng']}")
            print(f"- OSM URL: {results[0]['annotations']['OSM']['url']}")
        else:
            print("No results found.")


# ============== Function that runs all the previous code ======== #
def run_scan(number, all_results=False):
    print("=" * 56)
    print(BANNER)
    print(Fore.YELLOW + "Creep V 1.1" + Style.RESET_ALL)
    print("=" * 56, "\n")

    print("Country location:")
    location = get_location(number)
    if location:
        print(location)
    else:
        print("Location is not available")

    print("\nCountry carrier:")
    carrier_name = get_carrier(number)
    if carrier_name:
        print(carrier_name)
    else:
        print("Carrier not found")

    print("\nTime zones:")
    time_zones = get_time_zones(number)
    if time_zones:
        print(time_zones)
    else:
        print("Time zones are not available")

    print("\nNumber is valid:")
    print(is_valid_number(number))

    print("\nNumber exist:")
    print(is_possible_number(number))

    print("\nGeolocation:")
    results = get_geolocation(location)
    print_results(results, all_results)


## ============= Running_MAIN_with _arguments =============== #

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a Phone-Number and retrieve its information")
    parser.add_argument("number", type=str, help="The Phone-Number to scan")
    parser.add_argument("-all", "--all-results", action="store_true", help="Print all Geo-Location results")

    args = parser.parse_args()
    run_scan(args.number, args.all_results)

## ============== END OF PROGRAM ================ #
