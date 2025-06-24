import requests


def test_send_csv_file():
    text = 'some, data, to, send\nanother, row, to, send\n'
    url = 'https://httpbin.org/post'
    files = {'file': ('report.csv', text)}
    response = requests.post(url, files=files)
    response_json = response.json()
    assert response_json['files']['file'] == text


def test_send_image():
    url = 'https://petstore.swagger.io/v2/pet/1/uploadImage'
    with open('../files/expected_image.png', 'rb') as fp:
        files = {'file': ('img.png', fp, 'image/png', {'Expires': '0'})}
        response = requests.post(url, files=files)

    assert response.status_code == requests.codes.ok
    assert 'File uploaded to' in response.text


def test_get_file():
    url = 'https://httpbin.org/image/png'
    response = requests.get(url)
    content = response.content
    assert response.status_code == 200

    with open('../files/expected_image.png', 'rb') as local_file:
        local_file_content = local_file.read()

    assert content == local_file_content, "Files are not identical"
