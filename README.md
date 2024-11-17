This API is to be used in chatGPT to send automated emails

```
curl -X POST "https://timesheet-sender.onrender.com/send-email/" \
  -F "recipient=tejas.uk9664@gmail.com" \
  -F "subject=Test Email from FastAPI" \
  -F "body=This is a test email sent using FastAPI." \
  -F "file=@./public/Fieldglass_Time_Sheet.pdf"
```

```
curl -X POST "https://timesheet-sender.onrender.com/send-email/" \
-H "Content-Type: application/json" \
-d '{"recipient": "tejas.uk9664@gmail.com", "subject": "Test Email", "body": "This is the body of the email."}'
```
```
curl -X POST "https://timesheet-sender.onrender.com/send-email/" \
-H "Content-Type: multipart/form-data" \
-F "email={\"recipient\":\"recipient@example.com\",\"subject\":\"Test Email with Attachment\",\"body\":\"This is an email with an attachment.\"}" \
-F "file=@path/to/file.txt"
```

```
curl -X POST "https://timesheet-sender.onrender.com/send-email/" \
     -H "Content-Type: application/json" \
     -d '{"recipient":"tejas.uk9664@gmail.com","subject":"Test Subject","body":"Test Body"}'
```
