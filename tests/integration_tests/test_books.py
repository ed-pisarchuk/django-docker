import pytest
import json
from rest_framework import status


@pytest.mark.django_db
def test_get_books__positive(client):
    response = client.get("/store/books/")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_book__positive(client, book):
    response = client.get(f"/store/books/{book.pk}/")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_book__positive(client, publisher, author):
    book_name = "Евгений Онегин"
    data = json.dumps(
        {"name": book_name, "publisher": publisher.pk, "authors": [author.pk]}
    )
    response = client.post("/store/books/", data, content_type="application/json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == book_name
    assert response.data["publisher"] == publisher.pk


@pytest.mark.django_db
def test_put_book__positive(client, book, author):
    book_name = "Новая книга"
    data = json.dumps(
        {
            "id": book.pk,
            "name": book_name,
            "publisher": book.publisher.pk,
            "authors": [author.pk],
        }
    )
    response = client.put(
        "/store/books/" + str(book.pk) + "/", data, content_type="application/json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == book_name


@pytest.mark.django_db
def test_patch_book__positive(client, book):
    book_name = "Другая новая книга"
    data = json.dumps({"name": book_name})
    response = client.patch(
        f"/store/books/{str(book.pk)}/", data, content_type="application/json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == book_name


@pytest.mark.django_db
def test_delete_book__positive(client, book):
    response = client.delete(f"/store/books/{book.pk}/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
