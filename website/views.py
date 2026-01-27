from django.shortcuts import render
import smtplib


# Create your views here.
def index(request):
    return render(request, 'index.html')

def fillform(request):
    return render(request, 'form.html')

def sendMail(request):
    email = request.POST["email"]
    phone = request.POST["phone"]
    name = request.POST["name"]
    problem = request.POST["problem"]

    reciever = ["chirag178g@gmail.com"]
    sender = "chirag178g@gmail.com"
    subject = f"New Problem BL24 from {name}"    
    message = f"""Subject:{subject} \n


        PROBLEM : {problem} \n 
        Email : {email} \n 
        Phone : {phone} \n
        name : {name}.
    """

        # fetching data from password.txt and getting the password
    p = "mwoa nhbf xdkq zcjy"

    gmail_user = sender
    gamil_app_password = p
    sent_from = sender
    sent_to = reciever
    email_text = message

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gamil_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print("Email Sent!")
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
    return render(request, 'index.html')