def markdownparser(markdown):
  z=markdown.count("#");
  if  (markdown[z].isspace()==False or z==0 or z>6) :
       return (markdown)
  else:
      if z==1:
       return ("<h1>"+markdown[z+1:]+"</h1>")
      elif z==2:
       return ("<h2>"+markdown[z+1:]+"</h2>")
      elif z==3:
       return ("<h3>"+markdown[z+1:]+"</h3>")
      elif z==4:
       return ("<h4>"+markdown[z+1:]+"</h4>")
      elif z==5:
       return ("<h5>"+markdown[z+1:]+"</h5>")
      elif z==6:
       return ("<h6>"+markdown[z+1:]+"</h6>")

  
print(markdownparser("## header"))
