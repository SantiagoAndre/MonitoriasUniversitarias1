from django.utils.translation import gettext_lazy as _
class NameAlreadyUsedException(Exception):
    pass
class ParentSubjectNotFoundException(Exception):
    pass
'''    
class ParentLearningLineNotFoundException(Exception):
    pass
'''    
class SubjectCircularRealtionException(Exception):
    pass
class MaxDeepSubjectException(Exception):
    pass
class ValidationError(Exception):
    pass
# validators 

