#!/usr/bin/python3
import sys,os,datetime,dataclasses,concurrent.futures,multiprocessing

@dataclasses.dataclass
class Result:
  name:str
  access:object

SKIPLINKS=False
if SKIPLINKS:
  print('Ignoring symbolic links...')

targets=sys.argv[1:]
results=[]
processing=[]

if len(targets)==0:
  print('Usage: acleanhome.py [folder1] [folder2] [folder3] [...]')
  sys.exit(0)

def crawl(folder,latest=0,top=False):
  for root,dirs,files in os.walk(folder):
    for d in dirs:
      if top:
        print(f'Crawling {d}...')
      access=crawl(os.path.join(root,d),latest)
      if access>latest:
        latest=access
    for f in files:
      f=os.path.join(root,f)
      if SKIPLINKS and os.path.islink(f):
        continue
      try:
        access=os.stat(f,follow_symlinks=False).st_atime
        if access>latest:
          latest=access
      except Exception as e:
        print(e)
  return latest

def update():
  working=len(processing)
  if working>0:
    print(f'Processing {working} folders: {" ".join(processing)}')

def checkaccess(folder):
  processing.append(folder)
  update()
  try:
    access=crawl(folder,0,True)
    results.append(Result(folder,access))
  except Exception as e:
    print(e)
  processing.remove(folder)
  update()

with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as pool:
  for task in pool.map(checkaccess,targets):
    pass

print()
today=datetime.datetime.now()
for r in sorted(results,key=lambda x:x.access):
  access='?' if r.access==0 else today-datetime.datetime.fromtimestamp(r.access)
  print(f'{r.name}\tLast access: {access}')
