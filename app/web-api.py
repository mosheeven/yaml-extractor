import flask
from flask import request
import yaml
import jmespath


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Yaml Extractor</h1><p>Post endpoint: /api/yaml_extract.</p>
    <p>Accept: application/json.</p>
    <p>Message structure: 
    {
    "text": "YAML_TEXT",
    "expr": "EXPR" 
    }</p>'''

@app.route('/health', methods=['GET'])
def health():
    return '''<h1>:)</h1>'''


@app.route('/api/yaml_extract', methods=['POST'])
def yaml_extractor():
    post_body = request.get_json(force=True)
    yaml_data = yaml.safe_load(post_body.get("text"))
    path = jmespath.search(post_body.get("expr"), yaml_data)
    print(path)
    return_dict = {}
    return_dict['data'] = path

    return return_dict

if __name__ == "__main__":
    app.run(host='0.0.0.0')