from utils.html import *

import googletrans


trans = googletrans.Translator()


html_start = '''<!DOCTYPE html>\n<html>\n<head>\n'''
html_end = '''\n</body>\n</html>\n'''

html_start_lang = '''<!DOCTYPE html>\n
<html>\n
    <head>\n
        <meta charset="utf-8">\n
        <title>Title</title>\n
<link rel="stylesheet" href="theme.css">\n
    </head>\n
	<body>\n
'''



def index_html_lang(languages):
    index_str = ""
    index_str += '  <meta http-equiv="content-language" content="kr">\n'
    index_str += '  <meta http-equiv="refresh" content="0; URL=lang/kr.html">\n'

    for i in languages:
        index_str += '  <meta http-equiv="content-language" content="' + i +  '">\n'
        index_str += '  <meta http-equiv="refresh" content="0; URL=lang/' + i + '.html">\n'
    index_str += '''   <title>My Website</title>\n</head>\n<body>\n'''
    return index_str

def merge_html(languages):
    return html_start + index_html_lang(languages) + html_end

def merge_html_lang(content):
    return html_start_lang + "".join(content) + html_end

def t(word, lang):
    if lang == 'ko':
        return word
    
    return (trans.translate(word, dest=lang)).text




def editor(lang):
    
    content = [
        h3(t("Magic Mask", lang)) ,
        "<br>",
        h1(t("고도로 발전된 기술은 마법과 구별되지 않는다 - 클라크의 삼법칙", lang)),
        "<br>",
        "<br>",
        h2(t("Product launch soon.", lang)),
        "<br>",
        "<br>",
        "<br>",
        br(),
        br(),
        br(),
        br(),
        br(),
        p("사업자 등록 번호 : 000-00-00000   |   이메일 : example@company.com")

    ]
    
    return content

lang_list = ['en', 'ja', 'zh-cn', 'zh-tw']

def main():
    f = open('index.html', 'w')
    f.write(merge_html(lang_list))
    f.close()
    
    f = open('lang/kr.html', 'w')
    f.write(merge_html_lang(editor('ko')))
    f.close()

    for i in lang_list:
        trans_page = merge_html_lang(editor(l))

        f = open(f'lang/{i}.html', 'w')
        f.write(trans_page)
        f.close()

if __name__ == "__main__":
    main()
