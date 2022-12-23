import os
import sys

preamble = '''
<html>

<head>
<meta name=Generator content="Microsoft Word 15 (filtered)">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
	{font-family:Garamond;
	panose-1:2 2 4 4 3 3 1 1 8 3;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:8.0pt;
	margin-left:0in;
	line-height:107%;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
.MsoChpDefault
	{font-family:"Calibri",sans-serif;}
.MsoPapDefault
	{margin-bottom:8.0pt;
	line-height:107%;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
-->
</style>

</head>

<body bgcolor="#0D0D0D" lang=EN-US style='word-wrap:break-word'>
'''

def make_image(image_file_string):
    return '''
<div style="text-align: center;">
<img src="../pictures_namefiles/{}" width="1000" style="display: block; margin-right: auto; margin-left: auto;">
</div>

'''.format(image_file_string)

middle = '''
<div style="text-align: left;" class=WordSection1>
'''

def make_block(paragraph):

    if paragraph == "\n":
        return '''<p class=MsoNormal align=center style='text-align:center'><b><span
style='font-size:45.0pt;line-height:107%;font-family:"Garamond",serif;
color:#FFF2CC'>&nbsp;</span></b></p>\n\n'''

    return '''
    <p class=MsoNormal><b><span style='font-size:45.0pt;line-height:107%;
font-family:"Garamond",serif;color:#FFF2CC'>{}</span></b></p>
'''.format(paragraph.replace('"', '&quot').replace('“', '&quot').replace('”', '&quot').replace("'", '\''))

end = '''
</div>

</body>

</html>
'''



header = 0
for line in open("Website_Names_Master.tsv"):
    tokens = line.split("\t")
    if header == 0:
        header += 1
        continue
    else:
        web_file = open("./pages/" + tokens[7] + ".html", "w")
        web_file.write(preamble + '\n')
        if os.path.exists('./pictures_namefiles/{}'.format(tokens[6])):
            print(tokens[6] + " - exists!")
            web_file.write(make_image(tokens[6]) + "\n")
            web_file.write(make_block("\n"))
        for note_paragraph in open("./notes_namefiles/" + tokens[5], encoding='utf-8'):
            print(note_paragraph)
            web_file.write(make_block(note_paragraph))
        web_file.write(end)
        web_file.close()
