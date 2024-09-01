from google.oauth2 import service_account
import googleapiclient.discovery

# Define the scope and service account file
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
SERVICE_ACCOUNT_FILE = "path/to/service_account.json"

# Authenticate using service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Build the API client
youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

# Retrieve video views
request = youtube.videos().list(
    part="statistics",
    id="VIDEO_ID"
)
response = request.execute()

print(f"Video Views: {response['items'][0]['statistics']['viewCount']}")