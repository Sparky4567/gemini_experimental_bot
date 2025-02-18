from packages.request_package.request_module import Gemini_Request

try:
    gemini_request = Gemini_Request()
    gemini_request.request_method()
except KeyboardInterrupt as e:
    print("\n\nExiting...\n\n")
    quit()

