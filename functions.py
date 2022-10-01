# originally until_x() from here: https://stackoverflow.com/questions/68905829/creating-a-newline-in-a-string-after-20-characters-at-the-end-of-a-word-python
def autolinebreak(string: str, x: int = 20) -> str:
     lst = string.split()
     line = ''
     str_final = ''
     for word in lst:
         if len(line + ' ' + word) <= x:
             str_final += word + ' '
             line += word + ' '
         else:
             str_final += '\n' +  word + ' '
             line = word + ' '
     return str_final