Facebook Video Downloader

This Python application allows users to download videos from Facebook by simply entering the video URL. It features a Tkinter-based GUI, providing a user-friendly interface with a progress bar that tracks the download progress.

Features
URL Validation: Verifies that the provided URL belongs to Facebook, ensuring valid input before attempting to download.
Progress Tracking: Uses a progress bar to show real-time download status.
Error Handling: Displays appropriate error messages if an invalid URL is entered or if connection issues arise.
Multithreaded Downloading: Downloads the video in a separate thread, allowing the GUI to remain responsive.

Libraries Used
time: For handling delays and pacing in the download process.
tkinter: For creating the GUI components.
requests: For making HTTP requests to fetch video content.
re: For regex operations to find the video link in the HTML response.
urllib.parse: For URL decoding.
threading: For handling downloads in a separate thread, preventing the GUI from freezing.
queue: For real-time communication between the download thread and the progress bar.

Requirements
Python 3.x

Required Python Libraries:
requests
tkinter (comes pre-installed with Python)
threading
