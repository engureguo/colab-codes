import configparser

def read_hf_token():
    cp = configparser.ConfigParser()
    cp.read('config.ini',  encoding='utf-8')
    return cp.get('HF', 'token')