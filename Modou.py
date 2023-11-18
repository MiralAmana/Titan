password="cisco"
email="admin@gmail.com"
user_email=input("Entrer votre email")
user_password=input("Saisissez votre mot de passe")
if(user_email==email and user_password==password):
    print("Connexion réussie")
else:
    print("Email ou mot de passe incorrect")
        