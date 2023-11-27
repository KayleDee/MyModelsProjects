from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 254)
    phone = models.CharField(max_length = 10)
    is_favorite = models.BooleanField(True)

def create_contact(name, email, phone, is_favorite):
    creating_acc = Contact(name=name, email=email,phone=phone, is_favorite=is_favorite)
    creating_acc.save()
    return creating_acc

def all_contacts():
    return Contact.objects.all()


def find_contact_by_name(current_name):
    try:
        person = Contact.objects.get(name=current_name)
        return person
    except:
        return None
    
def favorite_contacts():
    favs = Contact.objects.filter(is_favorite=True)
    return favs

def update_contact_email(people, new_email):
    try:
        update = Contact.objects.get(name=people)
        update.email = new_email
        update.save()
        return update
    except:
        return None

def delete_contact(remove):
    try:
        deleting = Contact.objects.get(name=remove)
        deleting.delete()
        return deleting
    except:
        return None