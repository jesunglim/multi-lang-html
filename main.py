from utils.html import *
from utils.translator import *
from editer import *




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







def main():
    f = open('index.html', 'w')
    f.write(merge_html(lang_list))
    f.close()
    
    f = open('lang/kr.html', 'w')
    f.write(merge_html_lang(editor('ko')))
    f.close()

    for i in lang_list:
        trans_page = merge_html_lang(editor(i))

        f = open(f'lang/{i}.html', 'w')
        f.write(trans_page)
        f.close()

if __name__ == "__main__":
    main()
