#Unus Annus Playlist ID:
#   UUIcgBZ9hEJxHv6r_jDYOMqg

#modified youtube api sample code

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Get all playlist items
    total_expected_videos = 365
    list_of_playlistItems = []

    request = youtube.playlistItems().list(
        part="snippet,contentDetails,id,status",
        maxResults=50,
        playlistId="UUIcgBZ9hEJxHv6r_jDYOMqg"
    )

    has_next = True
    while has_next:
        response = request.execute()
        
        list_of_playlistItems.append(response)
        if "nextPageToken" in response.keys():
            next_page_token = response["nextPageToken"]
            
            request = youtube.playlistItems().list(
                part="snippet,contentDetails,id,status",
                maxResults=50,
                pageToken=next_page_token,
                playlistId="UUIcgBZ9hEJxHv6r_jDYOMqg"
            )
        else:
            has_next = False
    


if __name__ == "__main__":
    main()