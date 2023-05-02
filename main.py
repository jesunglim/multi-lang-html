import googletrans

trans = googletrans.Translator()


html_start = '''<!DOCTYPE html>\n
<html>\n
    <head>\n
        <meta charset="utf-8">\n
        <title>Title</title>\n
<link rel="stylesheet" href="theme.css">\n
    </head>\n
	<body>\n'''
html_end = '''\n    </body>\n</html>\n'''

def merge_html(content):
    return html_start + "".join(content) + html_end

def t(word, lang):
    if lang == 'ko':
        return word
    
    return (trans.translate(word, dest=lang)).text

def br():
    return "<br>\n"

def p(word):
    start = "   <p>"
    end = "</p>\n"
    return start+word+end

def h1(word):
    start = "   <h1>"
    end  = "</h1>\n"
    return start+word+end

def h1(word):
    start = "   <h1>"
    end  = "</h1>\n"
    return start+word+end

def h2(word):
    start = "   <h2>"
    end  = "</h2>\n"
    return start+word+end

def h3(word):
    start = "   <h3>"
    end  = "</h3>\n"
    return start+word+end

def h4(word):
    start = "   <h4>"
    end  = "</h4>\n"
    return start+word+end

def h5(word):
    start = "   <h5>"
    end  = "</h5>\n"
    return start+word+end

def h6(word):
    start = "   <h6>"
    end  = "</h6>\n"
    return start+word+end








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
    page = merge_html(editor('ko'))
    
    f = open('lang/kr.html', 'w')
    f.write(page)
    f.close()

    for l in lang_list:
        trans_page = merge_html(editor(l))

        f = open(f'lang/{l}.html', 'w')
        f.write(trans_page)
        f.close()

if __name__ == "__main__":
    main()
