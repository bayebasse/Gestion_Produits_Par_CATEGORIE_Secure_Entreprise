import mysql.connector
connection=mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="GestionInventaire"
)


curseur=connection.cursor()

if connection.is_connected():
    print("OK MR")

import bcrypt
mot_de_passe_Baye_Bass="admin123"
mot_de_passe_maria="Maria123"
mot_de_passe_Ame="Ame123"

mot_de_passe_Baye_Bass_bytes=mot_de_passe_Baye_Bass.encode('utf-8')
hash_mot_pass_baye=bcrypt.hashpw(mot_de_passe_Baye_Bass_bytes,bcrypt.gensalt())

mot_de_passe_Maria_bytes=mot_de_passe_maria.encode('utf-8')
hash_mot_pass_Maria=bcrypt.hashpw(mot_de_passe_Maria_bytes,bcrypt.gensalt())


mot_de_passe_Ame_bytes=mot_de_passe_Ame.encode('utf-8')
hash_mot_pass_Amadou=bcrypt.hashpw(mot_de_passe_Ame_bytes,bcrypt.gensalt())

# Gestion Utilisateurs#
sql="insert into Utilisateurs(Mot_De_Passe,Prenom_Utilisateur,Nom_Utilisateur,Email) values(%s,%s,%s,%s)"
curseur.execute(sql,(hash_mot_pass_baye,"Baye Bass","Dieye","dieyebass11@gmail.com"))

sql="insert into Utilisateurs(Mot_De_Passe,Prenom_Utilisateur,Nom_Utilisateur,Email) values(%s,%s,%s,%s)"
curseur.execute(sql,(hash_mot_pass_Maria,"Mariama","Diallo","dbamariam13@gmail.com"))

sql="insert into Utilisateurs(Mot_De_Passe,Prenom_Utilisateur,Nom_Utilisateur,Email) values(%s,%s,%s,%s)"

curseur.execute(sql,(hash_mot_pass_Amadou,"Amadou","Ba","baamadou1@gmail.com"))
connection.commit()

def Se_Connecter():
    choix1=input("Connectez vous :" )
    match choix1:
        case "1":
            entree_email=input("Entrez votre email : " )
            entree_mot_passe=input("Entrez votre mot de passe :  ")
            sql="select Email from Utilisateurs where Prenom_Utilisateur=%s"
            curseur.execute(sql,("Baye Bass",))
            email_trouver=curseur.fetchone()[0]
            sql="select Mot_De_Passe from Utilisateurs where Prenom_Utilisateur=%s" 
            curseur.execute(sql,("Baye Bass",))
            mot_passe_trouver=curseur.fetchone()[0]
            if bcrypt.checkpw(entree_mot_passe.encode('utf-8'),mot_passe_trouver.encode('utf-8')) and entree_email==email_trouver:   
                print("Connexion réussie")
                
Se_Connecter()


from datetime import date
current_date=date.today()



def Afficher_Categories():
    sql="select Nom_Categorie from Categories"
    curseur.execute(sql)
    resultat=curseur.fetchall()
    print("Voici Les Catégories Disponibles")
    print(resultat)
    
def Ajouter_Produit():
    Nom_produit=input("Entrez le nom du Produit: ")
    print("          ")
    print("Voici les Categories Disponibles , Choississez 1 : ")
    print("          ")
    sql="select Nom_Categorie from Categories"
    curseur.execute(sql)
    resultat=curseur.fetchall()
    print(resultat)
    print("             ")
    choix_catalogue=input("Entrez votre Choix de CATALOGUE: " )
    if choix_catalogue=="Informatique":
        Informatique.append(Nom_produit)
        prix=int(input("Entrez le prix du Produit : " ))
        sql="""insert into Produits(Prix_Produit,ID_Categorie,Date_Mouvement) 
                values(%s,%s,%s)"""
        curseur.execute(sql,(prix,1,current_date))
        connection.commit()
        sql="select count(*) from Produits where ID_Categorie=%s"
        curseur.execute(sql,(1,))
        quantite=curseur.fetchone()[0]
        connection.commit()
        sql="update Historiques set Quantité=%s"
        curseur.execute(sql,(quantite,))
        connection.commit()
        sql="insert into Historiques(Date,ID_CATEGORIE,Quantité,Type) values(%s,%s,%s,%s)"
        curseur.execute(sql,(current_date,1,quantite,'Entrée'))
        connection.commit()
        
        
    elif choix_catalogue=="Papeterie":
        Papeterie.append(Nom_produit)
        prix=int(input("Entrez le prix du Produit :  " ))
        sql="""insert into Produits(Prix_Produit,ID_Categorie,Date_Mouvement) 
                values(%s,%s,%s)""" 
        curseur.execute(sql,(prix,1,current_date))
        connection.commit()
        sql="select count(*) from Produits where ID_Categorie=%s"
        curseur.execute(sql,(2,))
        quantite=curseur.fetchone()[0]
        connection.commit()
        sql="update Historiques set Quantité=%s"
        curseur.execute(sql,(quantite,))
        connection.commit()
        sql="insert into Historiques(Date,ID_CATEGORIE,Quantité,Type) values(%s,%s,%s,%s)"
        curseur.execute(sql,(current_date,2,quantite,'Entrée'))
        connection.commit()

                

        curseur.execute(sql,(prix,2,current_date))
        connection.commit()
    elif choix_catalogue=="Mobilier":
        Mobilier.append(Nom_produit)
        prix=int(input("Entrez le prix du Produit : " ))
        sql="""insert into Produits(Prix_Produit,ID_Categorie,Date_Mouvement) 
                values(%s,%s,%s)"""
        curseur.execute(sql,(prix,3,current_date))
        connection.commit()
        sql="select count(*) from Produits where ID_Categorie=%s"
        curseur.execute(sql,(3,))
        quantite=curseur.fetchone()[0]
        connection.commit()
        sql="update Historiques set Quantité=%s"
        curseur.execute(sql,(quantite,))
        connection.commit()
        sql="insert into Historiques(Date,ID_CATEGORIE,Quantité,Type) values(%s,%s,%s,%s)"
        curseur.execute(sql,(current_date,3,quantite,'Entrée'))
        connection.commit()
        



    


while True:
    print("****** MENU ********")
    print("1 . Voir les Categories " )
    print("2. Ajouter un Produit " )
    print("9. Quitter :  ") 
    choix=input("Entrez votre choix : " )
    match choix:
        case "1":
            Afficher_Categories()
        case "2":
           Ajouter_Produit()
        case "9":
            print("Tu as quitté LE PROGRAMME" )
            break
        
        




