#! /usr/bin/env python3

import  flickrapi
import yaml


api_key='blah'
api_secret='boom'

with open("./conf/flickrkeys.yaml", 'r') as stream:
    try:
        yamlDict = yaml.load(stream)
        #print(yaml.dump(yamlDict))
        api_key = yamlDict['api_key']
        api_secret = yamlDict['api_secret']
        print('Hey you!' + api_key + ' And you! ' + api_secret)

    except yaml.YAMLError as exc:
        print(exc)

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
#51434786@N06 is mine! Thanks to https://www.flickr.com/services/api/explore/?method=flickr.people.getInfo
sets   = flickr.photosets.getList(user_id='51434786@N06')
title  = sets['photosets']['photoset'][1]['title']['_content']

print('Second set title: %s' % title)
print(sets['photosets']['photoset'][1])

#TODO: Dump the data into json files
