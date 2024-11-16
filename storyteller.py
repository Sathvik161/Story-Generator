import streamlit as st
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from random import choice

# Streamlit app title
st.title("Enhanced Story Generator")

# Sidebar for story settings
st.sidebar.title("Story Settings")
story_style = st.sidebar.radio("Choose Story Style", ["Fantasy", "Science Fiction", "Mystery", "Romance"], index=0)
emotion = st.sidebar.selectbox("Choose Emotion", ["Adventurous", "Romantic", "Suspenseful", "Tragic"])
theme = st.sidebar.text_input("Enter a Theme (optional)", "")
setting = st.sidebar.selectbox("Choose Setting", ["Modern", "Fantasy", "Historical", "Futuristic"])

# Character settings
st.sidebar.title("Character Settings")
character_name = st.sidebar.text_input("Main Character's Name", "Sathvik")
character_traits = st.sidebar.multiselect("Character Traits", ["brave", "kind", "cautious", "intelligent", "adventurous"], default=["brave"])

# Story format and style
st.sidebar.title("Story Format & Style")
story_format = st.sidebar.selectbox("Story Format", ["Narrative", "Journal", "Screenplay", "Dialogue"])
style = st.sidebar.radio("Writing Style", ["Standard", "Poetic", "Epic"], index=0)

# Map story styles to prompts
story_prompts = {
    "Fantasy": "Write a creative and detailed fantasy story based on the following idea:",
    "Science Fiction": "Generate an immersive science fiction story with intricate details based on this idea:",
    "Mystery": "Create a suspenseful mystery story with plot twists based on this idea:",
    "Romance": "Write a heartfelt romance story inspired by this idea:",
}

# Prompt template with placeholders for all features
template = f"""{story_prompts.get(story_style, "")}
Context: {{context}}
Main Character: {character_name} - Traits: {', '.join(character_traits)}
Emotion: {emotion}
Theme: {theme or 'General'}
Setting: {setting}
Story Format: {story_format}
Writing Style: {style}

COMPLETE STORY:
"""

# Initialize LLM
callback = CallbackManager([StreamingStdOutCallbackHandler()])
llm = LlamaCpp(
    model_path="your llama path",
    temperature=1,
    n_gpu_layers=50,
    n_batch=4096,
    n_ctx=4096,
    max_tokens=3000,
    callback_manager=callback,
    verbose=True
)

# Set up prompt template and chain
prompt = PromptTemplate(template=template, input_variables=["context"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Function to generate a story with formatted output
def generate_story(context):
    result = llm_chain({"context": context})
    story_text = result.get("text", "No story generated.")
    
    # Formatting the story text with Markdown syntax
    # Assume any line that ends with ':' or has 'Chapter' is a heading, and use Markdown for styling
    formatted_story = ""
    for line in story_text.splitlines():
        if line.strip().endswith(":") or "Chapter" in line:
            formatted_story += f"### {line}\n"  # Make heading-level formatting for chapters
        else:
            formatted_story += f"{line}\n\n"   # Double newline for paragraph breaks

    return formatted_story

# Input section for story context
context = st.text_area("Enter the context or idea for your story:")

# Generate story button
if st.button("Generate Story"):
    if context:
        story = generate_story(context)
        st.write("Generated Story:")
        st.markdown(story)  # Render formatted story with Markdown
    else:
        st.warning("Please provide a context or idea for the story.")
