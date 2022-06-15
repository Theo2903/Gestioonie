from rest_framework import serializers, generics, permissions


class CustomListAPIView(generics.ListAPIView):

    __serializer_cache = {}

    model = None
    fields = None
    exclude = None
    depth = 2 # is ok in most commons case

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        if self.model not in self.__serializer_cache:
            DynamicSerializer = type(
                self.model.__name__ + 'SerializerList',
                (serializers.ModelSerializer,), #  avec les dépendeces DRF
                {
                    'Meta': type(
                        'Meta',
                        (),
                        {
                            'model': self.model,
                            'fields': self.fields,
                            'depth': self.depth,
                            'exclude': self.exclude,
                        }
                    )
                }
            )
            self.__serializer_cache[self.model] = DynamicSerializer
        return self.__serializer_cache[self.model]


class CustomListCreateAPIView(generics.ListCreateAPIView):

    __serializer_cache = {}

    model = None
    fields = None
    exclude = None
    depth = 2 # is ok in most commons case

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):

        REQUEST_METHOD = self.request.method
        MODEL_REQUEST_METHOD = self.model.__name__ + '_' + REQUEST_METHOD

        if REQUEST_METHOD == "POST":
            self.depth = 0

        if MODEL_REQUEST_METHOD not in self.__serializer_cache:
            DynamicSerializer = type(
                self.model.__name__ + 'SerializerListCreateAPIView' + REQUEST_METHOD,
                (serializers.ModelSerializer,), #  avec les dépendeces DRF
                {
                    'Meta': type(
                        'Meta',
                        (),
                        {
                            'model': self.model,
                            'fields': self.fields,
                            'depth': self.depth,
                            'exclude': self.exclude,
                        }
                    )
                }
            )
            self.__serializer_cache[MODEL_REQUEST_METHOD] = DynamicSerializer
        return self.__serializer_cache[MODEL_REQUEST_METHOD]


class CustomRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    __serializer_cache = {}

    model = None
    fields = None
    exclude = None
    depth = 2 # is ok in most commons case

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        if self.model not in self.__serializer_cache:
            DynamicSerializer = type(
                self.model.__name__ + 'SerializerRetrieveUpdateDestroy',
                (serializers.ModelSerializer,), #  avec les dépendeces DRF
                {
                    'Meta': type(
                        'Meta',
                        (),
                        {
                            'model': self.model,
                            'fields': self.fields,
                            'depth': self.depth,
                            'exclude': self.exclude,
                        }
                    )
                }
            )
            self.__serializer_cache[self.model] = DynamicSerializer
        return self.__serializer_cache[self.model]


class CustomPermission(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    authorized_groups = ['', ] # group defined in backend
    authorized_urls = ['', ]   # url websites that have permission to call API's
    
    # IF object have only one owner
    # get user profile that have right to change the object 
    def get_user_profile(self, obj):
        return obj.user # most common cases
        

    # IF object have multiple owners
    # get users profiles that have right to change the object
    def get_user_profile_list(self, obj):
        return []
        # exemple: return obj.exhibitor.exhibitor.user.all()

    def has_object_permission(self, request, view, obj):
        verbs = ['PUT', 'PATCH', 'POST', 'DELETE']

        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        else:
            if request.user.is_authenticated and request.method in verbs:
                user_profile_list = self.get_user_profile_list(obj)
                if user_profile_list:
                    return request.user.profile in user_profile_list
                else:
                    user_profile = self.get_user_profile(obj)
                    return request.user.profile == user_profile
            else:
                return False

    def has_permission(self, request, view):
        try:
            # Check if there is an authorized url
            for authorized_url in self.authorized_urls:
                if request.META['HTTP_ORIGIN'] == authorized_url:
                    return True
        except KeyError:
            pass

        # Check if user is NOT authenticated
        if not request.user.is_authenticated:
            return False

        # Check if user is admin
        if request.user.is_superuser:
            return True

        # Authorized groups able to perform SAFE_METHODS (GET, OPTIONS)
        if self.authorized_groups:
            for authorized_group in self.authorized_groups:
                if authorized_group in request.user.groups.values_list('name', flat=True) and request.method in permissions.SAFE_METHODS:
                    return True

        return False
