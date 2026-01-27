from google import genai
from PIL import Image

client = genai.Client(api_key="AIzaSyA6UaiupZ3G-HLKvYuOL5XeE6PLPQkfsYI")

img = Image.open("test.jpeg")

res = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=[img, "Say OK"]
)

print(res.text)

