# 🔐 Cryptography Visualizer

An interactive web application that demonstrates and visualizes classical cryptographic algorithms in a step-by-step manner. This project is designed to help users understand how encryption and decryption work behind the scenes.

---

## 📌 Overview

Cryptography can often feel complex and abstract. This project simplifies the learning process by visually representing how different algorithms transform plain text into encrypted text and back again.

It is especially useful for students, beginners, and anyone interested in understanding the fundamentals of encryption.

---

## 🚀 Features

* 🔑 Support for multiple cryptographic algorithms:

  * Caesar Cipher
  * Rail Fence Cipher
  * Vigenere cipher
  * Playfair Cipher
  * Hill Cipher

* 🔍 Step-by-step visualization of encryption process

* 🔄 Encryption and Decryption functionality

* 🔢 Matrix and pattern-based representation (for algorithms like Rail Fence)

* 🧠 Algorithm explanation section

* 🎨 User-friendly interface with Bootstrap

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, Bootstrap
* **Logic Layer:** Custom Python implementations of cryptographic algorithms
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```id="r7l8m2"
cryptography-visualizer/
│
├── app.py
├── algo.py
├── templates/
│   ├── index.html
├── static/
│   ├── css/
│   └── js/
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```id="g4yq2d"
git clone https://github.com/your-username/cryptography-visualizer.git
cd cryptography-visualizer
```

### 2️⃣ Create virtual environment

```id="p1m9xk"
python -m venv venv
```

### 3️⃣ Activate virtual environment

**Windows:**

```id="a2k8d1"
venv\Scripts\activate
```

**Mac/Linux:**

```id="l9s3vd"
source venv/bin/activate
```

### 4️⃣ Install dependencies

```id="u8n2fp"
pip install -r requirements.txt
```

### 5️⃣ Run the application

```id="z6w4jc"
python app.py
```

### 6️⃣ Open in browser

```id="q3t8vy"
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User selects a cryptographic algorithm
2. Inputs plain text and required parameters (e.g., shift, key)
3. The system processes the input using algorithm logic in `algo.py`
4. Step-by-step transformation is displayed
5. Final encrypted or decrypted result is shown

---

## 📸 Screenshots

* Input form
  <img width="1780" height="819" alt="image" src="https://github.com/user-attachments/assets/3f07d387-4e2d-47c8-875e-1928c50e8bdf" />

* Step-by-step visualization
  <img width="1739" height="504" alt="image" src="https://github.com/user-attachments/assets/c16e5b6e-1d1a-41c0-aeb4-a69eee290836" />

* Final result
  <img width="1765" height="578" alt="image" src="https://github.com/user-attachments/assets/215c1207-2357-4bd2-bb74-1fc4cf397baf" />

---

## 🔮 Future Improvements

* Add more algorithms ( AES basics, DES basics)
* Add animation for step visualization
* Export results as PDF
* Improve UI/UX with modern design
* Add user authentication to save history

---

## 🎯 Learning Objectives

* Understand core concepts of classical cryptography
* Implement algorithms from scratch
* Visualize abstract concepts in a practical way
* Build logic-driven web applications using Flask

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and improve the project.

---

## 📬 Contact

* GitHub: https://github.com/arbaz-mudassar
* Email: [arbazmudassar@gmail.com](mailto:arbazmudassar0@gmail.com)

---

⭐ If you found this project useful or interesting, consider giving it a star!
