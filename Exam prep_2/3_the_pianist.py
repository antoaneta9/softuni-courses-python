
songs = {}
number_of_songs = int(input())
for _ in range(number_of_songs):
    piece, composer, key = input().split('|')
    if piece not in songs:
        songs[piece] = {
            'composer': composer,
            'key': key
        }

while True:
    cmd = input()
    if cmd == 'Stop':
        break

    parts = cmd.split('|')
    if parts[0] == 'Add':
        piece = parts[1]
        composer = parts[2]
        key = parts[3]
        if piece not in songs:
            songs[piece] = {
                'composer': composer,
                'key': key
            }
            print(f"{piece} by {composer} in {key} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    elif parts[0] == 'Remove':
        piece = parts[1]
        if piece in songs:
            print(f"Successfully removed {piece}!")
            del songs[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif parts[0] == 'ChangeKey':
        piece = parts[1]
        new_key = parts[2]
        if piece in songs:
            songs[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for k,v in songs.items():
    print(f"{k} -> Composer: {v['composer']}, Key: {v['key']}")