AI Security Testing Platform
A Python-based project for testing the security behavior of Large Language Models (LLMs) against common prompt-based attacks.
Features
- Prompt Injection testing
- Jailbreak response testing
- System Prompt Exposure testing
- JSON-based test cases
- Automated response verification
- Timestamped JSON test reports
- Local LLM testing through Ollama
Note: The currently implemented features depend on the modules and test cases present in your local project. Sensitive Data Disclosure, Cross-User Data Access, and Excessive Agency should be marked as planned until their implementations are complete.

Project Structure
AI_Security_Testing_Platform/
├── main.py
├── configuration.py
├── attacks.py
├── target_client.py
├── verification.py
├── requirements.txt
├── test_data/
│   └── prompts/
│       ├── prompt_injection.json
│       ├── jailbreak.json
│       └── system_prompt_exposure.json
└── results/
Your actual folder structure may contain additional files or folders.
Requirements
- Python 3.10 or later recommended
- Ollama installed and running locally
- A model downloaded in Ollama, such as llama3.2:3b
- Python dependencies listed in requirements.txt
Setup
1. Clone the repository
Replace YOUR_GITHUB_USERNAME with your GitHub username:
git clone https://github.com/YOUR_GITHUB_USERNAME/Security-Testing-Platform.git
cd Security-Testing-Platform
2. Create a virtual environment (recommended)
Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
If PowerShell blocks activation, you can use Command Prompt activation instead:
.venv\Scripts\activate.bat
3. Install dependencies
python -m pip install -r requirements.txt
4. Start Ollama and download the model
Install Ollama from ollama.com, then run:
ollama pull llama3.2:3b
Make sure Ollama is running and the model name and endpoint in your project configuration match your local setup. The endpoint used in this project context is:
http://localhost:11434/api/chat
5. Run the platform
From the project root:
python main.py
Follow the prompts in the terminal to select and run a supported attack test.
Test Results
Test results are written as timestamped JSON files under the results/ directory, if configured in your current version. Reports include test identifiers, evaluation status, expected behavior, and model responses.

Typical statuses:
- Pass — the response met the verifier's expected safety criteria.
- Fail — the verifier detected behavior classified as unsafe.
- Inconclusive — the automated checks could not confidently determine the result.
Automated, keyword-based checks are heuristics. Review inconclusive results and validate important findings manually; a Pass does not prove that a model is secure.
Current Scope and Planned Work
Potential future modules include:
- Sensitive Data Disclosure
- Cross-User Data Access
- Excessive Agency
- More robust evaluation and regression tests
Only describe a module as implemented after its test data, routing, and verification logic are working together.
Security Notes
- Do not commit API keys, passwords, .env files, private datasets, or real sensitive information.
- Use dummy canary values and controlled test data for disclosure testing.
- Review generated reports before publishing them; they may contain prompts or model responses.
- Use this platform only on systems and models you own or are authorized to test.
Contributing
Contributions and suggestions are welcome. Open an issue to discuss bugs, test cases, or improvements before submitting substantial changes.
License
No license has been specified yet. Until a license is added, do not assume others have permission to reuse, modify, or distribute this project.