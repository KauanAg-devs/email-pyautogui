from services.validate_email import is_valid_email


def get_receptors_emails(receptors):
  while(True): 
    receptor = input('digite o email do recebidor: ')
    if(is_valid_email(receptor)): 
      receptors.append(receptor)
      stop = input('caso não queira adicionar mais recebidores, digite stop: ')
      if(stop == str.lower('stop')): break
    else: 
      print('email iválido')
