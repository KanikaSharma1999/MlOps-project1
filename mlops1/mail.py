import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("sender's email", "pass") 
# message to be sent 
message = "Hey Developer, Finally we got the model trained. "
# sending the mail 
s.sendmail("meetkanikasharma01011999@gmail.com", "meetkanikasharma01011999@gmail.com", message) 
# terminating the session 
s.quit()
