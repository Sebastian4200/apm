from django.shortcuts import render

# Create your views here.
def face_to_face_classes(request):
    return render(request, 'facetoface/face_to_face.html')
