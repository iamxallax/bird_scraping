import openai
import pathlib
import netrc

__, __, api_key = netrc.netrc().authenticators('openai')

client = openai.OpenAI(api_key=api_key)

def tts(text, filename, voice="onyx"):
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=voice,
        input=text,
    ) as response:
        response.stream_to_file(filename + ".mp3")

