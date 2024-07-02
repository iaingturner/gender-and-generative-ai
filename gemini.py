import google.generativeai as genai
import os

os.environ["API_KEY"]='AIzaSyAMpRKlchsLO5VVP4NAhEcVRs7bY0fXTHM'

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')



response = model.generate_content("Write a story about a AI and magic")
print(response.text)