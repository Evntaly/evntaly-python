from evntaly_python import EvntalySDK 
import os

# Initialize the SDK
evntaly = EvntalySDK("YOUR_DEVELOPER_SECRET", "YOUR_PROJECT_TOKEN")

# Test Check Limit
print("Checking API usage limits...")
limit_ok = evntaly.check_limit()
print(f"✅ Can track events? {limit_ok}")

# Test Track Event
if limit_ok:
    print("\n📌 Sending test event...")
    event_data = {
        "title": "Thread Test Event",
        "description": "Automated test event",
        "data": {
            "user_id": "12345",
            "timestamp": "2025-01-08T09:30:00Z",
            "referrer": "testing_script",
            "email_verified": True
        },
        "tags": ["test", "automation"],
        "notify": True,
        "icon": "🧵",
        "apply_rule_only": False,
        "user": {"id": "12345"},
        "type": "Automated Test",
        "sessionID": "test-session-id",
        "feature": "SDK Testing",
        "topic": "@SDK"
    }
    evntaly.track(event_data)
    print("✅ Event sent successfully!")

# Test Identify User
print("\n🔍 Identifying user...")
user_data = {
    "id": "12345",
    "email": "testuser@example.com",
    "full_name": "Test User",
    "organization": "Testing Inc.",
    "data": {
        "id": "test_user",
        "email": "testuser@example.com",
        "Location": "Global",
        "salary": 100000,
        "timezone": "UTC"
    }
}
evntaly.identify_user(user_data)
print("✅ User identified successfully!")

# Toggle Tracking
print("\n🚫 Disabling tracking...")
evntaly.disable_tracking()

print("🟢 Enabling tracking...")
evntaly.enable_tracking()

print("\n🎉 All tests completed!")