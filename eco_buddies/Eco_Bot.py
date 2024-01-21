"""
This module is used to test the Eco-Bot vision functionality.
"""
import io
import base64
import time
import os
import cv2
from PIL import Image
from IPython.display import display, Image, Audio, HTML, Video, clear_output
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np

# Load API keys from .env file
load_dotenv()

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

class EcoBot_Vision:
    """
    This is a simple Eco-Bot chat bot that uses OpenAI's GPT-4-1106 preview model
    for image processing.
    """
    def __init__(self):
        """
        Initializes a new instance of the class.

        This function is the constructor for the class. It is called when a new object of the class is created. It initializes the object by calling the constructor of the superclass.

        Parameters:
            None

        Returns:
            None
        """
        super().__init__()
        self.conversation_history = []


    def run_image(self):
        """
        Runs the image processing on the user-specified image.

        Returns:
            None

        TODO:
            - Prompt the user to input the image file path.
            - Display the image and the response.
        """
        image_path = input("Enter the path to the image file: ")
        try:
            with open(image_path, "rb") as f:
                image = Image.open(io.BytesIO(f.read()))
                image.show()
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "What’s in this image?"},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                                },
                            },
                        ],
                    }
                ]
                response = client.chat.completions.create(
                    model="gpt-4-vision-preview",
                    messages=messages,
                    max_tokens=300,
                )
                eco_vision_response = response.choices[0].message.content
                eval(eco_vision_response)
                print(eco_vision_response)
        except FileNotFoundError:
            raise FileNotFoundError("Image file not found.")

class EcoBot_Video_Vision:
    """
    This is a simple Eco-Bot chat bot that uses OpenAI's GPT-4-1106 preview model
    for video processing.
    """
    def __init__(self):
        super().__init__()
    def run_video(self, video_path):
        video = cv2.VideoCapture(video_path)

        base64Frames = []
        while video.isOpened():
            success, frame = video.read()
            if not success:
                break
            _, buffer = imencode(".jpg", frame)
            base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

        video.release()
        print(len(base64Frames), "frames read.")

    def display_video(self, base64Frames):
        display_handle = display(None, display_id=True)
        for img in base64Frames:
            display_handle.update(Image(data=base64.b64decode(img.encode("utf-8"))))
            time.sleep(0.025)

    def prompt(self, base64Frames):
        PROMPT_MESSAGES = [
            {
                "role": "user",
                "content": [
                    "These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.",
                    *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::10]),
                ],
            },
        ]
        params = {
            "model": "gpt-4-vision-preview",
            "messages": PROMPT_MESSAGES,
            "api_key": os.environ["OPENAI_API_KEY"],
            "headers": {"Openai-Version": "2020-11-07"},
            "max_tokens": 200,
        }

        result = openai.chat.completions.create(**params)
        print(result.choices[0].message.content)

    def create_narraitor(self, base64Frames):
        PROMPT_MESSAGES = [
            {
                "role": "user",
                "content": [
                    "These are frames of a video. Create a short voiceover script in the style of David Attenborough. Only include the narration.",
                    *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::10]),
                ],
            },
        ]
        params = {
            "model": "gpt-4-vision-preview",
            "messages": PROMPT_MESSAGES,
            "api_key": os.environ["OPENAI_API_KEY"],
            "headers": {"Openai-Version": "2020-11-07"},
            "max_tokens": 500,
        }

        result = openai.chat.completions.create(**params)
        print(result.choices[0].message.content)