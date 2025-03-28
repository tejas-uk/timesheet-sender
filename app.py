from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import uvicorn

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Gmail credentials from environment variables
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

if not GMAIL_ADDRESS or not GMAIL_PASSWORD:
    raise ValueError("Gmail credentials not found in environment variables")

def send_email(recipient: str, subject: str, body: str, file_path: Optional[str] = None):
    """
    Sends an email with an optional file attachment.
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg["From"] = GMAIL_ADDRESS
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach the file if a file path is provided
        if file_path:
            if not os.path.exists(file_path):
                raise FileNotFoundError("Attachment file does not exist")
            with open(file_path, "rb") as file:
                file_data = file.read()
                file_name = os.path.basename(file_path)
                msg.add_attachment(
                    file_data,
                    maintype="application",
                    subtype="octet-stream",
                    filename=file_name,
                )

        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
            server.send_message(msg)
        return {"status": "success", "message": f"Email sent to {recipient}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/send-email/")
async def send_email_endpoint(
    recipient: str,
    subject: str,
    body: str,
    file: Optional[UploadFile] = None
):
    """
    Endpoint to send an email with an optional file attachment.
    """
    try:
        # Process file upload if provided
        file_path = None
        if file:
            file_path = f"temp_{file.filename}"
            with open(file_path, "wb") as f:
                f.write(await file.read())

        result = send_email(recipient, subject, body, file_path)

        if file_path and os.path.exists(file_path):
            os.remove(file_path)

        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
