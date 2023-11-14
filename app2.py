import openai
import requests
import json
import config

prompt = "Embark on a voyage into the future, where interior design transcends boundaries–a concept that redefines luxury in a high-tech living space. Picture a cat in a poncho on a sleek and elegant furniture, bathed in the glow of holographic displays that serve as portals to new dimensions. As the Leica M10-R and the Canon EOS R5 capture each detail with utmost precision, the allure of innovative smart home technologies further enhances the experience. Witness the seamless integration of form and function, as this visionary concept sets the stage for a harmonious coexistence between human life and cutting-edge technology. Step into a realm where every surface tells a story, and where the boundaries of design are pushed beyond their limits. Let your imagination run wild as you explore the possibilities of tomorrow’s living spaces. –v 5.2 –stylize 1000 –ar 16:9"

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