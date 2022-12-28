#%%
import yaml
import os
import logging

from kiteconnect import KiteConnect

#%%
# UDF

def get_cred(conf) :
    cred_path_wo_sep_list = conf[0]['Path']['cred'].split('/')
    cwd_sep_wo_sep_list = os.getcwd().split(os.sep)
    for dir in cred_path_wo_sep_list :
        if dir == '..' :
            cwd_sep_wo_sep_list.pop()
        else :
            cwd_sep_wo_sep_list.append(dir)

    cred_path = os.sep.join(cwd_sep_wo_sep_list)
    try :
        with open(cred_path, 'r') as credyaml :
            cred = yaml.load(credyaml, Loader=yaml.FullLoader)
    except FileNotFoundError as e :
        #print ('check relative file path in Config.config.yaml')
        raise Exception(e, 'check relative file path in Config.config.yaml')
    assert 'Credentials' in cred[0].keys(), 'Credentials Not Set'
    assert 'USER_ID' in cred[0]['Credentials'].keys(), 'USER_ID Not Set'
    USER_ID = cred[0]['Credentials']['USER_ID']
    assert 'PASSWD' in cred[0]['Credentials'].keys(), 'PASSWD Not Set'
    PASSWD = cred[0]['Credentials']['PASSWD']
    assert 'TWOFA' in cred[0]['Credentials'].keys(), 'PASSWD Not Set'
    TWOFA = cred[0]['Credentials']['TWOFA']
    assert 'TOKEN' in cred[0]['Credentials'].keys(), 'TOKEN Not Set'
    TOKEN = cred[0]['Credentials']['TOKEN']

    return (USER_ID, PASSWD, TWOFA, TOKEN)

#%%
#configuration
logging.basicConfig(level=logging.DEBUG)

with open('Config/config.yaml', 'r') as confyaml :
    conf = yaml.load(confyaml, Loader=yaml.FullLoader)

assert 'Path' in conf[0].keys(), 'Path Not Set'
assert 'cred' in conf[0]['Path'].keys(), 'Path Not Set'

USER_ID, PASSWD, TWOFA, TOKEN, = get_cred(conf)

print (USER_ID, PASSWD, TWOFA, TOKEN)

# %%

kite = KiteConnect(api_key="your_api_key")
# %%
