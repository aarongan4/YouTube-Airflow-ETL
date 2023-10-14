import os
import json 
import googleapiclient.discovery
import pandas as pd
import s3fs

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
def run_youtube_etl():
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "<insert gcloud developer key>"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId="gbDl28Hx9TA"
    )
    response = request.execute()

    # response_items = json.dumps(response)

    response_items = response["items"]


        
    def process_comments(response):
        comments = []
        for comment in response:
                author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comment_text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
                publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
                comment_info = {'author': author, 
                        'comment': comment_text, 'published_at': publish_time}
                comments.append(comment_info)
        print(f'Processed {len(comments)} comments.')
        return comments


    comments = process_comments(response_items)

    comments_df = pd.DataFrame(comments)
    return comments_df
    # comments_df.to_csv('s3://<your s3 bucket file path name>')

run_youtube_etl()
