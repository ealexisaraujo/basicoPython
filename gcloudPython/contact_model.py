from google.cloud import ndb


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()


client = ndb.Client()
