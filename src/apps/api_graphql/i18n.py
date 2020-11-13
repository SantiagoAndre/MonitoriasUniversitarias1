from graphene import String,Boolean
from graphene import ObjectType,Mutation,Field
from django.utils import translation
from core.settings import LANGUAGES

# lANGUAGE DICT AND CODE LIST
DICT_LANGUAGES =  [{"code": code, "name":name} for (code,name) in LANGUAGES]
CODES_LANGUAGES =  [code for (code,_) in LANGUAGES]

# get Current Language
def current_language():
    code = translation.get_language()
    return [lang for lang in DICT_LANGUAGES if lang["code"]==code][0]



class LanguageApplicationObject(ObjectType):
    code =String()
    name =String()


class SelectLanguage(Mutation):

    success = Field(Boolean)

    class Arguments:
        code = String(required=True)
    def mutate(self, info, code):
        success =  code in CODES_LANGUAGES 
        if success:
            info.context.set_language_cookie= code
        return SelectLanguage(success=success)

