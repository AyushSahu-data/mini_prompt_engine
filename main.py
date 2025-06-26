from mini_prompt_engine.engine import PromptEngine

def run():
    engine = PromptEngine()

    context = {
        "project_type": input("Project type (e.g., chatbot, webapp): "),
        "tech_stack": input("Tech stack (e.g., Python, React, AWS): ")
    }

    print("\n[Step 1] Autoconfig:")
    print(engine.generate("autoconfig", context))

    print("\n[Step 2] Plan Architecture:")
    print(engine.generate("plan_architecture", context))

    print("\n[Step 3] Finalize:")
    print(engine.generate("finalize", context))

if __name__ == "__main__":
    run()
