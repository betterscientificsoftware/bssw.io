# required install package: Run those two lines below in the Terminal
# pip install oauth2client==1.5.2
# pip install gspread==0.6.2

import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import os
from datetime import datetime

# Find the correct folder
FOLDER_LOOKUP = {
    "Original Experience": "Articles",
    "Curated Links": "CuratedContent",
    "Event": "Events",
    "Blog Article": "Site",
}

# Below are the indexes of necessary information in the Google Sheet. Need to change if needed

FOLDER = 14  # index of folder name
LAST_NAME = 4  # index of last name
ARTICLE_NAME = [15, 17, 19]  # index of file name
TOPICS = range(8, 14)  # indexes of topic
CATEGORY = 7  # index of category
CONTENTS = [16, 18, 20]  # indexes of file content
EMAIL = 5  # index of file name
EVENT_TITLE = 21
EVENT_START = 22
EVENT_END = 23
EVENT_LOCATION = 24
EVENT_WEBSITE = 25
EVENT_SHORT_DESC = 26
EVENT_LONG_DESC = 27
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
    name = values[LAST_NAME] + get_filename(values)

    filepath = "{}/{}{}.md".format(folder, PREFIX, name)

    # check if the file already exist
    if os.path.isfile(filepath):
        suffix = 1
        while True:
            filepath = "{}/{}_{}{}.md".format(folder, PREFIX, name, suffix)
            if not os.path.isfile(filepath):
                return filepath
            suffix += 1
    return filepath


# convert date the the correct format
def convert_date(date_str1, date_str2):
    # convert string date to date
    date1 = datetime.strptime(date_str1, '%m/%d/%Y')
    date2 = datetime.strptime(date_str2, '%m/%d/%Y')

    # convert date bback to string in the right format
    if date1.year == date2.year:
        return "{} - {}".format(datetime.strftime(date1, "%B %d"), datetime.strftime(date2, "%B %d, %Y"))
    return "{} - {}".format(datetime.strftime(date1, "%B %d, %Y"), datetime.strftime(date2, "%B %d, %Y"))


# get file name
def get_filename(values):
    for i in ARTICLE_NAME:
        if values[i]:
            return values[i]
    return ""


# get the topic from Google sheet
def get_topic(values):
    for i in TOPICS:
        if values[i]:
            return values[i]
    return ""


# write content to file
def write_file(values, fo):
    # check if the event
    if values[EVENT_LOCATION] != "":
        fo.write("# {}\n\n".format(values[EVENT_TITLE]))
        fo.write("- Dates: " + convert_date(values[EVENT_START], values[EVENT_END]))
        fo.write("\n- Location: {}\n".format(values[EVENT_LOCATION]))
        fo.write("- Event Website: {}\n\n".format(values[EVENT_WEBSITE]))
        fo.write(" {}\n\n".format(values[EVENT_SHORT_DESC]))
        fo.write("**Description**: {}\n".format(values[EVENT_LONG_DESC]))

    # for blog, article and curated links
    else:
        fo.write("### {}\n".format(get_filename(values)))
        for i in CONTENTS:
            if values[i] != "":
                fo.write(values[i]+"\n")


# write content to files
def process_value(values):
    # get topic and file path
    topic = get_topic(values)
    filepath = generate_filepath(values)

    # open file and write
    with open(filepath, "w") as fo:
        write_file(values, fo)
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
    doc = gc.open_by_key('16-RpWOIeOCU66WdrIGjMNl6f3qIFH7H8D9_oPX2O2j4')

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
