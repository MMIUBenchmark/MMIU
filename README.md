
# MMIU

<p align="left">
  <a href="#🚀-quick-start"><b>Quick Start</b></a> |
  <a href="https://huggingface.co/MMIUBenchmark/MMIU/tree/main"><b>Dataset</b></a> |
  <a href="#🖊️-citation"><b>Citation</b></a> <br>
</p>


This repository is the official implementation of MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models


## 💡 News


-  We have released the dataset at xx 🔥🔥🔥



## Introduction
Multimodal Multi-image Understanding (MMIU) benchmark, a comprehensive evaluation suite designed to assess LVLMs across a wide range of multi-image tasks. MMIU encompasses 7 types of multi-image relationships, 52 tasks, 77K images, and 11K meticulously curated multiple-choice questions, making it the most extensive benchmark of its kind. 
![overview](assets/overview.jpg)








## Evaluation Results Overview
- The closed-source proprietary model GPT-4o from OpenAI has taken a leading position in MMIU, surpassing other models such as InternVL2-pro, InternVL1.5-chat, Claude3.5-Sonnet, and Gemini1.5 flash. Note that the open-source models InternVL2-pro.


- Some powerful LVLMs like InternVL1.5  and  GLM4V whose pre-training data do not contain multi-image content even outperform many multi-image models which undergo multi-image supervised fine-tuning (SFT), indicating the strong capacity in single-image understanding is the foundation of multi-image comprehension.
- By comparing performance at the level of image relationships, we conclude that LVLM excels at understanding semantic content in multi-image scenarios but has weaker performance in comprehending temporal and spatial relationships in multi-image contexts.
- The analysis based on the task map reveals that models perform better on high-level understanding tasks such as video captioning which are in-domain tasks, but struggle with 3D perception tasks such as 3D detection and temporal reasoning tasks such as image ordering which are out-of-domain tasks.
- By task learning difficulty analysis, tasks involving ordering, retrieval and massive images cannot be overfitted by simple SFT, suggesting that additional pre-training data or training techniques should be incorporated for improvement.
![taskmap](assets/taskmap.jpg)


## 🏆 Leaderboard



| Rank | Model | Score |
| ---- | ---------------------- | ----- |
| **1** | **GPT4o** | **55.72** |
| 2 | Gemini | 53.41 |
| 3 | Claude3 | 53.38 |
| **4** | **InternVL2** | **50.30** |
| 5 | Mantis | 45.58 |
| 6 | Gemini1.0 | 40.25 |
| 7 | internvl1.5-chat | 37.39 |
| 8 | Llava-interleave | 32.37 |
| 9 | idefics2_8b | 27.80 |
| 10 | glm-4v-9b | 27.02 |
| 11 | deepseek_vl_7b | 24.64 |
| 12 | XComposer2_1.8b | 23.46 |
| 13 | deepseek_vl_1.3b | 23.21 |
| 14 | flamingov2 | 22.26 |
| 15 | llava_next_vicuna_7b | 22.25 |
| 16 | XComposer2 | 21.91 |
| 17 | MiniCPM-Llama3-V-2_5 | 21.61 |
| 18 | llava_v1.5_7b | 19.19 |
| 19 | sharegpt4v_7b | 18.52 |
| 20 | sharecaptioner | 16.10 |
| 21 | qwen_chat | 15.92 |
| 22 | monkey-chat | 13.74 |
| 23 | idefics_9b_instruct | 12.84 |
| 24 | qwen_base | 5.16 |
| -   | Frequency Guess        | 31.5  |
| -   | Random Guess           | 27.4  |




## 🚀 Quick Start

Here, we mainly use the VLMEvalKit framework for testing, with some separate tests as well. Specifically, for multi-image models, we include the following models:

**transformers == 33.0**

- `XComposer2`
- `XComposer2_1.8b`
- `qwen_base`
- `idefics_9b_instruct`
- `qwen_chat`
- `flamingov2`

**transformers == 37.0**
- `deepseek_vl_1.3b`
- `deepseek_vl_7b`

**transformers == 40.0**

- `idefics2_8b`

For single-image models, we include the following:

**transformers == 33.0**

- `sharecaptioner`
- `monkey-chat`

**transformers == 37.0**

- `sharegpt4v_7b`
- `llava_v1.5_7b`
- `glm-4v-9b`

**transformers == 40.0**

- `llava_next_vicuna_7b`
- `MiniCPM-Llama3-V-2_5`

We use the VLMEvalKit framework for testing. You can refer to the code in `VLMEvalKit/test_models.py`. Additionally, for closed-source models, please replace the following part of the code by following the example here:

```python
response = model.generate(tmp) # tmp = image_paths + [question]
```

For other open-source models, we have provided reference code for `Mantis` and `InternVL1.5-chat`. For `LLava-Interleave`, please refer to the original repository.










