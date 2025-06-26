# mini_prompt_engine

# Mini Prompt Engine

A lightweight, self-contained system to manage structured interactions with large language models (LLMs) using prompt templates and staged workflows.

##  Features
- Jinja2-based templated prompt rendering
- OpenAI and Anthropic API support
- Structured 3-step flow: `autoconfig`, `plan_architecture`, `finalize`
- Optional streaming for OpenAI

##  Project Structure
```
mini_prompt_engine/
├── templates/               # Jinja2 prompt templates
├── utils.py                 # Template rendering and API calling logic
├── engine.py                # Core generation engine
├── config.yaml              # API credentials and model setup
main.py                      # CLI interface
requirements.txt             # Dependencies
README.md                    # This file
```

##  Setup
```bash
# Clone the repo
$ git clone <your-repo-url>
$ cd mini_prompt_engine

# Create virtual environment (optional)
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

##  Configuration
Edit `mini_prompt_engine/config.yaml` to include your API key and model:
```yaml
provider: openai  # or anthropic
api_key: "your-api-key"
model: "gpt-4"
```

##  Running the Engine
```bash
$ python main.py
```
You'll be prompted to enter your `project_type` and `tech_stack`. The tool will walk you through three stages of a prompt-driven LLM workflow.

##  Template Customization
Templates live in `mini_prompt_engine/templates/`. Each stage (`autoconfig`, `plan_architecture`, `finalize`) corresponds to a `.j2` Jinja2 template file.

##  Future Improvements
- Add web interface (Flask/Streamlit)
- Support for saving session history
- Advanced template validation and versioning
