# genric view


from rest_framework import generics

from postings.models import BlogPost

from .serializer import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = BlogPostSerializer
    #permission_classes      = [IsOwnerOrReadOnly]
    #queryset                = BlogPost.objects.all(

    def get_queryset(self):
        return BlogPost.objects.all()
