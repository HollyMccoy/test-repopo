# Word Finder

This project contains a Python script (`main.py`) that finds valid English words from a set of 7 letters. It uses the `nltk` library for its word list.

## Setup

To run this project, it is recommended to use a Python virtual environment to avoid issues with system-wide package installations.

1.  **Create a virtual environment:**
    Open a terminal in the project root and run:
    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**
    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3.  **Install dependencies:**
    With the virtual environment active, install the required packages from `requirements.txt`. Using `python -m pip` is a more robust way to ensure you're using the `pip` from your virtual environment.
    ```bash
    python -m pip install -r requirements.txt
    ```

4.  **Run the script:**
    ```bash
    python main.py
    ```
    The first time you run it, `nltk` may need to download its 'words' corpus.

## Troubleshooting

If you encounter errors during installation (`pip install`), here are a few things to try:

- **Ensure Virtual Environment is Active:** Make sure your command prompt or terminal shows the name of the virtual environment (e.g., `(venv)`) at the beginning of the line. If not, re-run the activation command from step 2.

- **Upgrade Pip:** An outdated version of `pip` can cause issues. Upgrade it with the following command:
  ```bash
  python -m pip install --upgrade pip
  ```

- **Windows Execution Policy:** On Windows, you might need to change the PowerShell execution policy to run the activation script. You can do this by running PowerShell as an administrator and executing:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
  ```

- **Antivirus/Permissions:** The `WinError` you saw previously can sometimes be caused by antivirus software locking files. Try temporarily disabling your antivirus or running the command prompt as an administrator.
