
import requests
import torch
from PIL import Image
from io import BytesIO

from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers.image_utils import load_image
import os
import json
import time
import random


processor = AutoProcessor.from_pretrained("TIGER-Lab/Mantis-8B-Idefics2") # do_image_splitting is False by default
model = AutoModelForVision2Seq.from_pretrained(
    "TIGER-Lab/Mantis-8B-Idefics2",
    device_map="auto"
)
generation_kwargs = {
    "max_new_tokens": 1024,
    "num_beams": 1,
    "do_sample": False
}







def call_mantis(image_paths,question):
    # Note that passing the image urls (instead of the actual pil images) to the processor is also possible
    images = []
    try:
        for image_path in image_paths:
            image = load_image(image_path)
            images.append(image)
    except Exception as e:
        print(e)
        return 'image error'
    
    content_list = []
    for i in range(len(images)):
        content_list.append({"type": "image"})
    content_list.append({"type": "text", "text": question})


    messages = [
        {
            "role": "user",
            "content": content_list
        }    
    ]

    try:
        prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
        inputs = processor(text=prompt, images=images, return_tensors="pt")
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

        # Generate
        generated_ids = model.generate(**inputs, **generation_kwargs)
        response = processor.batch_decode(generated_ids[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        print("ASSISTANT: ", response[0])
        return response[0]
    except Exception as e:
        print(e)
        print('model error')
        return 'model error'


json_path = 'all.json'

tasks_exist = ['person_reid', 'multiple_image_captioning', 'spot_the_similarity', 'face_retrieval', 'sketch2image_retrieval', 'handwritten_retrieval', 'spot_the_diff', 'image2image_retrieval', 'vehicle_retrieval', 'text2image_retrieval',
'general_action_recognition', 'video_captioning', 'next_img_prediction', 'temporal_ordering', 'meme_vedio_understanding', 'action_quality_assessment', 'temporal_localization', 'mevis',
'ravens_progressive_matrices', 'threed_indoor_recognition', 'point_tracking', 'threed_cad_recognition', 'single_object_tracking']
with open(json_path,'r') as f:
    data_all = json.load(f)

result = []



for modelname in models:
    output_dir = os.path.join('./result')

    output_dir = os.path.join(output_dir,modelname)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir,'metadata_info.json')

    for task_data in data_all:
       
        context = task_data["context"]
        question = task_data["question"]
        
        tmp = []
        image_flag = True
        
        for image_path in task_data["input_image_path"]:
            
            tmp.append(image_path)
            if not os.path.exists(image_path):
                image_flag = False
                break
        
        if image_flag == False:
            response = 'image none'
            task_data[modelname] = response
            print(modelname, task,len(tmp), ': ',response)
            result.append(task_data)
            continue



        try:
            
            if task_data['task'] in tasks_exist:
                question = question + '\n' + context
            else:
                question = context + '\n' + question
            question = question + '\nPlease answer the option directly like A,B,C,D...'

            response = call_mantis(tmp,question)
            task_data[modelname] = response
            print(modelname, task,len(tmp), ': ',response)
        except:
            response = 'model error or image error'
            task_data[modelname] = response
            print(modelname, task,len(tmp),': ',response)
        result.append(task_data)
        
        

    with open(output_path,'w') as f:
        json.dump(result,f)







