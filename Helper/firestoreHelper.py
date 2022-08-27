
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseHelper:

    def __init__(self):

        self.cred = credentials.Certificate("Helper/python-web-flutter-app-firebase-adminsdk-fkvse-171c04c8fd.json")
        firebase_admin.initialize_app(self.cred)
        self.firestoreDb = firestore.client()


    def addData(self,name,mail,title,content):

        try:
            subcollection = datetime.datetime.now().strftime("%d %B %Y")


            infoContact = self.firestoreDb.collection(u'app').document('Contacts')

            id = self.getDataLength(infoContact=infoContact,subcollection=subcollection,mail=mail)


            infoContact.set(
                {str(subcollection):{ mail:{str(id+1):{"name": name, u'mail': mail, u'title': title, u'message': content,u"createdAt": firestore.firestore.SERVER_TIMESTAMP}}}}, merge=True)

            return True
        except Exception as e:
            print("Veri Eklenirken hata olustu "+ str(e))
            return False


    def getDataLength(self,infoContact,subcollection,mail):


            doc_ref = infoContact

            doc = doc_ref.get()

            if doc.exists:
                try:
                    length_mail_messages = len(doc.to_dict()[subcollection][mail])
                    return length_mail_messages
                except:

                    return 0

            else:
                return 0






    def showData(self):

        try:

            snapshots = list(self.firestoreDb.collection(u'testCollection').get())
            for snap in snapshots:
                print(snap.to_dict())

            return True
        except Exception as e:
            print("Veri gösterilirken hata olustu"+str(e))
            return True