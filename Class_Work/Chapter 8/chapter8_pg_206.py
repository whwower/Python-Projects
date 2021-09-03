#8.7
def make_album(artist_name, album_title, number_of_songs = None):
	album = {'artist' : artist_name, 'title' : album_title}
	if number_of_songs:
		album['number_of_songs'] = number_of_songs
	return album
album_0 = make_album('Trevor', 'Noah')
album_1 = make_album('Somizi', 'Fati')
album_2 = make_album('Doit', 'Gora')
album_3 = make_album('David', 'Green', 12)

print(album_0)
print(album_1)
print(album_2)
print(album_3)

#8.8
def make_album(artist_name, album_title):
	album = {'artist' : artist_name, 'title' : album_title}
	return album

while True:
	print("\nEnter the album's artist")
	print('\nEnter "quit" to quit')

	artistN = input("Artist:")
	if artistN == 'quit':
		break
	album_name = input("Album:")
	if album_name == 'quit':
		break
	album_0 = make_album(artistN, album_name)
	print(album_0)


