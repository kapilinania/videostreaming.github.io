# Video Streaming Project

This project demonstrates how to stream video content from FFmpeg to an HTML page using HTTP Live Streaming (HLS). Users can access the video stream through a web browser and control playback using the provided controls.

## Prerequisites

- [FFmpeg](https://ffmpeg.org/download.html) installed on your system.
- Basic knowledge of HTML, JavaScript, and optionally a server-side technology like Python or Node.js.

## Setup Instructions

1. **Install FFmpeg:**
   - Download and install FFmpeg from the [official website](https://ffmpeg.org/download.html) based on your operating system.

2. **Prepare Video Files:**
   - Convert your video file to the HLS format using FFmpeg.
   - Example command:
     ```
     ffmpeg -i 1.mp4 -c:v libx264 -crf 23 -preset veryfast -c:a aac -b:a 128k -ac 2 -hls_time 4 -hls_playlist_type vod -hls_segment_filename 'video/segment_%03d.ts' video/index.m3u8
     ```

3. **Set Up a Simple HTTP Server:**
   - Choose a server-side technology (e.g., Python, Node.js).
   - Create a server script to serve the video content.
   - Example Python script (`server.py`) using `http.server` module:
     ```python
     -----above c```python
     -----above code ----
     ```ode ----
     ```

4. **Create HTML Page for Video Streaming:**
   - Create an HTML file with a video element to display the streamed content.
   - Example HTML code:
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Video Streaming</title>
         <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
     </head>
     <body>
        ---- above code uploaded ------
     </body>
     </html>
     ```

5. **Viewing the Video Stream:**
   - Start the HTTP server.
   -  ``` python
    python3 server.py
     ```
   - Open a web browser and navigate to the HTML page.
   - The video stream should start playing with playback controls.

## License

This project is licensed under the [MIT License](LICENSE).
