import smtplib
import ssl
from email.message import EmailMessage

print("$$$$$$$$\                         $$\ $$\        $$$$$$\    $$\     $$\                         $$\ ")                          
print("$$  _____|                        \__|$$ |      $$  __$$\   $$ |    $$ |                        $$ | ")                          
print("$$ |      $$$$$$\$$$$\   $$$$$$\  $$\ $$ |      $$ /  $$ |$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\ ")  
print("$$$$$\    $$  _$$  _$$\  \____$$\ $$ |$$ |      $$$$$$$$ |\_$$  _|\_$$  _|   \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ ")
print("$$  __|   $$ / $$ / $$ | $$$$$$$ |$$ |$$ |      $$  __$$ |  $$ |    $$ |     $$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|")
print("$$ |      $$ | $$ | $$ |$$  __$$ |$$ |$$ |      $$ |  $$ |  $$ |$$\ $$ |$$\ $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |")     
print("$$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |$$ |$$ |      $$ |  $$ |  \$$$$  |\$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |")      
print("\________|\__| \__| \__| \_______|\__|\__|      \__|  \__|   \____/  \____/  \_______| \_______|\__|  \__| \_______|\__|")
print("                                                                                                             Made by Treveen")
print("")
print("")
print("Welcome to Email Attacker : send scary emails!!!! ")
print("create a phishing link with zphisher to use this tool")

sender_email = input("Enter your Email Address: ")
sender_email_password = input("Enter your password: ")
receiver_email = input("Enter the email of the receiver: ")
subject = input("Enter your subject: ")
body = input("Enter the body of the email: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()
print("Sending Email to: ",receiver_email)

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email, sender_email_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Give me a second")
print("ALL RIGHTS RESERVED BY TREVEEN")
print("Success")
