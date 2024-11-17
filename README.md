This API is to be used in chatGPT to send automated emails

```
curl -X POST "https://timesheet-sender.onrender.com/send-email/" \
  -F "recipient=tejas.uk9664@gmail.com" \
  -F "subject=Test Email from FastAPI" \
  -F "body=This is a test email sent using FastAPI." \
  -F "file=@./public/Fieldglass_Time_Sheet.pdf"
```
