import sys
import imaplib
import getpass
import email
import email.header
import datetime
import mailparser as mailparser
import time
import os
import datetime
from datetime import datetime,timedelta

def dt_parse(t):
   return (
       datetime.fromtimestamp(
           time.mktime(
               email.utils.parsedate(t)
           )
       )
   )

# folders are saved by the first 15 characters of email ID
EMAIL_ACCOUNT = "rpaexamplemail@gmail.com"
EMAIL_FOLDER = "INBOX"
PASSWORD = "password12345."

def return_emails_from_imap(email_account, password, email_folder, search_term="ALL", url='imap.gmail.com'):

    M = imaplib.IMAP4_SSL(url)

    try:
        rv, data = M.login(email_account, password)
    except imaplib.IMAP4.error:
        print "Login Failed. Check Credentials and imap url."
        return
    
    rv, data = M.select(email_folder)

    if rv != 'OK':
        print "Email folder not found."
        return
    
    response = []
    rv, data = M.search(None, search_term)

    if rv != 'OK':
        print "No unSeen Messages"
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", num
            #return

        msg = email.message_from_string(data[0][1])
        parsed_msg = mailparser.parse_from_string(msg.as_string())
        response.append(parsed_msg)
    M.logout()
    return response


def save_emails_to_cwd(list_of_mails):
    
    if not os.path.exists("pybotlib_emails"):
        os.mkdir("pybotlib_emails")

    for mail in list_of_mails:

        if type(mail) != mailparser.mailparser.MailParser:
            print "save_emails_to_cwd ony takes in a list of mailparser.MailParser objects"
            return
        
        header = mail.headers
        body = mail.body
        mail_date = dt_parse(mail.Date).strftime("%m-%d-%Y %H.%M.%S")
        
        folder_name = "pybotlib_emails\\%s" % (mail.headers["Subject"]+" "+mail_date)

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        f = open(folder_name +"\\header.txt", "w")
        f.write(str(header))
        f.close()

        f = open(folder_name + "\\body.txt", "w")
        f.write(body)
        f.close()

        for a in mail.attachments:
            print(a)
            with open(folder_name + "\%s" % a["filename"], "w" ) as f:
                f.write(a["payload"].decode(a["content_transfer_encoding"]))
                f.close()
        


mails_list = return_emails_from_imap(
    email_account=EMAIL_ACCOUNT,
    password=PASSWORD,
    email_folder=EMAIL_FOLDER,
    search_term="ALL",
    url='imap.gmail.com')
      
save_emails_to_cwd(
    list_of_mails=mails_list
    )
