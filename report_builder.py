
# PLP Python Week 7 Assignment
# Program 2: Read CSV data and build a report

import csv

try:
    with open("hubs.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        hubs = list(reader)

    print("COMMUNITY HUB REPORT")
    print("--------------------")

    for hub in hubs:
        print(f"Hub Name: {hub['hub_name']}")
        print(f"Location: {hub['location']}")
        print(f"Number of Learners: {hub['learners']}")
        print("--------------------")

    print(f"Total hubs: {len(hubs)}")

except FileNotFoundError:
    print("Error: hubs.csv was not found. Please check that the file exists.")

