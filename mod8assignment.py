import json
import csv

def load_songs(filename):
    """
    Loads the song list from a JSON file.
    Handles the case where the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get("songs", [])  # returns list of songs
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def display_songs(songs):
    """
    Displays all songs with a number for user selection.
    """
    print("\nAvailable Songs:")
    for i, song in enumerate(songs):
        title = song.get("title", "Unknown Title")
        artist = song.get("artist", "Unknown Artist")
        album = song.get("album", "Unknown Album")
        genre = song.get("genre", "Unknown Genre")  # or other custom key
        print(f"{i + 1}. '{title}' by {artist} | Album: {album} | Genre: {genre}")

def get_user_playlist(songs):
    """
    Allows user to build a playlist by selecting songs from the list.
    """
    playlist = []
    while True:
        choice = input("\nEnter song number to add to playlist (or type 'done' to finish): ")
        if choice.lower() == 'done':
            break
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(songs):
                playlist.append(songs[index])
                print(f"Added: {songs[index]['title']} by {songs[index]['artist']}")
            else:
                print("Invalid number. Try again.")
        else:
            print("Invalid input. Please enter a number or 'done'.")
    return playlist

def save_playlist_to_csv(playlist, filename):
    """
    Saves the selected playlist to a CSV file with headers.
    """
    if not playlist:
        print("Playlist is empty. Nothing was saved.")
        return

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=playlist[0].keys())
        writer.writeheader()
        writer.writerows(playlist)
    print(f"\n✅ Playlist saved to '{filename}'.")

def main():
    """
    Main function to coordinate the program flow.
    """
    json_filename = "songs.json"
    csv_filename = "playlist.csv"

    songs = load_songs(json_filename)
    if not songs:
        return  # exit naturally if file is missing or empty

    display_songs(songs)
    playlist = get_user_playlist(songs)
    save_playlist_to_csv(playlist, csv_filename)

#  Kick-off the program
if __name__ == "__main__":
    main()
