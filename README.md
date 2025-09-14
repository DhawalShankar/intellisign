# IntelliSign: Sign Language to Text Converter  
*Bridging Communication Gaps with AI and IoT*  

## 📌 Overview  
**IntelliSign** is a low-cost, AI-powered assistive technology designed to convert **American Sign Language (ASL) gestures into text** in real time.  
It empowers the deaf and hard-of-hearing community by enabling spontaneous, natural, and inclusive communication.  

Key features:  
- 🔹 Real-time gesture-to-text conversion  
- 🔹 Low-cost and portable IoT hardware (Raspberry Pi + I2C LED display)  
- 🔹 AI-powered gesture recognition using **Computer Vision + CNN**  
- 🔹 Optional **LLM (Gemini API) integration** for natural sentence formation  

---

## 🚀 Motivation  
Millions of hearing and speech-impaired individuals face daily communication barriers.  
Existing solutions are either **too costly**, **not portable**, or **lack real-time accuracy**.  

**IntelliSign** addresses this by offering:  
- Affordable accessibility  
- Real-time spontaneous communication  
- Inclusivity in education, healthcare, and workplaces  

---

## 🛠️ Technical Approach  

### Pipeline  
1. **Image Preprocessing** → Grayscale, Thresholding, Gaussian Blur  
2. **Feature Extraction & Recognition** → CNN-based classification  
3. **Gesture Mapping** → Map recognized gestures to ASL letters  
4. **Sentence Formation (Optional)** → LLM/Gemini API for fluent sentences  
5. **Hardware Integration** → Raspberry Pi + I2C LED display  

---

## ⚙️ Project Structure  
```bash
IntelliSign/
│── data/ # Training & testing datasets
│ ├── train/
│ ├── test/
│ └── labels.csv
│
│── models/ # Saved trained models
│ ├── cnn_model.pkl
│ └── cnn_model.h5
│
│── src/
│ ├── preprocess.py # Preprocessing scripts
│ ├── train.py # Model training
│ ├── predict.py # Real-time prediction pipeline
│ └── utils.py # Helper functions
│
│── hardware/ # IoT hardware integration
│ ├── raspberry_pi_setup/
│ └── display_driver.py
│
│── results/ # Model performance results
│ ├── accuracy_plots.png
│ └── confusion_matrix.png
│
│── docs/ # Documentation
│ ├── synopsis.tex
│ └── report.pdf
│
└── README.md
```
---

## 📊 Dataset & Evaluation  
- **Custom dataset** collected via laptop webcam for real-world relevance  
- Preprocessing: grayscale, thresholding, Gaussian blur  
- **Expected accuracy:** 70–80% on self-collected dataset  
- Dataset split: 70% train, 15% validation, 15% test  

---

## 💡 Key Advantages  
- ✅ Real-time gesture recognition  
- ✅ Affordable & portable  
- ✅ Natural sentence construction with LLM  
- ✅ Inclusive across education, healthcare, and workplaces  

---

## 🌍 Applications & Future Enhancements  
- **Education:** Assistive tool in classrooms  
- **Healthcare:** Doctor-patient seamless communication  
- **Workplaces:** Inclusive team collaboration  

**Planned enhancements:**  
- Multi-language sign support (ISL, BSL, etc.)  
- Text-to-Speech integration for two-way communication  
- Mobile app for broader accessibility  
- Advanced gesture recognition with temporal modeling  

---

## 🔑 Getting Started  

### 1. Clone Repository  
```bash
git clone https://github.com/DhawalShankar/IntelliSign.git
cd IntelliSign
```
### 2. Setup Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3. Run Prediction
```bash
python src/predict.py
```
### 4. Run with Gemini API (Optional)

Add your Gemini API key in .env
```bash
GEMINI_API_KEY=your_key_here
```

📝 Conclusion

IntelliSign is more than a project — it is a step toward building an inclusive society by bridging the communication gap for millions.
By combining AI, Computer Vision, and IoT, we aim to inspire innovation in assistive technologies and create a world where everyone can communicate freely.
