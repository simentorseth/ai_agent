import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError(
        "GEMINI API KEY was not found, make sure that it is defined in .env file.")


def get_token_counts(response):
    if response.usage_metadata is None:
        raise RuntimeError(
            "Promt and response tokens are empty, likely a failed API request.")

    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    return prompt_token_count, response_token_count


def print_response(prompt, response, verbose):
    prompt_token_count, candidates_token_count = get_token_counts(response)

    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {candidates_token_count}")
        print(f"Response:")
        print(response.text)
    else:
        print(f"Response:")
        print(response.text)


def main():
    parser = argparse.ArgumentParser(description="Toy AI agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)

    messages = [types.Content(
        role="user", parts=[types.Part(text=args.user_prompt)])]

    prompt = args.user_prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    print_response(prompt, response, args.verbose)


if __name__ == "__main__":
    main()
