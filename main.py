from flask import Flask, request, jsonify, abort
from gpt4all import GPT4All
import logging

gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")
app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@app.route('/completion', methods=['POST'])
def completion():
    try:
        logging.info("Request:%s", request)
        content = request.get_json()['content']
        prompt = f"""You are my note-taking assistant. Please tag any given piece of text with relevant hashtags. Please, only answer with 3 (three) or less tags without any additional information.

\"{content}\"
"""
        result = gptj.generate(prompt, streaming=False)
        logging.info(result)
        return jsonify({'content': result})
    except Exception as e:
        logging.error("Error:%s", e)
        abort(500, e)

@app.route('/hc', methods=['GET'])
def hc():
    return jsonify({'message': 'OK'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
