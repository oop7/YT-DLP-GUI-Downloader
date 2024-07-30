import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import os
import threading

def download_video():
    url = url_entry.get()
    save_path = path_var.get()
    quality = quality_var.get()
    download_type = type_var.get()

    if not url or not save_path:
        messagebox.showerror("Error", "URL or Save Path cannot be empty!")
        return

    yt_dlp_path = os.path.join(os.getcwd(), 'yt-dlp.exe')
    ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')

    ydl_opts = ['-o', os.path.join(save_path, '%(title)s.%(ext)s')]

    if download_type == 'video' and quality != 'best':
        if quality == '2160':
            ydl_opts.extend(['-f', 'bestvideo[height>=2160]+bestaudio/best[height>=2160]'])
        else:
            ydl_opts.extend(['-f', f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'])
    elif download_type == 'audio':
        ydl_opts.extend(['--extract-audio', '--audio-format', 'mp3'])

    # Merge video and audio using ffmpeg
    ydl_opts.extend(['--ffmpeg-location', ffmpeg_path])
    ydl_opts.extend(['--merge-output-format', 'mp4'])
    ydl_opts.extend(['--progress'])

    command = [yt_dlp_path] + ydl_opts + [url]

    def run_command():
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        for line in process.stdout:
            if '[download]' in line:
                # Parse progress and speed from the line
                if '%' in line:
                    try:
                        percent = float(line.split('%')[0].split()[-1])
                        progress_bar['value'] = percent
                    except ValueError:
                        pass
                if 'ETA' in line or 'speed' in line:
                    status_label.config(text=line.strip())

        process.wait()
        if process.returncode == 0:
            messagebox.showinfo("Success", "Download and merge completed successfully!")
        else:
            stderr_output = process.stdout.read()
            messagebox.showerror("Error", f"An error occurred: {stderr_output}")

        progress_bar.stop()

    threading.Thread(target=run_command).start()
    progress_bar.start()

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)

# Set up the main application window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# URL Entry
ttk.Label(main_frame, text="Video URL:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
url_entry = ttk.Entry(main_frame, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Save Path
ttk.Label(main_frame, text="Save Path:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
path_var = tk.StringVar()
path_entry = ttk.Entry(main_frame, textvariable=path_var, width=50)
path_entry.grid(row=1, column=1, padx=5, pady=5)
ttk.Button(main_frame, text="Browse", command=browse_folder).grid(row=1, column=2, padx=5, pady=5)

# Quality Selection
ttk.Label(main_frame, text="Quality:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
quality_var = tk.StringVar(value='best')
quality_options = ['144', '240', '360', '480', '720', '1080', '1440', '2160']
quality_menu = ttk.Combobox(main_frame, textvariable=quality_var, values=quality_options)
quality_menu.grid(row=2, column=1, padx=5, pady=5)

# Type Selection
ttk.Label(main_frame, text="Type:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
type_var = tk.StringVar(value='video')
video_radio = ttk.Radiobutton(main_frame, text='Video', variable=type_var, value='video')
audio_radio = ttk.Radiobutton(main_frame, text='Audio', variable=type_var, value='audio')
video_radio.grid(row=3, column=1, padx=5, pady=5, sticky='w')
audio_radio.grid(row=3, column=1, padx=5, pady=5, sticky='e')

# Progress Bar
progress_bar = ttk.Progressbar(main_frame, mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky='ew')

# Status Label
status_label = ttk.Label(main_frame, text="Status: Idle")
status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# Download Button
ttk.Button(main_frame, text="Download", command=download_video).grid(row=6, column=1, pady=10)

# Start the GUI event loop
root.mainloop()
