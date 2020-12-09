import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
#active this two option when you send email from live.like heroku/pythonanywhere
https://accounts.google.com/b/0/DisplayUnlockCaptcha	#this option will off if email sending is off for few hours/days.so you have to active this option again and again
https://myaccount.google.com/u/2/lesssecureapps
"""
MY_ADDRESS = 'email(from which email you want to send email to all others email'
PASSWORD = 'password of that email'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    #https://www.tutorialspoint.com/python/python_sending_email.htm
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
'''
def get_contacts(filename):
  names = []
  emails = []
  with open(filename, mode='r', encoding='utf-8') as contacts_file:
    for a_contact in contacts_file:
      names.append(a_contact.split()[0])
      emails.append(a_contact.split()[1])
    return names, emails

from string import Template


#follow this link for more about template string: https://docs.python.org/3.5/library/string.html#template-strings
def read_template(filename):
  with open(filename, 'r', encoding='utf-8') as template_file:
    template_file_content = template_file.read()
  return Template(template_file_content)

#smtplib protocol: https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol

import smtplib
# set up the SMTP server
MY_ADDRESS = 'coq1431@gmail.com'
PASSWORD = '1milon$noor1'
#s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)


names, emails = get_contacts('mycontacts.txt') # read contacts
message_template = read_template('message.txt')

# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For each contact, send the email:
for name, email in zip(names, emails):
  msg = MIMEMultipart()       # create a message

  # add in the actual person name to the message template
  message = message_template.substitute(PERSON_NAME=name.title()) #https://docs.python.org/3.5/library/string.html#template-strings

  # print message body for our sake
  print(message)

  # set parameters of the message
  msg['From']=MY_ADDRESS
  msg['To']=email
  msg['Subject']="This is TEST"

  # add message body
  msg.attach(MIMEText(message, 'plain')) #https://docs.python.org/3/library/email.html

  # send the message via the server set up earlier.
  s.send_message(msg)
  print("SENT EMAIL TO ", name)
  del msg
'''
