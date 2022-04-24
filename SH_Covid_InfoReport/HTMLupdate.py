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


for i in document.items("div.titleblock > h2"):
    print(i.text())
# NEED: 

for i in document.items("div > table.summarytable"):
    print(i.text())

for i in document.items("div > table.summarytable"):
    print(i.text())

    
# modify tags
def input():

    try:
        if p.has_class('summarytable'):
            title = input('Enter a title')


    except:
        print('Error, cannot find class')


# convert html to pdf
# FIXME: cannot display head background
def convert_to_pdf(file_name):
    pdfkit.from_file(file_name, 'out2.pdf')

# convert html to image
# FIXME: cannot display head background
def convert_to_image(filename):
    imgkit.from_file(filename, 'out.jpg')

convert_to_pdf('test.html')
convert_to_image('test.html')
