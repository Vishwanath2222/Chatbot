import openai
import os
import sys
question=input("Q : what is your question?\n")
while True:
  openai.api_key = os.environ['OPENAI_API_KEY']
  if openai.api_key == "":
    sys.stderr.write("""
    You haven't set up your API key yet.

    If you don't have an API key yet, visit:

    https://platform.openai.com/signup

    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"

    """)
    exit(1)

  response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{
          "role": "system",
          "content": "You are a helpful assistant."
      }, 
      #    {"role": "user","content": "Who won the world series in 2020?"},
      #    {"role": "assistant","content":"The Los Angeles Dodgers won the World Series in 2020."},
          {"role": "user",
          "content": question
      }])


  output=response["choices"][0]["message"]["content"]
  print("A : ",output,"\n")
  question=input("Q : what is your next question?\n")