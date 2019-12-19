
'''
CRUDL
'''


# class StatusApiView(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.ListAPIView):

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     passed_id = None

#     def get_queryset(self):
#         request = self.request
#         queryset = StatusModel.objects.all()
#         query = request.GET.get("q")
#         if query is not None:
#             queryset = queryset.filter(content__icontains=query)
#         return queryset

#     # This method is for "?id=1,2,2"
#     def get_object(self):
#         request = self.request
#         queryset = self.get_queryset()
#         passed_id = request.GET.get("id") or self.passed_id
#         obj = None
#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj

#     # Overriding the get_object method
#     def get(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         body_ = request.body
#         json_data = {}

#         if is_json(body_):
#             json_data = json.loads(body_)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         if passed_id is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         body_ = request.body
#         json_data = {}

#         if is_json(body_):
#             json_data = json.loads(body_)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         body_ = request.body
#         json_data = {}

#         if is_json(body_):
#             json_data = json.loads(body_)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         return self.update(request, *args, **kwargs)

#     def perform_destroy(self, instance):
#         if instance is not None:
#             instance.delete()
#         return None

#     def delete(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         body_ = request.body
#         json_data = {}

#         if is_json(body_):
#             json_data = json.loads(body_)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id

#         return self.destroy(request, *args, **kwargs)


'''
Individual Implementation
'''
# class StatusListSearchApiView(APIView):

#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, *args, **kwargs):
#         qs = StatusModel.objects.all()
#         serialized = StatusSerializer(qs)
#         return Response(serialized.data)

#     def post(self, request, *args, **kwargs):
#         qs = StatusModel.objects.all()
#         serialized = StatusSerializer(qs)
#         return Response(serialized.data)


# # List and Search View
# class StatusApiView(generics.ListAPIView):

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         queryset = StatusModel.objects.all()
#         query = self.request.GET.get("q")
#         if query is not None:
#             queryset = queryset.filter(content__icontains=query)
#         return queryset


# # Create View
# class StatusApiCreateView(generics.CreateAPIView):

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = StatusModel.objects.all()


# # Detail View
# class StatusApiDetailView(generics.RetrieveAPIView):

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = StatusModel.objects.all()
#     # lookup_field = "id" Custom replacement of pk and can also be used in case of "slug"

#     # def get_object(self):
#     #     kwargs = self.kwargs
#     #     id_ = kwargs.get("id")
#     #     return self.queryset.get(id=id_)


# class StatusApiUpdateView(generics.UpdateAPIView):

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = StatusModel.objects.all()


# class StatusApiDeleteView(generics.DestroyAPIView):

#     authentication_classes = []
#     permission_classes = []
#     serializer_class = StatusSerializer
#     queryset = StatusModel.objects.all()
