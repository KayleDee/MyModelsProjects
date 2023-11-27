from django.test import TestCase
from app import models
# Create your tests here.
class TestBuddyList(TestCase):
    def test_adding_buddies(self):
        bl = models.adding_buddies(
            "Jerry",
            "1234567890",
            True
        )

        self.assertEqual(bl.id, 1)
        self.assertEqual(bl.buddy, "Jerry")
        self.assertEqual(bl.num, "1234567890")
        self.assertTrue(bl.pin)

    def test_all_buddies(self):
        buddies_data = [
            {
                "buddy": "Leon",
                "num": "08-435-264",
                "pin": True,
            },
            {
                "buddy": "Jill",
                "num": "13-124-153",
                "pin": False,
            },
            {
                "buddy": "Boy",
                "num": "12-113-114",
                "pin": True,
            },
        ]

        for buddy_data in buddies_data:
            models.adding_buddies(
                buddy_data["buddy"],
                buddy_data["num"],
                buddy_data["pin"],
            )

        buddies = models.all_buddies()

        self.assertEqual(len(buddies), len(buddies_data))

        buddies_data = sorted(buddies_data, key=lambda c: c["buddy"])
        buddies = sorted(buddies, key=lambda c: c.buddy)

        for data, buddy in zip(buddies_data, buddies):
            self.assertEqual(data["buddy"], buddy.buddy)
            self.assertEqual(data["num"], buddy.num)
            self.assertEqual(data["pin"], buddy.pin)

    def test_search_by_buddy(self):
        buddies_data = [
            {
                "buddy": "Leon",
                "num": "08-435-264",
                "pin": True,
            },
            {
                "buddy": "Jill",
                "num": "13-124-153",
                "pin": False,
            },
            {
                "buddy": "Boy",
                "num": "12-113-114",
                "pin": True,
            },
        ]

        for buddy_data in buddies_data:
            models.adding_buddies(
                buddy_data["buddy"],
                buddy_data["num"],
                buddy_data["pin"],
            )


        self.assertIsNone(models.find_buddy_by_buddy("aousnth"))

        buddy = models.find_buddy_by_buddy("Boy")

        self.assertIsNotNone(buddy)
        self.assertEqual(buddy.num, "12-113-114")

    def test_pin(self):
        buddies_data = [
            {
                "buddy": "Leon",
                "num": "08-435-264",
                "pin": True,
            },
            {
                "buddy": "Jill",
                "num": "13-124-153",
                "pin": False,
            },
            {
                "buddy": "Boy",
                "num": "12-113-114",
                "pin": True,
            },
        ]

        for buddy_data in buddies_data:
            models.adding_buddies(
                buddy_data["buddy"],
                buddy_data["num"],
                buddy_data["pin"],
            )


        self.assertEqual(len(models.view_pin_buddy()), 2)

    def test_update_a_buddy(self):
        buddies_data = [
           {
                "buddy": "Leon",
                "num": "08-435-264",
                "pin": True,
            },
            {
                "buddy": "Jill",
                "num": "13-124-153",
                "pin": False,
            },
            {
                "buddy": "Boy",
                "num": "12-113-114",
                "pin": True,
            },
        ]

        for buddy_data in buddies_data:
            models.adding_buddies(
                buddy_data["buddy"],
                buddy_data["num"],
                buddy_data["pin"],
            )


        models.update_a_buddy("Jill", "07-707-770")

        self.assertEqual(
            models.find_buddy_by_buddy("Jill").num, "07-707-770"
        )

    def test_eliminate_a_buddy(self):
        buddies_data = [
            {
                "buddy": "Leon",
                "num": "08-435-264",
                "pin": True,
            },
            {
                "buddy": "Jill",
                "num": "13-124-153",
                "pin": False,
            },
            {
                "buddy": "Boy",
                "num": "12-113-114",
                "pin": True,
            },
        ]

        for buddy_data in buddies_data:
            models.adding_buddies(
                buddy_data["buddy"],
                buddy_data["num"],
                buddy_data["pin"],
            )


        models.eliminate_a_buddy("Jill")

        self.assertEqual(len(models.all_buddies()), 2)