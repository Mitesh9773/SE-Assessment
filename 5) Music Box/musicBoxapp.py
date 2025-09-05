import os
import tkinter as tk
from tkinter import messagebox

# Ensure playlists folder exists
if not os.path.exists("playlists"):
    os.makedirs("playlists")

# Playlist Class
class Playlist:
    def __init__(self, name, songs):
        self.name = name.strip()
        self.songs = [song.strip() for song in songs if song.strip()]

    def save(self):
        if not self.name:
            raise ValueError("Playlist name cannot be empty.")
        if not self.songs:
            raise ValueError("Playlist must contain at least one song.")

        filename = f"playlists/playlist_{self.name}.txt"
        if os.path.exists(filename):
            raise FileExistsError("Playlist already exists!")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.songs))

    @staticmethod
    def load(filename):
        with open(f"playlists/{filename}", "r", encoding="utf-8") as f:
            return f.read().splitlines()

# GUI Application
def save_playlist():
    try:
        name = name_entry.get()
        songs = song_text.get("1.0", tk.END).splitlines()
        pl = Playlist(name, songs)
        pl.save()
        messagebox.showinfo("Success", f"Playlist '{name}' saved!")
        name_entry.delete(0, tk.END)
        song_text.delete("1.0", tk.END)
        load_playlists()
    except (ValueError, FileExistsError) as e:
        messagebox.showerror("Error", str(e))

def load_playlists():
    playlist_listbox.delete(0, tk.END)
    for file in os.listdir("playlists"):
        if file.endswith(".txt"):
            playlist_listbox.insert(tk.END, file)

def show_playlist(event):
    selected = playlist_listbox.curselection()
    if not selected:
        return
    filename = playlist_listbox.get(selected[0])
    try:
        songs = Playlist.load(filename)
        display_text.config(state="normal")
        display_text.delete("1.0", tk.END)
        for s in songs:
            display_text.insert(tk.END, s + "\n")
        display_text.config(state="disabled")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")

# Tkinter Setup
root = tk.Tk()
root.title("MusicBox")
root.geometry("500x500")

tk.Label(root, text="Playlist Name:").pack(anchor="w", padx=10, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(anchor="w", padx=10)

tk.Label(root, text="Enter Songs (one per line):").pack(anchor="w", padx=10, pady=5)
song_text = tk.Text(root, width=50, height=7)
song_text.pack(padx=10, pady=5)

tk.Button(root, text="Save Playlist", command=save_playlist).pack(pady=5)
tk.Button(root, text="View Playlists", command=load_playlists).pack(pady=5)

playlist_listbox = tk.Listbox(root, width=40, height=6)
playlist_listbox.pack(padx=10, pady=5)
playlist_listbox.bind("<<ListboxSelect>>", show_playlist)

tk.Label(root, text="Songs in Selected Playlist:").pack(anchor="w", padx=10, pady=5)
display_text = tk.Text(root, width=50, height=7, state="disabled")
display_text.pack(padx=10, pady=5)

root.mainloop()
