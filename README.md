# Clone the repository
## Run the following command in your terminal:

```
git clone https://github.com/hassancs91/AI-Content-Ideas-Generator-Prototype.git
```

# Environment variables
## Copy the `.env-example` file to `.env`:

```
cp .env-example .env
```

### Open the `.env` file and choose a provider:

- `LLM_PROVIDER`: `ollama` (free, runs on your computer) or `grok` (xAI API). Defaults to `ollama`.

**Ollama (free):** install Ollama from ollama.com, then run `ollama pull llama3.1` once. Ollama must be running while the app works. Set `OLLAMA_MODEL` to change the model.

**Grok:** set `XAI_API_KEY` to your xAI API key and optionally `GROK_MODEL`. Grok usage may be billed by xAI.

# Install required packages
## For Ubuntu 22.04, run the following command in your terminal:

```
pip3 install -r requirements.txt
```

<!-- lwh-footer -->

---

## 📘 The free book

This tool is one block. The book has the other 46.

**[Vibe Engineering Blocks](https://learnwithhasan.com/blocks/?utm_source=github&utm_medium=readme&utm_campaign=AI-Content-Ideas-Generator-Prototype&utm_content=footer)** is my free 74-page book.
47 building blocks for shipping real apps with AI. One block per page, each with the exact
prompt to hand your AI.

Built by **[Hasan Aboul Hasan](https://learnwithhasan.com/?utm_source=github&utm_medium=readme&utm_campaign=AI-Content-Ideas-Generator-Prototype&utm_content=footer)**. I build real products with AI and
write down exactly how.
[Guides](https://learnwithhasan.com/guides/?utm_source=github&utm_medium=readme&utm_campaign=AI-Content-Ideas-Generator-Prototype&utm_content=footer) &nbsp;·&nbsp;
[YouTube](https://www.youtube.com/@HasanAboulHasan) &nbsp;·&nbsp;
[Community](https://learnwithhasan.com/community/?utm_source=github&utm_medium=readme&utm_campaign=AI-Content-Ideas-Generator-Prototype&utm_content=footer)
