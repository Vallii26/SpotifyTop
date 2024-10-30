import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

os.system('clear')

def get_top_spotify_data(limit, range, rangetime):
    os.system('clear')
    
    # Set up authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id='SPOTIFY_CLIENT_ID',
        client_secret='SPOTIFY_SECRET_ID',
        redirect_uri='http://localhost:3000',
        scope='user-top-read'
    ))

    # Get top artists
    top_artists = sp.current_user_top_artists(limit=limit, time_range=rangetime)
    print(f'Your top {limit} artists for {range} are:')
    for idx, artist in enumerate(top_artists['items']):
        print(f"{idx + 1}. {artist['name']}")

    # Get top tracks
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=rangetime)
    print(f'\nYour top {limit} songs for {range} are:')
    for idx, track in enumerate(top_tracks['items']):
        print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")

# Main program loop for changing profiles
while True:
    try:
        limit = int(input('How many artists and songs do you want to know? --> '))
        range = input("Do you want to know short term(last 30 days), medium term(last 6 months) or long term(all time)? (short, medium, long) --> ")
        if range.lower() == 'short':
            rangetime = 'short_term'
            range = 'the last 30 days'
            get_top_spotify_data(limit, range, rangetime)
        elif range.lower() == 'medium':
            rangetime = 'medium_term'
            range = 'the last 6 months'
            get_top_spotify_data(limit, range, rangetime)
        elif range.lower() == 'long':
            rangetime='long_term'
            range = 'all time'
            get_top_spotify_data(limit, range, rangetime)
        else:
            print('Please select a valid option')
        
        # Ask if the user wants to switch profiles
        change_profile = input("\nWould you like to switch Spotify profiles? (yes/no): ").strip().lower()
        if change_profile != 'yes':
            print("Exiting.")
            break
    except Exception as e:
        print(f"An error occurred: {e}")