from rest_framework.throttling import UserRateThrottle

class WatchListCreateThrottle(UserRateThrottle):

    scope = "watch-create"

class WatchListThrottle(UserRateThrottle):

    scope = "watch-list"


