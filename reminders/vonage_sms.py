import vonage

# Initialize vonage client
client = vonage.Client(key="7b81c752", secret="qox1ae62QiO2mzJy")

# Construct message using vonage client
sms = vonage.Sms(client)

# Send message using vonage client
responseData = sms.send_message(
    {
        "from": "Remind me later",
        "to": "918086130189",
        "text": "Get up and do the work",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
