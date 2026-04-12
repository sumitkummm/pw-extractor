import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def get_authenticated_service():
    # Env vars se credentials load karna
    creds = Credentials(
        token=None,
        refresh_token=os.getenv("1//04RaA-UWBYChcCgYIARAAGAQSNwF-L9IrFmq_DVXusg9O_XlHvU9ZNy1dllkYmwAeXRc5q5GCgKEbG3Dk2AiHwnOv-5CWY0Z2bbM"),
        client_id=os.getenv("448926041465-3am9ttrhkg21a15l0krfdqc3i46uentt.apps.googleusercontent.com"),
        client_secret=os.getenv("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"),
        token_uri="https://oauth2.googleapis.com/token"
    )
    return build('youtube', 'v3', credentials=creds)

def upload_video(file_path, title, description):
    try:
        youtube = get_authenticated_service()
        request_body = {
            'snippet': {
                'title': title,
                'description': description,
                'categoryId': '27' # Education
            },
            'status': {
                'privacyStatus': 'unlisted',
                'selfDeclaredMadeForKids': False,
            }
        }
        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
        response = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=media
        ).execute()
        return f"https://www.youtube.com/watch?v={response['id']}"
    except Exception as e:
        print(f"YouTube Error: {e}")
        return None