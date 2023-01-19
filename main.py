from googleapiclient.discovery import build

DEVELOPER_KEY = 'DEVELOPER KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


def youtube_search(query, number_of_results=None, next_page_token=None, videos=None):
    if videos is None:
        videos = []
    request = youtube.search().list(
        part="snippet",

        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()
    videos += [video['id'] for video in response['items']]

    if (number_of_results is None or len(videos) < number_of_results) and 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
        return youtube_search(number_of_results, next_page_token, videos=videos)
    else:
        return videos


if __name__ == '__main__':
    ids = youtube_search("bodycam")

