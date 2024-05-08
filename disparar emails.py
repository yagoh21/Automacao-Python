import win32com.client as win32

#integração de outlook
outlook = win32.Dispatch('outlook.application')

#criar e-mail
email = outlook.CreateItem(0)

email.to ="stephanie.fernandes@maminfo.com.br"
email.Subject ="Liberação de Acesso"
email.HTMLBody = """

<p>ola, segue liberação de acesso do meu carro</p> 

<p>placa EAE-9195</p>
<p>celta vermelho 2 portas</p>
<p>Yago Henrique Firmino Da Silva </p>
<p>RG : 50.242.123-x</p>

"""

email.Send()
print("email enviado")