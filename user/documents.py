# from elasticsearch_dsl.connections import connections
# from django_elasticsearch_dsl import Document, Index
# from . import models
#
# connections.create_connection()
#
# user = Index('users')
#
# # reference elasticsearch doc for default settings here
# user.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )
#
# @user.doc_type
# class BookDocument(Document):
#
#     class Django:
#         model = models.User
#         fields = ['user_id', 'user_name', 'created_at']