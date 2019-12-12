import json
from django.views import View
from django.http import JsonResponse

from .models import Comments

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        Comments(
            user = data['user'],
            comment = data['comment'],
        ).save()

        return JsonResponse({"message":"SUCCESS"},status = 200 )

    def get(self, request):

        data = list(Comments.objects.values())
        print(data)
        return JsonResponse({"comments":data}, status = 200)

