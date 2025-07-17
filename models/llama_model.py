from transformers import LlamaForCasualLM, LlamaTokenizer

def interpret_query(query):
    model = LlamaForCasualLM.from_pretrained