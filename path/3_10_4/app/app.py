import os

import gradio as gr
import numpy as np
import torch
from lavis.models import load_model_and_preprocess
from PIL import Image

device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_opt", model_type="pretrain_opt2.7b", is_eval=True, device=device
)


def generate_caption(image, caption_type):
    image = vis_processors["eval"](image).unsqueeze(0).to(device)

    if caption_type == "Beam Search":
        caption = model.generate({"image": image})
    else:
        caption = model.generate(
            {"image": image}, use_nucleus_sampling=True, num_captions=3
        )

    caption = "\n".join(caption)

    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    return caption


def chat(input_image, question, history):
    history = history or []
    question = question.lower()

    image = vis_processors["eval"](input_image).unsqueeze(0).to(device)

    clean = lambda x: x.replace("<p>", "").replace("</p>", "").replace("\n", "")
    clean_h = lambda x: (clean(x[0]), clean(x[1]))
    context = list(map(clean_h, history))
    template = "Question: {} Answer: {}."
    prompt = (
        " ".join(
            [template.format(context[i][0], context[i][1]) for i in range(len(context))]
        )
        + " Question: "
        + question
        + " Answer:"
    )

    response = model.generate({"image": image, "prompt": prompt})
    history.append((question, response[0]))

    return history, history


def clear_chat(history):
    return [], []


with gr.Blocks() as demo:
    gr.Markdown(
        "### BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
    )
    gr.Markdown(
        "This demo uses the `pretrain_opt2.7b` weights. For more information please visit [Github](https://github.com/salesforce/LAVIS/tree/main/projects/blip2) or [Paper](https://arxiv.org/abs/2301.12597)."
    )

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Image", type="pil")
            caption_type = gr.Radio(
                ["Beam Search", "Nucleus Sampling"],
                label="Caption Decoding Strategy",
                value="Beam Search",
            )
            btn_caption = gr.Button("Generate Caption")
            output_text = gr.Textbox(label="Answer", lines=5)

        with gr.Column():
            chatbot = gr.Chatbot().style(color_map=("green", "pink"))
            chat_state = gr.State()

            question_txt = gr.Textbox(label="Question", lines=1)
            btn_answer = gr.Button("Generate Answer")
            btn_clear = gr.Button("Clear Chat")

    btn_caption.click(
        generate_caption, inputs=[input_image, caption_type], outputs=[output_text]
    )

    btn_answer.click(
        chat,
        inputs=[input_image, question_txt, chat_state],
        outputs=[chatbot, chat_state],
    )

    btn_clear.click(clear_chat, inputs=[chat_state], outputs=[chatbot, chat_state])

    gr.Examples(
        [
            ["./merlion.png", "Beam Search", "which city is this?"],
            [
                "./Blue_Jay_0044_62759.jpg",
                "Beam Search",
                "what is the name of this bird?",
            ],
            ["./5kstbz-0001.png", "Beam Search", "where is the man standing?"],
            [
                "ILSVRC2012_val_00000008.JPEG",
                "Beam Search",
                "Name the colors of macarons you see in the image.",
            ],
        ],
        inputs=[input_image, caption_type, question_txt],
    )

    gr.Markdown(
        "Sample images are taken from [ImageNet](https://paperswithcode.com/sota/image-classification-on-imagenet), [CUB](https://paperswithcode.com/dataset/cub-200-2011) and [GamePhysics](https://asgaardlab.github.io/CLIPxGamePhysics/) datasets."
    )

demo.launch()
