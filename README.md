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

## 🔽 Download
You can download the most recent version of tool [here](https://codeload.github.com/oop7/YT-DLP-GUI-Downloader/zip/refs/heads/main)

## 🛠️ Installation

### 1. Install Dependencies
Ensure you have Python 3.x installed. Install required Python packages using `pip`.
```
pip install -r requirements.txt

```
Note: If you don't have `yt-dlp` and `ffmpeg`, download `yt-dlp.exe` and `ffmpeg.exe` and place them in the same directory as the script.

2. Run the Application

```
python youtube_downloader.py
```

## 💻 Usage

1. Open the application.
2. Enter the YouTube video URL.
3. Select the save path for downloaded files.
4. Choose the video quality and type (video or audio).
5. Click "Download" to start downloading.

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

