
from vlmeval.config import supported_VLM
import os
import json

# transformers == 33.0
# ['XComposer2','XComposer2_1.8b','qwen_base','idefics_9b_instruct','qwen_chat', 'flamingov2']


# transformers == 37.0
# ['deepseek_vl_1.3b','deepseek_vl_7b']

# transformers == 40.0
# ['idefics2_8b']


models = ['XComposer2','XComposer2_1.8b','qwen_base','idefics_9b_instruct','qwen_chat', 'flamingov2']
json_path = 'all.json'

tasks_exist = ['person_reid', 'multiple_image_captioning', 'spot_the_similarity', 'face_retrieval', 'sketch2image_retrieval', 'handwritten_retrieval', 'spot_the_diff', 'image2image_retrieval', 'vehicle_retrieval', 'text2image_retrieval',
'general_action_recognition', 'video_captioning', 'next_img_prediction', 'temporal_ordering', 'meme_vedio_understanding', 'action_quality_assessment', 'temporal_localization', 'mevis',
'ravens_progressive_matrices', 'threed_indoor_recognition', 'point_tracking', 'threed_cad_recognition', 'single_object_tracking']
with open(json_path,'r') as f:
    data_all = json.load(f)

result = []



for modelname in models:
    model = supported_VLM[modelname]()
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
            tmp.append(question)
            response = model.generate(tmp)
            task_data[modelname] = response
            print(modelname, task,len(tmp), ': ',response)
        except:
            response = 'model error or image error'
            task_data[modelname] = response
            print(modelname, task,len(tmp),': ',response)
        result.append(task_data)
        
        

    with open(output_path,'w') as f:
        json.dump(result,f)







