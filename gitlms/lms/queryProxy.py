from django.core.cache import cache
from .models import Department
from django.contrib.auth.decorators import login_required

class DepartmentCacheProxy:
    def __init__(self, user):
        self.user = user
    
    @login_required
    def get_departments(self):
        # Check if departments are already cached
        departments_cache_key = 'all_departments'
        departments = cache.get(departments_cache_key)
        print(departments)
        if not departments:
            print("not cached yet")
            # If departments are not cached, fetch from DB and cache them
            departments = Department.objects.all().order_by('name')
            cache.set(departments_cache_key, departments, timeout=60*15)  # Cache for 15 minutes
            
        return departments
