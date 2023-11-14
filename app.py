import openai
import requests
import json
import config

prompt = "a white siamese cat"

# Define the API endpoint and your API key
api_url = "https://api.openai.com/v1/images/generations"
OPENAI_API_KEY= config.api_key
api_key = OPENAI_API_KEY


# Prepare the headers and payload for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model":"dall-e-3",
    "prompt": prompt,
    "n": 1,
    "size":"1024x1024"
}

# Make the API request
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Handle the response and extract the generated image
if response.status_code == 200:
    response_data = response.json()
    image_url = response_data["data"][0]["url"]
    print("Generated image URL:", image_url)
else:
    print("Failed to generate image:", response.text)
