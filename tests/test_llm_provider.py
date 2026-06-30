import sys
import os

sys.path.append(os.path.abspath("../src"))

from src.llm_provider import generate_response


reply = generate_response(
    "You are a cute robot named Bubbles. Say hello in one short sentence."
)

print(reply)