import os
from rest_framework import status, generics
from rest_framework.response import Response

from . import serializers, models
import jwt


class SignView(generics.CreateAPIView):
    model = models.User
    serializer_class = serializers.SignupSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
        else:
            print(serializer.errors)

        return Response({
            'success': 1,
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)



class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer

    def get_queryset(self):
        queryset = models.User.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id", None)
        password = request.data.get("password", None)

        if any(element is None for element in [user_id, password]):
            raise exc.ParseError("필수 파라미터값이 없습니다.")

        try:
            obj = self.get_queryset().get(user_id=user_id)
        except:
            raise exc.NotAuthenticated('존재하지 않는 ID 입니다.')

        if not check_password(password, obj.password):
            raise exc.NotAuthenticated("패스워드가 일치하지 않습니다.")

        payload = {
            "iss": "find_city",
            "user_index": obj.user_index,
            "exp": datetime.now() + timedelta(seconds=60 * 60 * 24),
        }

        jwt_encode = jwt.encode(payload=payload, key=os.environ['SECRET_KEY'], algorithm="HS256")
        token = jwt_encode.decode("utf-8")

        if token:
            obj.is_active = True
            obj.save()

        return Response(
            {
                "success": 1,
                "results": {
                    "token": token,
                    "expire_time": datetime.now() + timedelta(seconds=60 * 60 * 24),
                    "user_id": obj.user_id
                },
            },
            status=status.HTTP_200_OK
        )
