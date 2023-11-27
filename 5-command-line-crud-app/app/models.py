from django.db import models

# Create your models here.
class BuddyList(models.Model):
    buddy = models.TextField()
    num = models.TextField()
    pin = models.BooleanField(True)

def adding_buddies(person, number, is_pin):
    add_buddy = BuddyList(buddy=person, num=number, pin=is_pin)
    add_buddy.save()
    return add_buddy

def find_buddy_by_buddy(current_buddy):
    try:
        bud = BuddyList.objects.get(buddy=current_buddy)
        return bud
    except:
        return None
def all_buddies():
    return BuddyList.objects.all()

def view_pin_buddy():
    pinned = BuddyList.objects.filter(pin=True)
    return pinned

def update_a_buddy(person, phone_num):
    updating = BuddyList.objects.get(buddy=person)
    updating.num = phone_num
    updating.save()
    return updating

def eliminate_a_buddy(elim):
    eliminating = BuddyList.objects.get(buddy=elim)
    eliminating.delete()
    return eliminating 


# (Create) create an arbitrary amount of items for your application to manage.
# (Read) view all of the items at once.
# (Read) search for items that satisfy some filter.
# (Update) update individual items.
# (Delete) delete individual items.