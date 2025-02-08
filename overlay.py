import gpxpy
import cv2

def add_telemetry_overlay(video_file, gpx_file):
    print(f"Processing {video_file} with {gpx_file}...")

add_telemetry_overlay("gopro_video.mp4", "track.gpx")
