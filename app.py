import streamlit as st
import language_tool_python

# Initialize the language tool
tool = language_tool_python.LanguageTool('en-US')

# Streamlit application start
def main():
    st.title('Essay Grammar and Rubric Rating App')

    # Text area for user to paste essay
    essay_text = st.text_area("Paste your essay here:", height=300)
    
    if st.button('Check Essay'):
        # Check the essay text for grammar
        matches = tool.check(essay_text)
        grammar_score = max(0, 20 - len(matches))  # Example scoring function for grammar

        # Custom rubric scoring (placeholders for now)
        clarity_score = st.slider('Rate the essay for clarity and structure:', 0, 20, 10)
        argument_score = st.slider('Rate the essay for argument strength and evidence:', 0, 20, 10)
        style_score = st.slider('Rate the essay for style and voice:', 0, 20, 10)
        prompt_adherence_score = st.slider('Rate the essay for adherence to the prompt:', 0, 20, 10)

        # Calculate total score
        total_score = grammar_score + clarity_score + argument_score + style_score + prompt_adherence_score
        st.write(f'Your total essay score is: {total_score}/100')

        # Display grammar suggestions
        if matches:
            st.subheader('Grammar suggestions for improvement:')
            for match in matches:
                st.write(f"{match.ruleId}: {match.message}")

if __name__ == "__main__":
    main()