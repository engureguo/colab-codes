from gradio_client import Client

client = Client("egu0/BubbleSheep-Hgn_trans_en2zh")

rsp = client.predict("Hello")
print(rsp)