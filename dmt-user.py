import os

path=os.path.join(os.environ.get('HOME'),'.dmt/user/def/user.def')

with open(path,'w') as user:
    user.write("user:\n  shell: full")

