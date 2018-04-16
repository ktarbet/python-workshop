import re

#pretend text for parsing
text="""


METHOD ONE A(123,
abc
xyz
);

METHOD TWO A(123,
abc
xyz
);

METHOD ONE B(123,
abc
xyz
);

METHOD TWO B(123,
abc
xyz
);


"""
newtext=""
text_temp=text
while len(text_temp)>0:
    if 'METHOD' in text_temp:

        #subsample one function code-block
        text_sub=text_temp[re.search('METHOD',text_temp).regs[0][0]:re.search(";",text_temp).regs[0][0]+1]

        #remove subsampled text from temporary text that is being parsed
        text_temp = text_temp[re.search(';', text_temp).regs[0][0] + 2:]

        #if the text contains desired function, append to output text
        if 'METHOD ONE' in text_sub:
            newtext+="\n"+text_sub
    else:
        #workaround to keep any left-over text from going into an infinite while-loop
        text_temp=""

print newtext