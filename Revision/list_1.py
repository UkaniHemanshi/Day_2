song_list=[]

def add_song():
    global song_list
    song_title = input("Enter the songlist string by comma: ")
    song_list = [song for song in song_title.split(",")]
    return song_list

def remove_song(song_name,song_list):
    if song_name in song_list:
        song_list.remove(song_name)
        return song_list
    else:
        print("This song doesn't exists")

def display_song_string(song_list):
    result = ",".join(song_list)
    return result

def slice_list_data(song_list,start,end):

    return song_list[start:end]


print(add_song())
remove_sname = input("Enter the song name you want to remove:")
print(remove_song(remove_sname,song_list))
print(display_song_string(song_list))
print(slice_list_data(song_list,1,3))

