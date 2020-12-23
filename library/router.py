from rest_framework import routers
from library.serializerViews import (AuthorInfoView, BookInfoView, StudentInfoView,
                                    BookIssuedInfoView, LibraryInfoView, CollegeInfoView,
                                    UniversityInfoView)


router = routers.DefaultRouter()
router.register(r'author', AuthorInfoView, basename='Author')
router.register(r'book', BookInfoView, basename='Book')
router.register(r'student', StudentInfoView, basename='studnet')
router.register(r'book_issued', BookIssuedInfoView, basename='book_issued')
router.register(r'library', LibraryInfoView, basename="library")
router.register(r'college', CollegeInfoView, basename='college')
router.register(r'university', UniversityInfoView, basename='university')

