import os

replacements = {
    # Titles in HTML Playlist
    '<div class="playlist-title">Happy Birthday To You!</div>': '<div class="playlist-title">Jab Koi Baat</div>',
    '<div class="playlist-title">Birthday Celebration!</div>': '<div class="playlist-title">Home (Edith Whiskers)</div>',
    '<div class="playlist-title">Party Time!</div>': '<div class="playlist-title">Die With A Smile</div>',

    # In HTML Main Player
    '<div class="track-title" id="track-title">Happy Birthday To You!</div>': '<div class="track-title" id="track-title">Jab Koi Baat</div>',

    # In JS object
    'title: "Happy Birthday To You!"': 'title: "Jab Koi Baat"',
    'title: "Birthday Celebration!"': 'title: "Home (Edith Whiskers)"',
    'title: "Party Time!"': 'title: "Die With A Smile"',

    'src: "file/hbd.mp3"': 'src: "song1.mp3"',
    'src: "aud.mp3"': 'src: "song2.mp3"'
}

for fpath in ['music.html', 'happybday/music.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated music metadata in html")
