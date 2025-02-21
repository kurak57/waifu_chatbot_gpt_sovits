# Waifu Voice Chatbot

## Description
This project is a chatbot that utilizes Large Language Models (LLMs) and text-to-speech (TTS) to create a more interactive AI character. The chatbot is designed to work with LM Studio for LLM inference and GPT-SoVITS for voice synthesis.

## Prerequisites
Before running this project, you need to install and start GPT-SoVITS. You can find the repository here: [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS).

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/kurak57/waifu_chatbot_gpt_sovits.git
   cd waifu_chatbot_gpt_sovits
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add the necessary configurations.

## Usage
1. Start GPT-SoVITS before running the chatbot.
2. Run `inference_webui.py` from GPT-SoVITS to enable voice synthesis.
4. This project uses LM Studio to run the LLM. The default model used is Meta-Llama-3.1-8B-Instruct, but you can change it according to your needs.
5. Run the waifu chatbot script:
   ```sh
   python main.py
   ```

## Configuration
Create a `.env` file in the root directory with the following structure:

```ini
# LLM API Configuration
LLM_BASE_URL=http://localhost:1234/v1 #LM STUDIO DEFAULT
LLM_API_KEY=lm-studio #LM STUDIO DEFAULT

# TTS API Configuration
TTS_BASE_URL=http://localhost:9872/ #GPT-sovits default
```

## Features
- Supports multiple AI languages (Japanese, English, Chinese)
- Customizable character personalities
- Integration with LM Studio for local LLM inference
- Text-to-Speech (TTS) using GPT-SoVITS

## Customization
- Modify `config.py` to adjust LLM and TTS settings.
- Change `CHARACTER_NAME` in `config.py` to load different personalities.
