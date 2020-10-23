import smtplib

def main(emailfrom, emailto, msg):
    email_from = emailfrom
    email_to = emailto
    smtp = "smtp.gmail.com"

    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_from, open('senha.txt').read().strip())
    server.login(email_from, pa202001)
    msg = msg
    server.sendmail(email_from, email_to, msg)
    server.quit()