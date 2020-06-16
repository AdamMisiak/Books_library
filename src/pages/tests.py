from django.urls import reverse, resolve


def test_home_view_status_code(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
