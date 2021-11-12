from __future__ import print_function
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1nx2huNH68pfKMwUY_oOxkfPIWb9X-SLL93kaLDS4jQM'
SAMPLE_RANGE_NAME = 'Sheet1!A2:B'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    service = build('sheets', 'v4', developerKey=os.environ["GS_API_KEY"])

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        d = { 'sessions': [ { 'name': v[0], 'level': v[1] } for (v) in values ] }
        with open("../sessions.json", "w") as outfile:
            json.dump(d, outfile, indent=4)

if __name__ == '__main__':
    main()
