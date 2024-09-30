from services.get_receptors_emails import get_receptors_emails
from use_cases.go_to_gmail import go_to_gmail
from use_cases.go_to_write import go_to_write
from use_cases.write_receptors_emails import write_receptors_emails
from use_cases.write_subject import write_subject
from use_cases.write_message import write_message
from use_cases.send_email import send_email

receptors = []

get_receptors_emails(receptors)

if not receptors:
    print("Nenhum email válido foi encontrado.")
else:
    subject = input('Digite o nome do assunto: ')
    message = input('Digite a sua mensagem: ')

    go_to_gmail()
    go_to_write()
    write_receptors_emails(receptors=receptors)

    write_subject(subject=subject)
    write_message(message=message)
    send_email()
    print("Emails e assunto escritos com sucesso!")
