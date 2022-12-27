import yaml
import os

with open('kitemoney/Config/config.yaml', 'r') as confyaml :
    conf = yaml.load(confyaml, Loader=yaml.FullLoader)

assert 'Path' in conf[0].keys(), 'Path Not Set'
assert 'cred' in conf[0]['Path'].keys(), 'Path Not Set'

def get_cred(conf) :
    cred_path_wo_sep_list = conf[0]['Path']['cred'].split('/')
    cwd_sep_wo_sep_list = os.getcwd().split(os.sep)
    for dir in cred_path_wo_sep_list :
        if dir == '..' :
            cwd_sep_wo_sep_list.pop()
        else :
            cwd_sep_wo_sep_list.append(dir)

    cred_path = os.sep.join(cwd_sep_wo_sep_list)

    with open(cred_path, 'r') as credyaml :
        cred = yaml.load(credyaml, Loader=yaml.FullLoader)
    print (cred)

get_cred(conf)