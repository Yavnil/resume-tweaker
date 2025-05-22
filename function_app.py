import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="resume_send_and_gather", auth_level=func.AuthLevel.FUNCTION)
def resume_send_and_gather(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON body.", status_code=400)

    resume_url = req_body.get('resumeUrl')
    job_description = req_body.get('jobDescription')

    if resume_url and job_description:
        # Process the data as needed
        return func.HttpResponse(
            f"Received resume URL: {resume_url}\nReceived job description: {job_description}",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please provide both resumeUrl and jobDescription in the request body.",
            status_code=400
        )