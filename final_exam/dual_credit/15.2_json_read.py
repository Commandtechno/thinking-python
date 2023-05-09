import json

tracks = json.load(open("tracks.json"))

for track in tracks:
    print(track["track"]["name"])