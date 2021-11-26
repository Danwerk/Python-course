"""API."""
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

import os
import googleapiclient.discovery
import googleapiclient.errors

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    sample_spreadsheet_id = id
    sample_range_name = 'A1:A4'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sample_spreadsheet_id,
                                range=sample_range_name).execute()
    values = result.get('values', [])

    flat_list = [item for sublist in values for item in sublist]

    return flat_list


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    ret = []
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=link.split('list=')[1],
        maxResults=50
    )
    response = request.execute()
    for i in response['items']:
        vid_id = (i['snippet']['resourceId']['videoId'])
        yt_id = 'https://youtube.com/watch?v='
        yt_link = yt_id + vid_id
        ret.append(yt_link)

    return ret


if __name__ == "__main__":
    print(get_links_from_playlist('https://www.youtube.com/watch?v=0C-dNgypA5M&list=PLdVkHRu3zRbJhoHZa8WEEeginurhA5_xp',
                                  'AIzaSyBdc2t-D1tAMWsMTRq4QbdR3pOiL4uHvpU'))
