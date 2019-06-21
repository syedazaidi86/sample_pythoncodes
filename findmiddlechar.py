def get_middle(str):
 lens=len(str);
 if (lens>=1 & lens<=1000):
   if (lens % 2)==0:
       return str[lens//2-1]+str[lens//2]
   else:
       return str[lens//2]
 else:
    return ""
   
strtest="test"
print(get_middle(strtest))
