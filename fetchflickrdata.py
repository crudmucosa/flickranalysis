#! /usr/bin/env python3

import  flickr_api


# TODO: Read from a yml file to get the keys
apiKey='blah'
apiSecret='boom'

flickr_api.set_keys(api_key = apiKey, api_secret = apiSecret)

username = 'crudmucosa'
user = flickr_api.Person.findByUserName(username)

print(user)
photos = user.getPublicPhotos()
print(photos)
