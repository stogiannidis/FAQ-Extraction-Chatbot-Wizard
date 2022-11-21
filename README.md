# FAQ Generation Wizard!

This repo contains all the work for Team Helvia Labs contribution in Cohere's Thanksgiving Hackathon <br>
&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;&ensp;&thinsp;[View Streamlit Demo](https://faq-extraction-wizard.streamlit.app/)

## How it works

Our app receives an input url to a website.
Then, it scrapes all text from the URL and uses cohere's generate model in order to generate frequently asked questions from the scraped text


## How to use
 
```
pip install requirements.txt
streamlit app.py
```
Please note that in order for the app to run you need access to an API key which you need to provide in 
the chatbot_creation_wizard.py file <br>
Hence, the change you have to make is:

```
api_key = st.secrets["COHERE_API_KEY"]
```
to 
```
api_key = your_api_key
```
