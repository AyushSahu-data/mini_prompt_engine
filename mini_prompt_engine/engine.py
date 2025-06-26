from mini_prompt_engine.utils import render_template, call_openai, call_anthropic, load_config

class PromptEngine:
    def __init__(self, config_path="mini_prompt_engine/config.yaml"):
        self.config = load_config(config_path)
        self.provider = self.config.get("provider")

    def generate(self, step_name, context, stream=False):
        prompt = render_template(f"{step_name}.j2", context)
        if self.provider == "openai":
            if stream:
                return call_openai(prompt, self.config, stream=True)
            return call_openai(prompt, self.config)
        elif self.provider == "anthropic":
            return call_anthropic(prompt, self.config)
        else:
            raise ValueError("Unknown provider: " + self.provider)
