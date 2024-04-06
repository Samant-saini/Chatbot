import openai
import gradio as gr

openai.api_key = "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"




messages = [{"role": "system", "content": "You are a tour guide that specializes in giving adive for the tour visit"}]


def CustomChatGPT(location,duration):
    



    messages.append({"role": "user", "content": f"I want to visit {location} for {duration} days"})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

location= gr.Button("hello")
duration= gr.Textbox(label="No of days")
btn = gr.Button(value="Submit")
#location_radio = gr.Radio(["Manali", "Shimla"], label="Select Location", default=None, name="location", horizontal=True)
#duration_radio = gr.Radio(["2 days", "5 days"], label="Select Duration", default=None, name="duration", horizontal=True)


demo = gr.Interface(fn=CustomChatGPT,
                    inputs=[location, duration], 
                    outputs = "text",
                      title = " Your Tour guide")

demo.launch(share=True)