# Falcor 👋

![GitHub stars](https://img.shields.io/github/stars/dangerpotter/falcor?style=social)
![GitHub forks](https://img.shields.io/github/forks/dangerpotter/falcor?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/dangerpotter/falcor?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/dangerpotter/falcor)
![GitHub language count](https://img.shields.io/github/languages/count/dangerpotter/falcor)
![GitHub top language](https://img.shields.io/github/languages/top/dangerpotter/falcor)
![GitHub last commit](https://img.shields.io/github/last-commit/dangerpotter/falcor?color=red)
![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Follama-Falcor%2Follama-wbui&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)
[![Discord](https://img.shields.io/badge/Discord-Falcor-blue?logo=discord&logoColor=white)](https://discord.gg/5rJgQTnV4s)
[![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/tjbck)

Falcor is an [extensible](https://github.com/Falcor/pipelines), feature-rich, and user-friendly self-hosted Falcor designed to operate entirely offline. It supports various LLM runners, including Ollama and OpenAI-compatible APIs. For more information, be sure to check out our [Falcor Documentation](https://docs.Falcor.com/).

![Falcor Demo](./demo.gif)

## Key Features of Falcor ⭐

- 🚀 **Effortless Setup**: Install seamlessly using Docker or Kubernetes (kubectl, kustomize or helm) for a hassle-free experience with support for both `:ollama` and `:cuda` tagged images.

- 🤝 **Ollama/OpenAI API Integration**: Effortlessly integrate OpenAI-compatible APIs for versatile conversations alongside Ollama models. Customize the OpenAI API URL to link with **LMStudio, GroqCloud, Mistral, OpenRouter, and more**.

- 🧩 **Pipelines, Falcor Plugin Support**: Seamlessly integrate custom logic and Python libraries into Falcor using [Pipelines Plugin Framework](https://github.com/Falcor/pipelines). Launch your Pipelines instance, set the OpenAI URL to the Pipelines URL, and explore endless possibilities. [Examples](https://github.com/Falcor/pipelines/tree/main/examples) include **Function Calling**, User **Rate Limiting** to control access, **Usage Monitoring** with tools like Langfuse, **Live Translation with LibreTranslate** for multilingual support, **Toxic Message Filtering** and much more.

- 📱 **Responsive Design**: Enjoy a seamless experience across Desktop PC, Laptop, and Mobile devices.

- 📱 **Progressive Web App (PWA) for Mobile**: Enjoy a native app-like experience on your mobile device with our PWA, providing offline access on localhost and a seamless user interface.

- ✒️🔢 **Full Markdown and LaTeX Support**: Elevate your LLM experience with comprehensive Markdown and LaTeX capabilities for enriched interaction.

- 🎤📹 **Hands-Free Voice/Video Call**: Experience seamless communication with integrated hands-free voice and video call features, allowing for a more dynamic and interactive chat environment.

- 🛠️ **Model Builder**: Easily create Ollama models via the Web UI. Create and add custom characters/agents, customize chat elements, and import models effortlessly through [Falcor Community](https://Falcor.com/) integration.

- 🐍 **Native Python Function Calling Tool**: Enhance your LLMs with built-in code editor support in the tools workspace. Bring Your Own Function (BYOF) by simply adding your pure Python functions, enabling seamless integration with LLMs.

- 📚 **Local RAG Integration**: Dive into the future of chat interactions with groundbreaking Retrieval Augmented Generation (RAG) support. This feature seamlessly integrates document interactions into your chat experience. You can load documents directly into the chat or add files to your document library, effortlessly accessing them using the `#` command before a query.

- 🔍 **Web Search for RAG**: Perform web searches using providers like `SearXNG`, `Google PSE`, `Brave Search`, `serpstack`, `serper`, `Serply`, `DuckDuckGo`, `TavilySearch` and `SearchApi` and inject the results directly into your chat experience.

- 🌐 **Web Browsing Capability**: Seamlessly integrate websites into your chat experience using the `#` command followed by a URL. This feature allows you to incorporate web content directly into your conversations, enhancing the richness and depth of your interactions.

- 🎨 **Image Generation Integration**: Seamlessly incorporate image generation capabilities using options such as AUTOMATIC1111 API or ComfyUI (local), and OpenAI's DALL-E (external), enriching your chat experience with dynamic visual content.

- ⚙️ **Many Models Conversations**: Effortlessly engage with various models simultaneously, harnessing their unique strengths for optimal responses. Enhance your experience by leveraging a diverse set of models in parallel.

- 🔐 **Role-Based Access Control (RBAC)**: Ensure secure access with restricted permissions; only authorized individuals can access your Ollama, and exclusive model creation/pulling rights are reserved for administrators.

- 🌐🌍 **Multilingual Support**: Experience Falcor in your preferred language with our internationalization (i18n) support. Join us in expanding our supported languages! We're actively seeking contributors!

- 🌟 **Continuous Updates**: We are committed to improving Falcor with regular updates, fixes, and new features.

Want to learn more about Falcor's features? Check out our [Falcor documentation](https://docs.Falcor.com/features) for a comprehensive overview!

## 🔗 Also Check Out Falcor Community!

Don't forget to explore our sibling project, [Falcor Community](https://Falcor.com/), where you can discover, download, and explore customized Modelfiles. Falcor Community offers a wide range of exciting possibilities for enhancing your chat interactions with Falcor! 🚀

## How to Install 🚀

### Installation via Python pip 🐍

Falcor can be installed using pip, the Python package installer. Before proceeding, ensure you're using **Python 3.11** to avoid compatibility issues.

1. **Install Falcor**:
   Open your terminal and run the following command to install Falcor:

   ```bash
   pip install Falcor
   ```

2. **Running Falcor**:
   After installation, you can start Falcor by executing:

   ```bash
   Falcor serve
   ```

This will start the Falcor server, which you can access at [http://localhost:8080](http://localhost:8080)

### Quick Start with Docker 🐳

> [!NOTE]  
> Please note that for certain Docker environments, additional configurations might be needed. If you encounter any connection issues, our detailed guide on [Falcor Documentation](https://docs.Falcor.com/) is ready to assist you.

> [!WARNING]
> When using Docker to install Falcor, make sure to include the `-v Falcor:/app/backend/data` in your Docker command. This step is crucial as it ensures your database is properly mounted and prevents any loss of data.

> [!TIP]  
> If you wish to utilize Falcor with Ollama included or CUDA acceleration, we recommend utilizing our official images tagged with either `:cuda` or `:ollama`. To enable CUDA, you must install the [Nvidia CUDA container toolkit](https://docs.nvidia.com/dgx/nvidia-container-runtime-upgrade/) on your Linux/WSL system.

### Installation with Default Configuration

- **If Ollama is on your computer**, use this command:

  ```bash
  docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v Falcor:/app/backend/data --name Falcor --restart always ghcr.io/dangerpotter/falcor:main
  ```

- **If Ollama is on a Different Server**, use this command:

  To connect to Ollama on another server, change the `OLLAMA_BASE_URL` to the server's URL:

  ```bash
  docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=https://example.com -v Falcor:/app/backend/data --name Falcor --restart always ghcr.io/dangerpotter/falcor:main
  ```

- **To run Falcor with Nvidia GPU support**, use this command:

  ```bash
  docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v Falcor:/app/backend/data --name Falcor --restart always ghcr.io/dangerpotter/falcor:cuda
  ```

### Installation for OpenAI API Usage Only

- **If you're only using OpenAI API**, use this command:

  ```bash
  docker run -d -p 3000:8080 -e OPENAI_API_KEY=your_secret_key -v Falcor:/app/backend/data --name Falcor --restart always ghcr.io/dangerpotter/falcor:main
  ```

### Installing Falcor with Bundled Ollama Support

This installation method uses a single container image that bundles Falcor with Ollama, allowing for a streamlined setup via a single command. Choose the appropriate command based on your hardware setup:

- **With GPU Support**:
  Utilize GPU resources by running the following command:

  ```bash
  docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v Falcor:/app/backend/data --name Falcor --restart always ghcr.io/dangerpotter/falcor:ollama
  ```

- **For CPU Only**:
  If you're not using a GPU, use this command instead:

  ```bash
  docker run -d -p 3000:8080 -v ollama:/root/.ollama -v Falcor:/app/backend/data --name Falcor --restart always ghcr.io/dangerpotter/falcor:ollama
  ```

Both commands facilitate a built-in, hassle-free installation of both Falcor and Ollama, ensuring that you can get everything up and running swiftly.

After installation, you can access Falcor at [http://localhost:3000](http://localhost:3000). Enjoy! 😄

### Other Installation Methods

We offer various installation alternatives, including non-Docker native installation methods, Docker Compose, Kustomize, and Helm. Visit our [Falcor Documentation](https://docs.Falcor.com/getting-started/) or join our [Discord community](https://discord.gg/5rJgQTnV4s) for comprehensive guidance.

### Troubleshooting

Encountering connection issues? Our [Falcor Documentation](https://docs.Falcor.com/troubleshooting/) has got you covered. For further assistance and to join our vibrant community, visit the [Falcor Discord](https://discord.gg/5rJgQTnV4s).

#### Falcor: Server Connection Error

If you're experiencing connection issues, it’s often due to the Falcor docker container not being able to reach the Ollama server at 127.0.0.1:11434 (host.docker.internal:11434) inside the container . Use the `--network=host` flag in your docker command to resolve this. Note that the port changes from 3000 to 8080, resulting in the link: `http://localhost:8080`.

**Example Docker Command**:

```bash
docker run -d --network=host -v Falcor:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name Falcor --restart always ghcr.io/dangerpotter/falcor:main
```

### Keeping Your Docker Installation Up-to-Date

In case you want to update your local Docker installation to the latest version, you can do it with [Watchtower](https://containrrr.dev/watchtower/):

```bash
docker run --rm --volume /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --run-once Falcor
```

In the last part of the command, replace `Falcor` with your container name if it is different.

Check our Migration Guide available in our [Falcor Documentation](https://docs.Falcor.com/tutorials/migration/).

### Using the Dev Branch 🌙

> [!WARNING]
> The `:dev` branch contains the latest unstable features and changes. Use it at your own risk as it may have bugs or incomplete features.

If you want to try out the latest bleeding-edge features and are okay with occasional instability, you can use the `:dev` tag like this:

```bash
docker run -d -p 3000:8080 -v Falcor:/app/backend/data --name Falcor --add-host=host.docker.internal:host-gateway --restart always ghcr.io/dangerpotter/falcor:dev
```

## What's Next? 🌟

Discover upcoming features on our roadmap in the [Falcor Documentation](https://docs.Falcor.com/roadmap/).

## Supporters ✨

A big shoutout to our amazing supporters who's helping to make this project possible! 🙏

### Platinum Sponsors 🤍

- We're looking for Sponsors!

### Acknowledgments

Special thanks to [Prof. Lawrence Kim](https://www.lhkim.com/) and [Prof. Nick Vincent](https://www.nickmvincent.com/) for their invaluable support and guidance in shaping this project into a research endeavor. Grateful for your mentorship throughout the journey! 🙌

## License 📜

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details. 📄

## Support 💬

If you have any questions, suggestions, or need assistance, please open an issue or join our
[Falcor Discord community](https://discord.gg/5rJgQTnV4s) to connect with us! 🤝

## Star History

<a href="https://star-history.com/#dangerpotter/falcor&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=dangerpotter/falcor&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=dangerpotter/falcor&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=dangerpotter/falcor&type=Date" />
  </picture>
</a>

---

Modified from Open WebUI for Capella University by [Timothy Jaeryang Baek](https://github.com/dangerpotter) - Let's make Falcor even more amazing together! 💪
