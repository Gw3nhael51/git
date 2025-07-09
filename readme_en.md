# 🎲 Python Dice Roll Generator

This mini-script simulates a classic dice roll (1 to 6) using Python's `random` module.

---

## 🔍 Example Code

```python
import random

# Generate a number between 1 and 6 like a dice
random_integer = random.randint(1, 6)
print(f"Dice result: {random_integer}")
```

---

## 🐍 Activate Python Environment

Open the terminal in your project directory: `*/your_project_name/git/`  
Type the command: `./py_env_3.11/Scripts/activate` to activate the Python environment.  
Check the Python version: `python --version` (should display version 3.11.8)

---

## ▶️ Run the Python Script

Once the environment is activated, you can run the dice roll script. Navigate to the folder containing your file (e.g., `test.py`) and type the following command in the terminal:

```bash
python test.py
```

You should see a random result between 1 and 6, for example:

```
Dice result: 4
```

---

## 📝 Code Explanation

- `import random`: imports the Python module for generating random numbers.
- `random.randint(1, 6)`: generates a random integer between 1 and 6 (inclusive), simulating a classic dice roll.
- `print(f"Dice result: {random_integer}")`: displays the dice roll result in the terminal.

---

## 🛠️ Troubleshooting Tips

- If the `python` command does not work, try `python3`.
- Make sure the virtual environment is activated (the terminal prompt should change).
- If you get an error about the `random` module, ensure you are using a standard Python installation (the module is included by default).

---

## 📚 Going Further

- Try modifying the script to roll multiple dice at once.
- Add a loop to let the user roll the dice as many times as they want.
- Explore other modules from the Python standard library to enhance your script.
