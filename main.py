import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI API KEY was not found, make sure that it is defined in .env file.")


def main():
    client = genai.Client(api_key=api_key)
    
    prompt = "Hard coded string as a placeholder"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response.text)

if __name__ == "__main__":
    main()
