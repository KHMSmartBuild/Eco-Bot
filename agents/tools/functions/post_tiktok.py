import requests
import json

# Initialize the video upload
url = "https://open.tiktokapis.com/v2/post/publish/inbox/video/init/"
headers = {
    'Authorization': 'Bearer {$UserAccessToken}',
    'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    "source_info": {
        "source": "FILE_UPLOAD",
        "video_size": exampleVideoSize,
        "chunk_size" : exampleChunkSize,
        "total_chunk_count": exampleTotalChunkCount
    }
}
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response
if response.status_code == 200:
    upload_url = response.json()['data']['upload_url']
    print(f"Upload URL: {upload_url}")
else:
    print(f"Error: {response.json()}")
