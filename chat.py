import openai
from logger import log
import speech_recognition as sr

# Set up the OpenAI API client
openai.api_key = "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"
log("chat",f"API KEY : {openai.api_key}")


# Initializing the Speech Recognition 
r = sr.Recognizer() 

# Set up the model and prompt
model_engine = "text-davinci-003"

try:
    while True:
        log("chat","Chat Started....")
        print("\n ======================QUESTION===========================")
        try:
            while True:
                print("\n Say Question ! Make sure your voice will be clear...")
                print("\n Listening.......")
                with sr.Microphone() as source :
                    audio = r.listen(source)
                
                text = r.recognize_google(audio) 
                log("chat",f"Question : \n {text}")
                # print("You said : {}".format(text)) 
                break
        except Exception as e:
            log("chat",f"Error while listening: {e}")
            # print(e)
            continue
        # Generate a response
        print("\n >>>>>>>>>>>>>>>>>>>>>> ⏳ Generating Response ⏳ >>>>>>>>>>>>>>>>>>>>>>")
        log("chat","Generating Response....")
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        log("chat",f"Answer : \n {response}")
        print(f"\n ======================ANSWER=========================== \n {response}")
        exit_msg = input("\n Do want to close? Y: "  )
        log("chat",f"Do want to close Y: {exit_msg}")
        if exit_msg == 'Y':
            log("chat","Closed")
            break
        else :
            continue
        
except Exception as e :
     log("chat",f"Error while execurting : {e}")
     print(e)

