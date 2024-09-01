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

# List available report types
report_types = youtube.reporting().reportTypes().list().execute()
for report_type in report_types['reportTypes']:
    print(f"Report Type ID: {report_type['id']} - Name: {report_type['name']}")

# Create a reporting job
job = youtube.reporting().jobs().create(body={'reportTypeId': 'YOUR_REPORT_TYPE_ID'}).execute()

# Download the report
report_file = youtube.reporting().media().download(jobId=job['id'], reportId='REPORT_ID').execute()
with open('report.csv', 'wb') as f:
    f.write(report_file)
