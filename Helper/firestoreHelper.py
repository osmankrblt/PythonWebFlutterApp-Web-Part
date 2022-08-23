
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
            subcollection = datetime.datetime.now().strftime("%d%B%Y")
            #subcollection = datetime.datetime.now().strftime("%x")



            infoContact = self.firestoreDb.collection(u'app').document('Contacts').collection(subcollection).document(mail)

            id = self.getDataLength(infoContact=infoContact) + 1

            infoContact.set({"contacts":{str(id):{"name":name,u'mail':mail,u'title': title ,u'message':content,u"createdAt":firestore.firestore.SERVER_TIMESTAMP}}},merge=True)
            return True
        except Exception as e:
            print("Veri Eklenirken hata olustu "+ str(e) )
            return False

    def getDataLength(self,infoContact):

        doc_ref = infoContact

        doc = doc_ref.get()

        if doc.exists:
            return len(doc.to_dict()["contacts"])
        else:
            return 0





    def showData(self):

        try:

            snapshots = list(self.firestoreDb.collection(u'testCollection').get())
            for snap in snapshots:
                print(snap.to_dict())

            return True
        except Exception as e:
            print("Veri gösterilirken hata olustu")
            return True