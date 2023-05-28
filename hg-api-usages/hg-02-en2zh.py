import requests
from utils import read_hf_token

# space: https://huggingface.co/spaces/egu0/BubbleSheep-Hgn_trans_en2zh

API_URL = "https://api-inference.huggingface.co/models/BubbleSheep/Hgn_trans_en2zh"
huggingface_token = read_hf_token()
headers = {"Authorization": "Bearer " + huggingface_token}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I love you, Lily.",
})

print(output[0]['translation_text'])


