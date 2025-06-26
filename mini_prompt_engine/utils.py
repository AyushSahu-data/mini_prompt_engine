import yaml
from jinja2 import Environment, FileSystemLoader
import openai
import anthropic

def load_config(path="mini_prompt_engine/config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def render_template(template_name, context):
    env = Environment(loader=FileSystemLoader("mini_prompt_engine/templates"))
    template = env.get_template(template_name)
    return template.render(**context)

def call_openai(prompt, config, stream=False):
    openai.api_key = config["api_key"]
    response = openai.ChatCompletion.create(
        model=config["model"],
        messages=[{"role": "user", "content": prompt}],
        stream=stream
    )
    if stream:
        for chunk in response:
            if 'choices' in chunk:
                content = chunk['choices'][0].get('delta', {}).get('content', '')
                yield content
    else:
        return response['choices'][0]['message']['content']

def call_anthropic(prompt, config):
    client = anthropic.Anthropic(api_key=config["api_key"])
    message = client.messages.create(
        model=config["model"],
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text
