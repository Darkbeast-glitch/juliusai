import openai
import streamlit as st
import config


st.title("JuliusAI + ChatGPT")

st.sidebar.header("How i was made")
st.sidebar.info('''This is a web application that provides users with an interactive platform to engage with the OpenAI API's implementation of the ChatGPT model. The application has been developed by Julius Boakye, a skilled software engineer from Ghana, who has created his own implementation of the ChatGPT.

Users of the application are prompted to enter a query into the text box and then press enter to receive a response generated by the ChatGPT model. The user interface has been designed to be intuitive and user-friendly, with clear instructions to guide users through the process.

Overall, this web application is a powerful tool that leverages cutting-edge natural language processing technology to provide users with a seamless and engaging experience. Its intuitive design and powerful functionality make it a valuable resource for anyone interested in exploring the capabilities of the ChatGPT model.''')

# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
# follow step 4 to get a secret_key
openai.api_key = config.api_key


def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input(
        "Enter query here, to exit enter :q", "Is investing in crypto currency the future?")
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query)
        return st.write(f"{user_query} {response}")


def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=user_query,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response


# call the main function
main()
