import requests
import json
import os
with open('/Users/lixiaoyi/Desktop/word/words.txt','r') as file:
    for line in file:
        word = line.strip()
        if os.path.exists('/Users/lixiaoyi/Desktop/word/{}.md'.format(word)):
            pass
        else:
            question = "I am learning English words. Please give me some example sentences containing the word \'{}\' to help me understand the meaning of the word and how to use the word."
            req_data = {"model": "mistral-nemo","prompt":question.format(word),"stream": False}
            r = requests.post('http://192.168.0.23:11434/api/generate', data=json.dumps(req_data))
            answer = r.json()['response']
            with open('/Users/lixiaoyi/Desktop/word/{}.md'.format(word),'w') as f:
                f.write(answer)