# required install package: Run those two lines below in the Terminal
# pip install oauth2client==1.5.2
# pip install gspread==0.6.2

import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import os


# Find the correct folder
FOLDER_LOOKUP = {
    "Original Experience": "Articles",
    "Curated Links": "CuratedContent",
    "Event": "Events",
    "Blog Article": "Site",
}

# Below are the indexes of necessary information in the Google Sheet. Need to change if needed

FOLDER = 21  # index of folder name
LAST_NAME = 4  # index of last name
FILE_NAME = 27  # index of file name
TOPICS = range(15, 21)  # indexes of topic
CATEGORY = 14  # index of category
CONTENTS = range(22, 27)  # indexes of file content
PREFIX = "Google"  # Unique Prefix to distinguish between Google Form with currently existing file in bssw.io


# get the google client - no need to change
def get_google_client():
    with open('google_key.json') as f:
        config = json.load(f)

    creds = SignedJwtAssertionCredentials(
        config['client_email'],
        config['private_key'],
        ['https://spreadsheets.google.com/feeds']
    )
    return gspread.authorize(creds)


# create appropriate file path for the new files
def generate_filepath(values):
    # decide the folder to put files in
    folder = FOLDER_LOOKUP[values[FOLDER]]

    # name of the file and filepath
    name = values[LAST_NAME] + values[FILE_NAME]

    filepath = "{}/{}{}.md".format(folder, PREFIX, name)

    # check if the file already exist
    if os.path.isfile(filepath):
        suffix = 1
        while True:
            filepath = "{}/{}{}{}.md".format(folder, PREFIX, name, suffix)
            if not os.path.isfile(filepath):
                return filepath
            suffix += 1
    return filepath


# get the topic from Google sheet
def get_topic(values):
    for i in TOPICS:
        if values[i]:
            return values[i]
    return ""


# write content to files
def process_value(values):
    # get topic and file path
    topic = get_topic(values)
    filepath = generate_filepath(values)

    # open file and write
    with open(filepath, "w") as fo:
        for i in CONTENTS:
            fo.write(values[i])
        fo.write("\n\n<!---")
        fo.write("\nCategories: {}".format(values[CATEGORY]))
        fo.write("\nTopic: {}".format(topic))
        fo.write("\nLevel: 2")
        fo.write("\nPrerequisites: default")
        fo.write("\nAggregate: none")
        fo.write("\n--->")


# clean up the existing files if needed
def cleanup_existing_files():
    for folder in FOLDER_LOOKUP.values():
        for filename in os.listdir(folder):
            if filename.startswith(PREFIX) and filename.endswith(".md"):
                os.remove("{}/{}".format(folder, filename))


def run():
    print("Read Google Form")

    gc = get_google_client()

    # Open file: key in the Google Sheet URL
    doc = gc.open_by_key('1xFi0frEQdLb7a3LPtn8-2zFt2myO5dk15_8soseMkDk')

    # Open tab: tab name in the Google Sheet
    sheet = doc.worksheet("Form Responses 1")

    # Uncomment the below line to clean up the file
    # cleanup_existing_files()

    row_count = sheet.row_count
    # run through all rows of the Google Sheet
    for row in range(2, row_count + 1):
        values = sheet.row_values(row)

        # Blank row
        if not values[0]:
            break

        # process the values collected from Google Sheet
        process_value(values)


if __name__ == '__main__':
    run()
