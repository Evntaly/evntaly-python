import requests

class EvntalySDK:
    """
    EvntalySDK is a Python SDK for interacting with the Evntaly event tracking platform.
    It allows developers to initialize the SDK, track events, identify users, and check usage limits.
    """

    BASE_URL = "https://evntaly.com/prod"

    def __init__(self, developer_secret: str, project_token: str):
        """
        Initialize the SDK with a developer secret and project token.
        """
        self.developer_secret = developer_secret
        self.project_token = project_token
        self.tracking_enabled = True

    def check_limit(self) -> bool:
        """
        Checks if the usage limit allows further tracking.
        """
        url = f"{self.BASE_URL}/api/v1/account/check-limits/{self.developer_secret}"
        headers = {
            "Content-Type": "application/json",
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            if "limitReached" not in data:
                print("Unexpected response:", data)
                return False  # Default behavior if key is missing

            return not data["limitReached"]  # ✅ Return True if limit is NOT reached
        except requests.RequestException as e:
            print(f"Error checking limit: {e}")
            return False  # Fails safe (assumes limit is reached)

    def track(self, event_data: dict):
        """
        Tracks an event if tracking is enabled and within limits.
        """
        if not self.tracking_enabled:
            print("Tracking is disabled. Event not sent.")
            return

        if not self.check_limit():
            print("checkLimit returned false. Event not sent.")
            return

        url = f"{self.BASE_URL}/api/v1/register/event"
        headers = {
            "Content-Type": "application/json",
            "secret": self.developer_secret,
            "pat": self.project_token,
        }
        
        try:
            response = requests.post(url, json=event_data, headers=headers)
            response.raise_for_status()
            print("Track event response:", response.json())
        except requests.RequestException as e:
            print(f"Track event error: {e}")

    def identify_user(self, user_data: dict):
        """
        Identifies a user in the system.
        """
        url = f"{self.BASE_URL}/api/v1/register/user"
        headers = {
            "Content-Type": "application/json",
            "secret": self.developer_secret,
            "pat": self.project_token,
        }
        
        try:
            response = requests.post(url, json=user_data, headers=headers)
            response.raise_for_status()
            print("Identify user response:", response.json())
        except requests.RequestException as e:
            print(f"Identify user error: {e}")

    def disable_tracking(self):
        """
        Disables event tracking.
        """
        self.tracking_enabled = False
        print("Tracking disabled.")

    def enable_tracking(self):
        """
        Enables event tracking.
        """
        self.tracking_enabled = True
        print("Tracking enabled.")
