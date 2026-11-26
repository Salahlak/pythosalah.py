
import requests
from datetime import datetime, timezone

print("=== PYTHON HOSTING TEST ===")

print("Python is running successfully.")
print("Requests version:", requests.__version__)

try:
    response = requests.get(
        "https://httpbin.org/get",
        timeout=20
    )

    response.raise_for_status()

    print("API connection: SUCCESS")
    print("HTTP Status:", response.status_code)

except requests.RequestException as error:
    print("API connection: FAILED")
    print("Error:", error)
    raise

print("Execution time:", datetime.now(timezone.utc))
print("=== TEST COMPLETED ===")
