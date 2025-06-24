from helpers.pet_service import PetService
from models.data import Order


def test_get_pet():
    assert PetService().get_pet()[0]['id'] == 1010
    assert PetService().get_pet()[0]['id'] == 1010


def test_get_store_inventory():
    response = PetService().get_store_inventory()
    assert response['3000'] == 1
    assert response['5000'] == 1
    assert response['pending'] == 39


def test_post_order():
    body = Order(id_=1234567, petId=1, quantity=0, shipDate='2024-02-17T09:42:10.119Z', status='placed', complete=True)

    response = PetService().post_order(body.model_dump())

    assert response.status == body.status
    assert response.complete == body.complete
    assert body == response
