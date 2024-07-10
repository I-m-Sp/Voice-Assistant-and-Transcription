import google.generativeai as genai
import api
def request(data):
    genai.configure(api_key=api.GemApi)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(data)
    print(response.text)