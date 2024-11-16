# 📝 Story Generator

An advanced **Story Generator** built with **Streamlit** and **LangChain** that crafts creative, detailed stories based on user-provided contexts. This project allows users to select story styles, emotions, and customize character details for an immersive storytelling experience.

---

## 🎯 Features

- **Dynamic Story Styles**: Choose from genres like Fantasy, Science Fiction, Mystery, and Romance.
- **Emotion Customization**: Generate stories with specific emotional tones (e.g., Romantic, Suspenseful, Tragic).
- **Character Personalization**: Define the main character's name and traits for unique, relatable stories.
- **Flexible Story Settings**:
  - **Themes**: Add optional story themes for richer narratives.
  - **Formats**: Switch between Narrative, Journal, Screenplay, or Dialogue formats.
  - **Settings**: Choose environments such as Modern, Fantasy, Historical, or Futuristic.
- **Streamlined Markdown Formatting**:
  - Headings for chapters and sections.
  - Paragraph breaks for readability.
- Powered by **LlamaCpp** for seamless large language model integration.

---

## 🛠️ Technology Stack

- **[Streamlit](https://streamlit.io/)**: Interactive web application framework.
- **[LangChain](https://www.langchain.com/)**: Framework for building language model applications.
- **LlamaCpp**: Lightweight LLM integration for local execution.
- **Python**: Core programming language.

---

## 🚀 How to Run

### Prerequisites

1. Install Python (>= 3.8).
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/story-generator.git
   cd story-generator
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
4. Download the Llama model (e.g., llama-2-7b-chat.Q8_0.gguf) and place it in an appropriate folder.
5. Start the Streamlit app:
   ```bash
   streamlit run app.py

