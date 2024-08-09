# %%
!sudo apt-get install build-essential libssl-dev libffi-dev python3-dev


# %%
!python -m venv myenv
!source myenv/bin/activate
!pip install poe-api-wrapper


# %%
from poe_api_wrapper import AsyncPoeApi
import asyncio

tokens = {
    'p-b': 'fmU9cikJdfOeXdy8aT7YpQ%3D%3D',
    'p-lat': 'nwDTrz49byQ0Bzn7B5C8me|2024-08-09T02:40:26.818Z',
}

async def main():
    response = ""  # Initialize an empty string to store the response
    client = await AsyncPoeApi(tokens=tokens).create()

    message = "Explain general relativity in simple terms"  # Replace with your actual query


    async for chunk in client.send_message(bot="gpt3_5", message=message):
        print(chunk["response"], end='', flush=True)
        response += chunk["response"]

    print("\nFull response:", response)

    return response


final_response = asyncio.run(main())

# You can use final_response for further processing



