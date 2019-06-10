from rest_framework.views import APIView
from rest_framework.response import Response
from .models import bookde
class checker(APIView):
    def get(self,request):
        if 'id' in request.GET:
            data=bookde.objects.filter(id=request.GET['id']).all().values()
        elif 'name' in request.GET:
            data=bookde.objects.filter(name__contains=request.GET['name']).values()
        else:
            data=bookde.objects.all().values()
        return Response({"data":data})
    def put(self,request,post_id):
        bookde.objects.filter(id=post_id).update(**request.data)
        return Response({"data":"done"})
    def delete(self,request,post_id)
    def post(self,request):
        bookde.objects.create(**request.data)
        return Response({"data":"done"})
