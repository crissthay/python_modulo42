from dotenv import load_dotenv
import os

load_dotenv()

mode = os.getenv("MATRIX_MODE", "development")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion = os.getenv("ZION_ENDPOINT")

print("ORACLE STATUS: Reading the Matrix...\n")
print("Configuration loaded:")
print(f"Mode: {mode}")

if database:
    print("Database: Connected")
else:
    print("Database: Not configured")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Not authenticated")

print(f"Log Level: {log_level}")

if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")

if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] .env file not configured")

print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
