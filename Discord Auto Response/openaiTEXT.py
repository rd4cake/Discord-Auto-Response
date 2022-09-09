import os
import openai


def respond(text):
    openai.api_key = "YOUR API KEY"

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=text,
      temperature=0.5,
      max_tokens=60,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0,
      stop=["You:"])
    return response.choices[0].text

#"You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
