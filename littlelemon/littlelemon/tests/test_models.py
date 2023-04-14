from django.test import TestCase
from restaurant.models import MenuItem

#TestCase class
class MenuItemTest(TestCase):

  # it is important that the test starts with test_
  def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    print(item)
    self.assertEqual(str(item), "IceCream : 80")