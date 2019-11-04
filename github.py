#!/usr/bin/evn python3
#coding=utf-8
#当你在github和本地配置好私钥和公钥时，可直接使用脚本创建username.github.io.git仓库
#python3 github.py -u Benjaminzxm -g Benjaminzxm -n Benjaminzxm.github.io -m init
# python3 github.py -u Garretming -g Garretming -n Garretming.github.io -m init
import os
import sys,getopt


def main():
  help = 'github.py -u <username> -m <message> -g <group> -n <name>'
  username = None
  message = None
  group  = None
  name = None
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hu:m:g:n:")
  except getopt.GetoptError:
    print(help)
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
        print(help)
        sys.exit()
    elif opt in ("-u", "--username"):
        username = arg
    elif opt in ("-m", "--message"):
        message = arg
    elif opt in ("-g", "--group"):
        group = arg
    elif opt in ("-n", "--name"):
        name = arg
  if message == None:
    print(help)
    sys.exit()
  if group == None:
    print("please provide your organization in github")
    sys.exit()
  if name == None:
    print("please provide your project name in github;default   ' name = os.path.basename(path)'")
    sys.exit()
  os.system('rm -rf .git')
  os.system('git init')
  #使只在第一次提交时输入密码，后期无需输入
  os.system('git config --global credential.helper store')
  # os.system('curl -u Garretming -d \'{"name":"slg_cilent","description":"slg_cilent is a cilent for slg games"}\' https://api.github.com/user/repos')
  os.system('curl -u '+username+' -d \'{"name":"'+name+'","description":"'+message+'"}\' https://api.github.com/user/repos')
  # os.system('git remote add origin git@gitlab.com:' + group +'/' + name +'.git')
  os.system('git remote add origin git@'+ username+'.github.com:'+group +'/' + name+'.git')
  # os.system('git submodule add https://github.com/Misiur/buster.git buster')
  # os.system('git submodule add git@github.com:TryGhost/Ghost.git ghost') # 这个版本有问题
  os.system('git add .')
  # os.system('git pull --rebase')
  os.system('git commit -m ' + '\"' + message + '\"')
  # os.system('git stash')
  os.system('git push -u origin master')


  

if __name__ == '__main__':
  main()
    
   
         







   
   
    
  





