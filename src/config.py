import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Database URL from environment
DATABASE_URL: str = os.getenv("DATABASE_URL") 

# JWT Secret Key from environment
JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY") 
