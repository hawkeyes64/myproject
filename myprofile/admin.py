from django.contrib import admin

from .models import ETab, AboutMe, WorkExperience, \
    CasualExperience, skill_list, Reference_LinkIcon, AboutMe_Link

# Register your models here.
admin.site.register(ETab)
admin.site.register(AboutMe)
admin.site.register(AboutMe_Link)
admin.site.register(Reference_LinkIcon)
admin.site.register(WorkExperience)
admin.site.register(CasualExperience)
admin.site.register(skill_list)
