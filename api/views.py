from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class GetHomeworkProgress(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        serializer = [
            {
                "subject": "Biology",
                "percentage": 90,
                "date": "September, 7 Monday"
            },
            {
                "subject": "Geography",
                "percentage": 50,
                "date": "May, 10 Thursday"
            },
            {
                "subject": "Art and Crafts",
                "percentage": 65,
                "date": "June, 29 Friday"
            },
            {
                "subject": "History",
                "percentage": 80,
                "date": "December, 13 Monday"
            },
            {
                "subject": "Science",
                "percentage": 70,
                "date": "July, 30 Saturday"
            },
        ]
        return Response({"success":"Successful","data": serializer})


class GetUpcomingLessonsProgress(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        serializer = [
            {
                "subject": "Tutorial Algebra",
                "time": "4:00 PM",
                "date": "Sept, 7",
                "author": "Pierre Hackett",
                "avatar": "https://www.pngarts.com/files/5/Cartoon-Avatar-Transparent-Image.png"
            },
            {
                "subject": "School Homework",
                "time": "1:00 PM",
                "date": "Sept, 15",
                "author": "Kiersten Lange",
                "avatar": "https://cdn.truelancer.com/upload-full/701651-vector-cartoon-portrait-avatar-illustration-fanart.jpg"
            },
            {
                "subject": "Franch Language",
                "time": "12:00 AM",
                "date": "Oct, 2",
                "author": "Global History/ Analysis",
                "avatar": "https://cdn.dribbble.com/users/2364329/screenshots/10481283/media/f013d5235bfcf1753d56cad154f11a67.jpg"
            },
            {
                "subject": "Tutorial Algebra",
                "time": "9:00 AM",
                "date": "Nov, 7",
                "author": "Sam Anderson",
                "avatar": "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/83221961/original/425127947f0688643bcefba40b83c767b13e2a6a/illustrate-your-cartoon-avatar.jpg"
            },
        ]
        return Response({"success":"Successful","data": serializer})


class GetTasksProgress(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        serializer = [
            {
                "subject": "Tutorial Algebra",
                "time": "4:00 PM",
                "date": "Sept 7, 2021",
                "tag": "Algebra",
                "author": "Pierre Hackett",
                "avatar": "https://www.pngarts.com/files/5/Cartoon-Avatar-Transparent-Image.png"
            },
            {
                "subject": "History",
                "time": "6:00 AM",
                "tag": "history",
                "date": "Sept 7, 2021",
                "author": "Kiersten Lange",
                "avatar": "https://cdn.dribbble.com/users/2364329/screenshots/10481283/media/f013d5235bfcf1753d56cad154f11a67.jpg"
            },
            {
                "subject": "Chemistry",
                "time": "12:00 AM",
                "tag": "Science",
                "date": "Sept 7, 2021",
                "author": "Sam Anderson",
                "avatar": "https://cdn.truelancer.com/upload-full/701651-vector-cartoon-portrait-avatar-illustration-fanart.jpg"
            },
            {
                "subject": "Homework",
                "time": "5:00 PM",
                "tag": "Maths",
                "date": "Sept 7, 2021",
                "author": "Pierre Hackett",
                "avatar": "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/83221961/original/425127947f0688643bcefba40b83c767b13e2a6a/illustrate-your-cartoon-avatar.jpg"
            },
        ]
        return Response({"success":"Successful","data": serializer})


class GetLeaderBoard(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        serializer = [
            {
                "rank": 1,
                "points": 2334,
                "bestscore": 98,
                "user": "Pattrick Devano",
                "avatar": "https://st2.depositphotos.com/2703645/11099/v/950/depositphotos_110991592-stock-illustration-female-cartoon-avatar-icon.jpg"
            },
            {
                "rank": 2,
                "points": 2314,
                "bestscore": 95,
                "user": "Jennifer Hudson",
                "avatar": "https://cdn.truelancer.com/upload-full/701651-vector-cartoon-portrait-avatar-illustration-fanart.jpg"
            },
            {
                "rank": 3,
                "points": 2114,
                "bestscore": 90,
                "user": "Stevia Rownders",
                "avatar": "https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/83221961/original/425127947f0688643bcefba40b83c767b13e2a6a/illustrate-your-cartoon-avatar.jpg"
            },
            {
                "rank": 4,
                "points": 1823,
                "bestscore": 89,
                "user": "Sam Anderson",
                "avatar": "https://cdn.dribbble.com/users/2364329/screenshots/10481283/media/f013d5235bfcf1753d56cad154f11a67.jpg"
            },
        ]
        return Response({"success":"Successful","data": serializer})


class GetMyCoursesBoard(APIView):
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        serializer = [
            {
                "subject": "Tutorial History",
                "level": "Begginers",
                "tasks": "6/30",
                "percentage": 20,
                "author": "Pierre Hackett",
                "avatar": "https://www.pngarts.com/files/5/Cartoon-Avatar-Transparent-Image.png",
                "subjectavatar": "https://image.shutterstock.com/image-vector/illustration-featuring-huge-yellowed-history-600w-683203747.jpg"
            },
            {
                "subject": "Tutorial Algebra",
                "level": "Advance",
                "tasks": "27/30",
                "percentage": 90,
                "author": "Pierre Hackett",
                "avatar": "https://cdn.dribbble.com/users/2364329/screenshots/10481283/media/f013d5235bfcf1753d56cad154f11a67.jpg",
                "subjectavatar": "https://images-eu.ssl-images-amazon.com/images/I/51SZFsjL9UL._SX198_BO1,204,203,200_QL40_FMwebp_.jpg"
            },
            {
                "subject": "Tutorial France",
                "level": "Begginers",
                "tasks": "14/20",
                "percentage": 70,
                "author": "Pierre Hackett",
                "avatar": "https://cdn.truelancer.com/upload-full/701651-vector-cartoon-portrait-avatar-illustration-fanart.jpg",
                "subjectavatar": "https://thumbs.dreamstime.com/z/cartoon-paint-brush-icon-clipart-image-isolated-white-background-cartoon-paint-brush-icon-128950020.jpg"
            }
        ]
        return Response({"success":"Successful","data": serializer})