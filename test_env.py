from dotenv import load_dotenv
import os

load_dotenv()

print("URL:", os.getenv("MISP_URL"))
print("KEY:", os.getenv("MISP_API_KEY"))
