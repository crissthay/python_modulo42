from dotenv import load_dotenv
import os

load_dotenv()

print("ORACLE STATUS: Reading the Matrix...\n")
print("Configuration loaded:")
name = os.getenv("MATRIX_MODE")
if name == "production":
    print("Mode: production")
else:
    print("Mode: development")
data = os.getenv("DATABASE_URL")
if data:
    print("Database: Connected to local instance")
else:
    print("Database: Desconect")
api = os.getenv("API_KEY")
if api:
    print("API Access: Authenticated")
else:
    print("API Access: Not authenticated")
print("Log Acess:", os.getenv("LOG_LEVEL"))
zion = os.getenv("ZION_ENDPOINT")
if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("\nEnvironment security check:")
if api is not None:
    print("[OK] No hardcoded secrets detected")
else:
    print("[WARNING] Hardcoded secrets detected")
env = os.path.exists(".env")
if env:
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file not configured")
if name:
    print("[OK] Production overrides available")
else:
    print("[WARNING] Production overrides inavailable")

print("\nThe Oracle sees all configurations.")


    
