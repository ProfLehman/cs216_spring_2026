# download_speed.py
# January 14, 2026
# prof. lehman
# calculates download speed in MB give
# file size in GB and time in minutes and seconds
# input
file_size_mb=float(input("Enter your file size (MB): "))
minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))
# processing
total_mb=file_size_mb*1024
total_seconds=minutes*60+seconds
download_speed=total_mb/total_seconds
# output
print(f"download speed={download_speed:.2f} MB per second")