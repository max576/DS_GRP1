import csv
from googleapiclient.discovery import build
import datetime
import string

# Set up the YouTube API
developer_key = 'AIzaSyCK_hiwJr-Lifh2vjtxG54ySyqWrno5wAw'
youtube = build('youtube', 'v3', developerKey=developer_key)

# Calculate date one year ago
last_year = datetime.datetime.now() - datetime.timedelta(days=365)
last_year = last_year.isoformat("T") + "Z"  # Format for YouTube API

# Fetch video IDs and titles from the channel within the last year
request = youtube.search().list(
    part="snippet",
    channelId="UCWNpXitY8eJ-ku6M-v25MKw",
    maxResults=50,
    publishedAfter=last_year,
    type="video"
)

# Define a safe filename for the single CSV file
def safe_filename(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)

# Function to fetch comments
def fetch_comments(video_id, video_title):
    comments = []
    next_page_token = None  # Initialize the page token

    while True:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,  # Adjust the number of comments you want here
            pageToken=next_page_token,  # Use the next page token
            textFormat='plainText'
        )
        response = request.execute()

        for item in response.get('items', []):
            comment_snippet = item['snippet']['topLevelComment']['snippet']
            comment = comment_snippet['textDisplay']
            published_at = comment_snippet['publishedAt']
            comment_id = item['snippet']['topLevelComment']['id']
            comments.append((video_id, video_title, comment_id, comment, published_at))

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break  # Exit the loop if there are no more pages

    return comments


# Modified function to save comments into a single CSV file
def save_comments_to_csv(comments):
    filename = "all_biden_youtube_comments.csv"
    with open(filename, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for comment in comments:
            writer.writerow(comment)  # Write comment details

# Write CSV header
with open("all_biden_youtube_comments.csv", 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Video ID", "Video Title","Comment ID", "Comment", "Published At"])  # Write the CSV header

# Execute the request and process each video
response = request.execute()

for item in response['items']:
    video_id = item['id']['videoId']
    video_title = item['snippet']['title']
    comments = fetch_comments(video_id, video_title)
    save_comments_to_csv(comments)
