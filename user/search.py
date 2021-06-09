# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import Document, Keyword, Text, Integer, Date,Search
#
# from elasticsearch.helpers import bulk
# from elasticsearch import Elasticsearch
# from . import models
#
# connections.create_connection(hosts=['localhost'])
#
# class NavercafeIndex(Document):
#     user_index = Text()
#     user_id = Text()
#     pwd = Text()
#     user_type = Text()
#     user_name = Text()
#     auth_code = Text()
#     user_email = Text()
#     phone_number = Text()
#     birth_day = Text()
#     pwd_modified_at = Text()
#     created_at = Date()
#     modified_at = Date()
#
#     class Index:
#         name = 'user-index'
#
# def bulk_indexing():
#     NavercafeIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in models.User.objects.all().iterator()))
#
# def search(display):
#     s = Search().filter('match', display=display)
#     response = s.execute()
#     return response
