import pytest

@pytest.fixture
def setUp():
    print("Launch Browser")
    print("Login")
    print("browse products")
    
def testAddItemFromCart(setUp):
    print ("add item successful")

def testRemoveItemFromCart(setUp):
    print ("remove item successful")