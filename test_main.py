from urlshort import create_app

def test_shorten(client):
    # test to see if the word "submit" is on the homepage
    response = client.get('/')
    assert b'submit' in response.data 
