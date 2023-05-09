from utils.html import *
from utils.translator import *


lang_list = ['en', 'ja']


content = [

    h3(t("Magic Mask", lang_list)) ,
    "<br>",
    h1(t("고도로 발전된 기술은 마법과 구별되지 않는다 - 클라크의 삼법칙", lang_list)),
    "<br>",
    "<br>",
    h2(t("Product launch soon.", lang_list)),
    "<br>",
    "<br>",
    "<br>",
    br(),
    br(),
    br(),
    br(),
    br(),
    p("사업자 등록 번호 : 000-00-00000   |   이메일 : example@company.com"),
    #a = t("사업자 등록번호") + " : 000-00-00000    |   " + t("이메일") + " : example@company.com"
    
    ]





def editor():
    return content