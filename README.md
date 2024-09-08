# YouTube Video Downloader with GUI

A user-friendly application for downloading YouTube videos and audio. This tool uses `yt-dlp` for powerful downloading capabilities and integrates a graphical user interface (GUI) for ease of use. Features include customizable video quality, progress tracking, and automatic merging of video and audio files.

## 💪 Features

- Download videos and audio from YouTube.
- Choose video quality (e.g., 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p).
- Automatic merging of video and audio files.
- Progress bar and download speed display.
- Simple and intuitive GUI.

## ✅  Requirements

- Python 3.x
- `yt-dlp` (YouTube-DL fork)
- `ffmpeg` (for merging video and audio)

## 💻 Installation & Usage

### **Pre-built Executable (Recommended)**

1. Download the latest executable from the [Releases Section](https://github.com/oop7/YT-DLP-GUI-Downloader/releases).
1. Open the application.
2. Enter the YouTube video URL.
3. Select the save path for downloaded files.
4. Choose the video quality and type (video or audio).
5. Click "Download" to start downloading.

## Running from Source (Optional)

1. **Clone the repository**: ```git clone https://github.com/oop7/YT-DLP-GUI-Downloader.git```
3. **Install required dependencies**:```pip install -r requirements.txt```
4. **Run the tool**:```python yt_downloader.py```

## Building the Executable (Optional)

### To build the tool into an executable using PyInstaller:

1. **Install PyInstaller**:```pip install pyinstaller```
2. **Build the executable**:```pyinstaller --onefile yt_downloader.py```

This will generate an `.exe` file in the `dist/` directory.

## ⚙️ Troubleshooting

- Download Speed or Progress Not Updating: Ensure yt-dlp and ffmpeg are correctly installed and accessible from the script's directory.
- Errors During Download: Check the console output for detailed error messages.

## 📙 Contributing
Feel free to contribute by submitting issues or pull requests. If you have suggestions for improvements or new features, please open an issue or create a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ❓ Acknowledgments

- `yt-dlp` for providing robust video downloading capabilities.
- `ffmpeg` for handling video and audio merging.
- The open-source community for continuous support and development.

