# download_speed_one_line.py
# January 14, 2026
# prof. lehman
# calculates download speed in MB give
# file size in GB and time in minutes and seconds

print(f"download speed = {(float(input('Enter your file size (MB): '))*1024)/(int(input('Enter minutes: '))*60+int(input('Enter seconds: '))):.2f} MB per second")

