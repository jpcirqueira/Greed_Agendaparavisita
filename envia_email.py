import smtplib

def main(emailfrom, confirmado):
    print("cristo", confirmado)
    msg = """ sr.{} sua visita foi confirmada para as: {}"""
    for aux in confirmado:
        nome= aux
        email_to= confirmado[aux]['email']
        hinicio= confirmado[aux]['hInicioString']
        minicio= confirmado[aux]['mInicioString']
        hora = hinicio + ':' + minicio
        
        msg= msg.format(nome,hora)
        email_from = emailfrom
        smtp = "smtp.gmail.com"

        server = smtplib.SMTP(smtp, 587)
        server.starttls()
        server.login(email_from, open('senha.txt').read().strip())
        server.sendmail(email_from, email_to, msg)
        server.quit()

