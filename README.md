# MedGemma Proof of Concept

This project is a Proof of Concept (PoC) demonstrating the use of Google's `google/medgemma-4b-it` multimodal model for analyzing chest X-ray images.

The script loads the model, processes a local X-ray image (`xray.jpg`), and generates a text-based report of the findings.

## Project Structure

```
medgemma-poc/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── app.py
└── xray.jpg```

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR-USERNAME/medgemma-poc.git
    cd medgemma-poc
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Authenticate with Hugging Face:**
    To access the `medgemma` model, you must accept the terms on the [model's page](https://huggingface.co/google/medgemma-4b-it) and log in via the terminal.
    ```bash
    huggingface-cli login
    ```
    Paste your access token when prompted (a token with "read" permissions is sufficient).

## Usage

After completing the setup, run the main script:
```bash
python app.py
```

### Example Execution and Output

The script will first show logs for loading the model and then print the generated analysis.

```bash
(venv) (base) splekhov@minikube:~/medgemma-poc$ python app.py
Loading model and processor...
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████| 2/2 [00:00<00:00,  2.53it/s]
Model and processor loaded successfully.
Preparing data for the model...
Generating response...

--- Model Response ---
Based on the chest X-ray provided, here are some general observations:

*   **Lung Fields:** The lung fields appear clear, with no obvious consolidation, infiltrates, or masses.
*   **Heart Size:** The heart size appears within normal limits.
*   **Mediastinum:** The mediastinum (the space between the lungs containing the heart, great vessels, trachea, etc.) appears unremarkable.
*   **Bones:** The ribs and clavicles appear intact.
*   **Diaphragm:** The diaphragms are well-defined.

**Important Considerations:**

*   **This is a limited assessment:** A proper interpretation requires a radiologist's expertise and consideration of the patient's clinical history, symptoms, and other relevant information.
*   **Image Quality:** The image quality is adequate for a general assessment, but subtle findings might be missed.
*   **Other Findings:** There are no obvious signs of pneumothorax, pleural effusion, or other significant abnormalities.

**Disclaimer:** I am an AI and cannot provide medical diagnoses. This information is for general knowledge and informational purposes only, and does not constitute medical advice. It is essential to consult with a qualified healthcare professional for any health concerns or before making any decisions related to your health or treatment.
----------------------
```

## Disclaimer

This project is a technical demonstration and is not intended for medical use. AI-generated descriptions should not be considered a medical diagnosis. Always consult with a qualified healthcare professional.