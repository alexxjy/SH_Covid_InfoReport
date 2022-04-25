from pyquery import PyQuery as pq
import pdfkit
import imgkit

document = pq(filename='test.html')
p = document('p') # parse index.html 
## p stands for <p> </p> element
head = document('head')
# print(head)
## head stands for <head> </head> + <body> </body>
# p.empty()
# print(p)
body = document('body')
# print(body)
## body stands for <body> </body>


# for i in document.items("div.titleblock > h2"):
#     i.replace_with('<h2> Covid Info </h2>')
#     print(i.text())
# NEED: 

# replace covid news bulletin
countnews = 0
for i in document.items("div > table.summarytable"):
    if countnews == 2:
        print(i.text()) # EXPECTED: 4月9日：全员核酸
    if countnews == 4:
        print(i.text()) # EXPECTED: 暂无
    countnews = countnews + 1


# replace table bulletin
# EXPECTED: 6、7、21
# 解封:55,57,59<br>新增:21
# 无
for i in document.items("div > table.summarytable > tbody > tr > td"):
    print(i.text())

# replace specifictable
# EXPECTED: 6
# 1
# 0
# 0
# 1
# /
# 7
# 1
# 0
# 0
# 1
# /
# Actual: 6、7、21
# 解封:55,57,59
# 新增:21
# 无
for i in document.items("div > table.specifictable > tbody > tr "):
    print(i.text())

    
# modify tags
def input():

    try:
        if p.has_class('summarytable'):
            title = input('Enter a title')


    except:
        print('Error, cannot find class')

# update html
def update_html(outputfile):
    test2 = open(outputfile, "w")
    #write string to file
    test2.write(document.__str__())
    #close file
    test2.close()

# convert html to pdf
# FIXME: cannot display head background
def convert_to_pdf(file_name):
    pdfkit.from_file(file_name, 'out2.pdf')

# convert html to image
# FIXME: cannot display head background
def convert_to_image(filename):
    imgkit.from_file(filename, 'out.jpg')


update_html('test2.html')
convert_to_pdf('test.html')
convert_to_image('test.html')
