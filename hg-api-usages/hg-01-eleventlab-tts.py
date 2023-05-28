from gradio_client import Client

# tts means text to speech

# document of module `gradio_client`: https://pypi.org/project/gradio-client/

client = Client("https://elevenlabs-tts.hf.space/")
result = client.predict(
    # str representing input in 'Input Text (250 characters max)' Textbox component
    """
    In the land of the Paris Tower,
    Where the skies delight and empower,
    I met a man named Obama,
    Whose charm was quite the melodrama.
    """,
    "Rachel",  # str representing input in 'Voice' Dropdown component
    "eleven_monolingual_v1",  # str representing input in 'Model' Radio component
    fn_index=0
)
print(result)

