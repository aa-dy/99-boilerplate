# First Prompt

Create a Python application with FastAPI that functions as a serverless API. This application will be deployed on Netlify using Netlify Functions. The response should include all necessary files and configurations for a complete, production-ready setup.

Core Functionality:

Endpoint: The API should have a single GET endpoint.

Path: The path for this endpoint must be /hello/{name}.

Input: The endpoint should accept a path parameter named name which is a string.

Response: The endpoint must return a JSON response with a single key, message. The value of this key should be a string in the format

`"Hello, <name>!", where <name> is the value provided in the path parameter.`

Deployment and Configuration:

Platform: Netlify Functions.

Files: Generate the following files:

main.py: The main FastAPI application file.

requirements.txt: A list of all required Python packages and their versions (e.g., fastapi, uvicorn, python-dotenv).

netlify.toml: The configuration file for Netlify that directs it to the function. This file should be configured to recognize the Python function and set up the build process correctly.

CORS: The application must include a CORS middleware to allow requests from any origin (*). This is crucial for a frontend application to be able to access the API. The CORSMiddleware from FastAPI should be used for this purpose.

Security: The API should be secure by default, and the CORS configuration should be a top priority for frontend integration.

Comments: The code should be well-commented to explain the purpose of each section, including the endpoint definition, the middleware, and the serverless function handler wrapper.

Serverless Wrapper: The main.py file should include a wrapper function that makes the FastAPI application compatible with the Netlify Functions environment, which typically expects a handler function. This wrapper should handle the incoming request and return the appropriate response object.

Dependency Management: The requirements.txt file should contain all the necessary dependencies for the application to run successfully on Netlify's serverless environment.

Instructions for the LLM:

Ensure the code is self-contained and ready to be deployed.

Provide a brief, clear explanation of how the files work together.

The final response must be concise and contain only the requested files.
