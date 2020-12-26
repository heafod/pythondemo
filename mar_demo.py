import sys
from datetime import date
from marshmallow import Schema, fields, pprint, ValidationError
from packaging import version

v1 = version.Version("v1.0.0.1")
v2 = version.Version("v2.0.0")
print(v1 < v2)

# class ArtistSchema(Schema):
#     name = fields.Str()
#     age = fields.Int(required=True)
#
#
# class AlbumSchema(Schema):
#     title = fields.Str()
#     # release_date = fields.Date()
#     artist = fields.Nested(ArtistSchema())
#
#
# bowie = dict(name='David Bowie')
# # try:
# #     bowie = ArtistSchema().load({'name': 'David Bowie'})
# # except ValidationError as err:
# #     pprint(err.messages)
# #     sys.exit(1)
# #
# # print(type(bowie))
#
# album = dict(artist=bowie, title='Hunky Dory', release_date="2010-10-10 15:23:32")
#
# print(album)
# try:
#     bowie = AlbumSchema().load(album)
# except ValidationError as err:
#     pprint(err.messages)
#     sys.exit(1)
#
# schema = AlbumSchema()
# result = schema.dump(album)
# pprint(result, indent=2)
