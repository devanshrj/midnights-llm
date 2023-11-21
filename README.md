# Midnights-LLM
This repository contains instructions and tools to locally deploy LLMs on the Midnights server.

## Setup
The current deployment is primarily based on the [vLLM](https://github.com/vllm-project/vllm) for high-throughtput and memory-efficient inference for LLMs. The main requirements are `vLLM`, `PyTorch`, `transformers`, and `openai` (for deploying LLMs as a server that mimics the OpenAI API protocol).

Since Midnights' has an older CUDA version, I would recommend using the `requirements.txt` file to install all dependencies (with CUDA compatbility). Specifically,
```
<create new conda environment>
pip install -r requirements.txt
```

### To Do
- [ ] Add commands for inference and deployment
- [ ] Add example scripts for inference and deployment