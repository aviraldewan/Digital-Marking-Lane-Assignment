import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Likes, Dislikes

# Home Page displaying like and dislike count
def index(request):

    # Get number of likes and dislikes
    likes = Likes.objects.get()
    dislikes = Dislikes.objects.get()

    return render(request, "Like_Dislike_Count/index.html", {
        "likes": likes.likes,
        "dislikes": dislikes.dislikes
    })

# API to get/update number of likes/dislikes
def get_count(request, count):

    if request.method == "GET":

        if count == "likes":
            # store number of likes
            obj = Likes.objects.get()
            obj = obj.likes
        elif count == "dislikes":
            # store number of dislikes
            obj = Dislikes.objects.get()
            obj = obj.dislikes
        else:
            # Invalid Request(URl)
            return JsonResponse({"error": "Invalid URL"}, status=400)

        # Send number of likes/dislikes
        return JsonResponse(obj, safe=False)
    else:

        # 'data' carries the payload sent by index.js file after like/dislike button is clicked
        data = json.loads(request.body)

        if count == "likes":
            # Update likes and save in database
            likes = Likes.objects.get()
            likes.likes = data.get("likes")
            likes.save()
        elif count == "dislikes":
            # Update dislikes and save in database
            dislikes = Dislikes.objects.get()
            dislikes.dislikes = data.get("dislikes")
            dislikes.save()

        # return success message
        return JsonResponse({"Success": "Value Updated"}, status=200)
