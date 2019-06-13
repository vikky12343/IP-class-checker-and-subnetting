print('171B153')



def ipclass(ip):
    x=int(a.split(".")[0])
    Y=int(a.split(".")[1])
    Z=int(a.split(".")[2])
    w=int(a.split(".")[3])
    
    if x>=0 and x<=127:
        
        return 'a'
    
    elif x>=128 and x<=191:
    
        return 'b'
      
        
    elif x>=192 and x<=223:

        return 'c'
        

    elif x>=224 and x<=239:
        
        return 'd'
         
    elif x>=240 and x<=255:
    
        return 'e'
	
def ipmask(ip):
    if x>=0 and x<=127:
        
        return '255.0.0.0'
    
    elif x>=128 and x<=191:
    
        return '255.255.0.0'
          
    elif x>=192 and x<=223:
        
        return '255.255.255.0'
        
    elif x>=224 and x<=239:
         
        return '255.255.255.255'
         
    elif x>=240 and x<=255:
        
        return '255.255.255.255'
    
        

def network_broadcast_address(ip):
    x=int(a.split(".")[0])
    Y=int(a.split(".")[1])
    Z=int(a.split(".")[2])
    w=int(a.split(".")[3])
    if x>=0 and x<=127:
        
        network=str(x)+"0.0.0"
        broadcast=str(x)+"."+"255.255.255"
    
    elif x>=128 and x<=191:

         network=str(x)+"."+str(y)+".0.0"
         broadcast=str(x)+"."+str(y)+".255.255"
    
        
          
    elif x>=192 and x<=223:

         network=str(x)+"."+str(y)+"."+str(z)+".0"
         broadcast=str(x)+"."+str(y)+"."+str(z)+".255"
        
        
        
    elif x>=224 and x<=239:
        network=ip
        broadcast=ip

         
    elif x>=240 and x<=255:
        network=ip
        broadcast=ip
        
    return (network,broadcast)
