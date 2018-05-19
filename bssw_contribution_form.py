# This script reads input from the Google Form:
# https://docs.google.com/forms/d/e/1FAIpQLScuM_jGV5MO2K6CCurHlC7s_YwIVQcOuLPExobCq9uDnX4p5Q/viewform
# Each submission is converted into an article of one of the contribution types supported by the site https://bssw.io

# required install package: Run those two lines below in the Terminal
# pip install oauth2client==1.5.2
# pip install gspread==0.6.2

import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import json
import os
from datetime import datetime
from dateutil.parser import *


# Find the correct contribution type
CONTRIBUTION_LOOKUP = {
    "Original experience": "Articles",
    "Curated links": "CuratedContent",
    "Event": "Events",
    "Blog Article": "Site",
}

# Below are the indexes of necessary information in the Google Sheet.
# Column "A" in Tab "Form Responses 1" will be index 0, "B" is index 1 and so on.

TIMESTAMP = 0 # Date and time of contribution submission
FIRST_NAME = 3  # first name
LAST_NAME = 4  # last name
EMAIL_ADDRESS = 5 # contributor's email address
GITHUB_ID = 6 # contributor's GitHub ID
CATEGORY = 7  # category (Planning, Development, Performance, Reliability, Collaboration, Skills)
TOPICS = range(8, 13)  # each category has a collection of possible topic.  We scan all since only the selected category will have topics.
CONTRIBUTION_TYPE = 14  # Possible values: Original experience, Blog article, Curated Links, Event
FILE_KEY = 15 # 20 or fewer characters used to construct a unique file name
ARTICLE_TITLE = [ 16, 18, 20] # Contribution's title
ARTICLE_TEXT = [17, 19, 21]  # indexes of file content
EVENT_TITLE = 22
EVENT_START = 23
EVENT_END = 24
EVENT_LOCATION = 25
EVENT_WEBSITE = 26
EVENT_SHORT_DESC = 27
EVENT_LONG_DESC = 28
PREFIX = "BSSW_GENERATED_FILES"  # Folder for Generated Files


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
    # decide the contribution type for build file prefix
    contribution_type = CONTRIBUTION_LOOKUP[values[CONTRIBUTION_TYPE]]

    # name of the file and filepath
    name = values[LAST_NAME] + values[FILE_KEY]

    filepath = "{}/{}/{}.md".format(PREFIX, contribution_type, name)

    # check if the file already exist
    if os.path.isfile(filepath):
        suffix = 1
        while True:
            filepath = "{}/{}/{}{}.md".format(PREFIX, contribution_type, name, suffix)
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


# get the topic from Google sheet
def get_topic(values):
    for i in TOPICS:
        if values[i]:
            return values[i]
    return ""


# write content to file
def write_file(values, fo):

    timestamp = parse(values[TIMESTAMP])
    # build contributor string.  Define as first/last name.
    contributor = values[FIRST_NAME] + " " + values[LAST_NAME]
    # convert to GitHub link if available
    if values[GITHUB_ID]:
        contributor = "[" + contributor + "](https://github.com/" + values[GITHUB_ID] + ")"

# check if the event
    if values[EVENT_LOCATION] != "":
        fo.write("# {}".format(values[EVENT_TITLE]))
        fo.write("\n\n- Dates: " + convert_date(values[EVENT_START], values[EVENT_END]))
        fo.write("\n- Location: {}".format(values[EVENT_LOCATION]))
        fo.write("\n- Event Website: {}".format(values[EVENT_WEBSITE]))
        fo.write("\n\n{}".format(values[EVENT_SHORT_DESC]))
        fo.write("\n\n**Description**: {}".format(values[EVENT_LONG_DESC]))
        fo.write("\n\n#### Contributed by {}".format(contributor))
        fo.write("\n\n#### Publication date: {}".format(timestamp.strftime('%B %d, %Y')))

    # for blog, article and curated links
    else:
        for i in ARTICLE_TITLE:
            if values[i] != "":
                fo.write("\n# "+values[i])

        fo.write("\n\n#### Contributed by {}".format(contributor))
        fo.write("\n\n#### Publication date: {}".format(timestamp.strftime('%B %d, %Y')))

        for i in ARTICLE_TEXT:
            if values[i] != "":
                fo.write("\n\n"+values[i])


# write content to files
def process_value(values):
    # get topic and file path
    topic = get_topic(values)
    filepath = generate_filepath(values)

    print("\nGenerating {}\n".format(filepath))

    # open file and write
    with open(filepath, "w") as fo:
        write_file(values, fo)
        fo.write("\n\n<!---")
        fo.write("\nPublish: no")
        fo.write("\nCategories: {}".format(values[CATEGORY]))
        fo.write("\nTopics: {}".format(topic))
        fo.write("\nLevel: 2")
        fo.write("\nPrerequisites: defaults")
        fo.write("\nAggregate: none")
        fo.write("\n--->\n")



def run():
    print("Read Google Form")

    gc = get_google_client()

    # Open file: key in the Google Sheet URL
#   remember to share the sheet with duong-13@bssw-195403.iam.gserviceaccount.com
    doc = gc.open_by_key('1u6CLr6LbVbbWnpUVij1_z_ugWwAy-5RI7d6QwyFxK00')

    # Open tab: tab name in the Google Sheet
    sheet = doc.worksheet("Form Responses 1")

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
