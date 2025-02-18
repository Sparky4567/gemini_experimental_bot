from google import genai

from settings.config import API_KEY
from packages.speak_back_module.speak_module import Speak_Back
class Gemini_Request:
    def __init__(self):
        self.api_key = API_KEY
        self.speak_mod = Speak_Back()

    def request_method(self):
        try:
            client = genai.Client(api_key=API_KEY)
            user_input=str(input("\n\nWrite your input here\n\n")).lower().strip()
            if(user_input != "" and user_input is not None) and user_input != "exit" and user_input != "quit":
                user_input=user_input+", do not use any extra markup such as asterisks or special characters while providing answers"
                response = client.models.generate_content_stream(
                    model="gemini-2.0-flash",
                    contents=[user_input])     
                full_response = "" 
                for chunk in response:
                    full_response = full_response + chunk.text
                full_response = str(full_response).strip()
                self.speak_mod.speak_back(full_response)
                print("\n\n{}".format(full_response))
                self.request_method()
        
        
            elif(user_input=="exit"):
                print("\n\nExiting...\n\n")
                quit()

            elif(user_input=="quit"):
                print("\n\nExiting...\n\n")
                quit()

            else:
                self.request_method()

        except Exception as e:
            print("\n\nException in Gemini request\n\n")
    
    

    