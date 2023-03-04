import openai
from logger import log

# Set up the OpenAI API client
openai.api_key = "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"
log("chat",f"API KEY : {openai.api_key}")

# Set up the model and prompt
model_engine = "text-davinci-003"
# chat = ""
while True:
    log("chat","Chat Started....")
    print("======================QUESTION===========================")
    prompt = input("Enter your msg : \n ")
    log("chat",f"Question : \n {prompt}")
    
    # Generate a response
    print(">>>>>>>>>>>>>>>>>>>>>> ⏳ Generating Response ⏳ >>>>>>>>>>>>>>>>>>>>>>")
    print("\n")
    log("chat","Generating Response....")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    log("chat",f"Answer : \n {response}")
    print(f"======================ANSWER=========================== \n {response}")



    exit_msg = input("Do want to close? Y: "  )
    log("chat",f"Do want to close Y: {exit_msg}")
    if exit_msg == 'Y':
        log("chat","Closed")
        break
    else :
        continue
        


