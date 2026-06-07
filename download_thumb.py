  import urllib.request, shutil, sys, urllib.parse                              
                                                                              
  WORKER_URL = 'https://pexels-proxy.cleary0720.workers.dev'                    
   
  category = sys.argv[1]                                                        
  slug     = sys.argv[2]                                    
  keyword  = sys.argv[3] if len(sys.argv) > 3 else category                     
  out      = f'images/{slug}-thumb.jpg'                     
                                                                                
  params = urllib.parse.urlencode({'query': keyword, 'category': category})     
  req = urllib.request.Request(                                                 
      WORKER_URL + '?' + params,                                                
      headers={'User-Agent': 'TheMacroBrief/1.0'}                               
  )                                                                           
  with urllib.request.urlopen(req, timeout=30) as r:                            
      with open(out, 'wb') as f:                            
          shutil.copyfileobj(r, f)                                              
                                                                                
  print('Saved: ' + out + ' (keyword: ' + keyword + ')')                      
