import gradio as gr

def generate_response(prompt):
    return f"Gemma response placeholder for: {prompt}"

demo = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="Gemma Hackathon Starter"
)

demo.launch()
