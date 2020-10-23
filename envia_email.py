import smtplib

def main(msg, emailfrom, emailto):
    email_from = emailfrom
    email_to = emailto
    smtp = "smtp.gmail.com"

    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_from, open('senha.txt').read().strip())
    server.sendmail(email_from, email_to, msg)
    server.quit()

