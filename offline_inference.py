from vllm import LLM, SamplingParams

# sample prompt
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# create a sampling params object
# list of parameters for SamplingParams: https://github.com/vllm-project/vllm/blob/7d761fe3c12e87df37383467c43c97dec2bb8470/vllm/sampling_params.py#L29
sampling_params = SamplingParams(temperature=0.7, max_tokens=1600, top_p=0.9)

# create an LLM
# model can be any model from huggingface hub
llm = LLM(model="mistralai/Mistral-7B-v0.1")

# vllm supports AWQ quantized models using the `quantization` parameter
# llm = LLM(model="TheBloke/Mistral-7B-Instruct-v0.1-AWQ", quantization="AWQ")

# generate texts from the prompt
# output is a list of RequestOutput objects that contain the prompt, generated text, and other information
outputs = llm.generate(prompts, sampling_params)

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")