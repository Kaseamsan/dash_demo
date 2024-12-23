from dotenv import load_dotenv
import os

load_dotenv()

port= os.getenv("PORT")
csv_file= os.getenv("CSV_FILE")
