from django.http import JsonResponse

class CheckAge:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated and hasattr(user, 'age') and user.age < 18:
            return JsonResponse(
                {"message": "your age is under 18, you can't post"},
                status=403
            )

        response = self.get_response(request)
        return response
