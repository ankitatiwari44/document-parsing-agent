from google import genai

client = genai.Client(api_key="AIzaSyA6UaiupZ3G-HLKvYuOL5XeE6PLPQkfsYI")

for m in client.models.list():
    print(m.name)
