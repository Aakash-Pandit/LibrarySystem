from rest_framework import routers
from library.SerializerViews import AuthorInfoView, BookInfoView, StudentInfoView


router = routers.DefaultRouter()
router.register(r'author', AuthorInfoView)
router.register(r'book', BookInfoView)
router.register(r'student', StudentInfoView)
