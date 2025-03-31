# [MCP URL2SNAP](https://anthropic-mcp.hashnode.dev/model-context-protocol-mcp-a-beginners-guide-to-the-future-of-ai-communication) 🚀🤖

[![smithery badge](https://smithery.ai/badge/@Abhi5h3k/MCP-URL2SNAP)](https://smithery.ai/server/@Abhi5h3k/MCP-URL2SNAP)

A lightweight **Model Context Protocol (MCP)** server that enables your LLM to capture screenshots of any specified URL and return only the access URL for the captured image. This tool simplifies the process of generating and sharing webpage snapshots, making it perfect for integrating visual capture capabilities into AI applications like Claude Desktop or automation workflows.

---

# What is Model Context Protocol (MCP)?
At its core, MCP is a standardized protocol designed to streamline communication between AI models and external systems. Think of it as a universal language that allows different AI agents, tools, and services to interact seamlessly.

![MCP drawio (1)](https://github.com/user-attachments/assets/567c5853-3e3c-49c5-bec2-07325f000be2)

---

## **Features**  
- **Email Verification**: Verify email addresses in real-time.  
- **MCP Integration**: Seamlessly connect with MCP-compatible LLMs.  
- **Easy Setup**: Built with Python and the MCP SDK for quick deployment.  

---

# MCP follows a client-server architecture:

![client server drawio](https://github.com/user-attachments/assets/1f7141c9-d96f-4a5d-a8ab-944b8daa81f4)

---

# Watch the Demo
Click the image below to watch a video demo of the MCP Email Verify tool in action:

[![Youtube](https://github.com/user-attachments/assets/c3c05d3d-aac8-4d6b-a8ce-6dd0aec935f2)](https://youtu.be/Xv1YA5pXdqY)

---

## **Requirements**  
- **Python**: Python 3.11.0 or higher.  
- **UV**: 0.6.9 or higher.  

---
## **Setup**  

### Installing via Smithery

To install MCP-URL2SNAP for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@Abhi5h3k/MCP-URL2SNAP):

```bash
npx -y @smithery/cli install @Abhi5h3k/MCP-URL2SNAP --client claude
```

### Manual Installation
**1. Clone the Repository**  
```
git clone https://github.com/Abhi5h3k/MCP-URL2SNAP.git
cd MCP-URL2SNAP
```
**2. Install UV**
 
If you don’t have UV installed, you can install it using the following commands:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify the installation:
```
uv --version
```

**3. Set Up the Virtual Environment**

Create a virtual environment using UV:
```
uv venv
```
Activate the virtual environment:
On Windows:
```
.venv\Scripts\activate
```
**4. Install Dependencies** 
Install the required dependencies from pyproject.toml using UV:
```
uv install
```

## Running the Server
1. Set Up Environment Variables
Create a .env file in the root directory and add your [AbstractAPI](https://app.abstractapi.com/api/screenshot/tester) key:
```
ABSTRACT_API_KEY=your_api_key_here
```
2. Run the Server
Start the MCP server:
```
uv run server.py
```

## Usage

1. Register the Server with Claude Desktop
  Update the claude_desktop_config.json file to include your MCP server:
  
  ```
  {
      "mcpServers": {
          "verify_mail": {
              "command": "uv",
              "args": [
                  "--directory",
                  "C:\\ABSOLUTE\\PATH\\TO\\MCP-Email-Verify",
                  "run",
                  "server.py"
              ],
              "env":{
                "ABSTRACT_API_KEY":"YUR_API_KEY"
              }
          }
      }
  }
  ```
 ![image](https://github.com/user-attachments/assets/62db4fb4-d71a-49b5-97b8-9fbf4d4ab822)
 
 ![image](https://github.com/user-attachments/assets/da77ff7c-82cd-4ef8-94fd-ce9b11cad83f)


2. Restart Claude Desktop
  Restart Claude Desktop to detect the new tool.

3. Verify Emails
  Use prompts like:

  "can you show me the screenshot of https://github.com/Abhi5h3k"


## Development
Formatting and Linting
This project uses black and isort for code formatting and import sorting.

1. Install development dependencies:
   ```
    uv add black isort --dev
    ```
2. Format the code:
   ```
   black .
   ```
3. Sort imports:
  ```
    isort .
  ```


## Set up pre-commit
```bash
pre-commit install
pre-commit run --all-files
```


Article: Model Context Protocol (MCP): [A Beginner's Guide to the Future of AI Communication](https://anthropic-mcp.hashnode.dev/model-context-protocol-mcp-a-beginners-guide-to-the-future-of-ai-communication)
