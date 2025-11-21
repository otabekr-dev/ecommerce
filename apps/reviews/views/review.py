import json

from django.views import View
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from ..models import Review

class ReviewListView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        reviews = [r.to_dict() for r in Review.objects.all()]

        return JsonResponse({'reviews':reviews})
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body) if request.body else {}

        comment = data.get("comment")
        if not comment:
            return JsonResponse({"comment":"Required"}, status=400)
        
        review = Review.objects.create(
            product_id = data["product"],
            user_id = data["user"],
            rate = data["rate"],
            comment = data["comment"]
        )

        review.save()

        return JsonResponse(review.to_dict(), status=200)

class DetailedReviewList(View):

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        review = get_object_or_404(Review, pk=pk)

        return JsonResponse(review.to_dict(),status=200)


    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        review = get_object_or_404(Review, pk=pk)
        data = json.loads(request.body)

        comment = data.get("comment")
        if comment:
            review.comment = comment

        rate = data.get("rate")
        if rate:
            review.rate = rate

        review.save()        

        return JsonResponse(review.to_dict(), status=204)
    
    def delete(self, request: HttpRequest , pk: int) -> JsonResponse:
        review = get_object_or_404(Review, pk=pk)
        
        review.delete()

        return JsonResponse({"review":"Successfully deleted"})