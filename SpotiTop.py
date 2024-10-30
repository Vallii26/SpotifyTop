import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

os.system('clear')

def get_top_spotify_data(limit, range_description, time_range):
    os.system('clear')
    
    # Set up authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='SPOTIFY_CLIENT_ID',
        client_secret='SPOTIFY_SECRET_ID',
        redirect_uri='http://localhost:3000',
        scope='user-top-read'
    ))

    # Get top artists and determine genres
    top_artists = sp.current_user_top_artists(limit=limit, time_range=time_range)
    genres = []
    print(f'Your top {limit} artists for {range_description} are:')
    for idx, artist in enumerate(top_artists['items']):
        print(f"{idx + 1}. {artist['name']}")
        genres.extend(artist['genres'])

    # Get top tracks and determine albums
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
    albums = set()
    print(f'\nYour top {limit} songs for {range_description} are:')
    for idx, track in enumerate(top_tracks['items']):
        print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
        albums.add(track['album']['name'])

    # Display most listened albums
    print(f"\nYour top {limit} albums for {range_description} are:")
    for idx, album in enumerate(albums):
        print(f"{idx + 1}. {album}")

    # Display most listened genres
    genre_counts = {genre: genres.count(genre) for genre in set(genres)}
    top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:limit]
    print(f"\nYour top {limit} genres for {range_description} are:")
    for idx, genre in enumerate(top_genres):
        print(f"{idx + 1}. {genre}")

# Main program loop for changing profiles
while True:
    try:
        limit = int(input('How many artists, songs, albums, and genres do you want to know? --> '))
        range_selection = input("Do you want to know short term (last 30 days), medium term (last 6 months), or long term (all time)? (short, medium, long) --> ").strip().lower()
        
        if range_selection == 'short':
            time_range = 'short_term'
            range_description = 'the last 30 days'
        elif range_selection == 'medium':
            time_range = 'medium_term'
            range_description = 'the last 6 months'
        elif range_selection == 'long':
            time_range = 'long_term'
            range_description = 'all time'
        else:
            print('Please select a valid option')
            continue

        get_top_spotify_data(limit, range_description, time_range)
        
        # Ask if the user wants to switch profiles
        change_profile = input("\nWould you like to switch Spotify profiles? (yes/no): ").strip().lower()
        if change_profile != 'yes':
            print("Exiting.")
            break
    except Exception as e:
        print(f"An error occurred: {e}")
