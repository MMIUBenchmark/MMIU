import requests
import time

url = "xx" # 替换为实际的API接口（API）
api_key = "InternVL-2-Pro_da046f58b9adc971c2a9f002d8ad4e5704cadf76161268db240bf3afea8b9d78_gI8iJTcO"  # 替换为实际生成的API密钥（KEY）


# high-level obj
context = "You are given a GUI navigation task that includes current screenshot images, historical screenshot images, and corresponding actions, where the last image represents the current screenshot and the preceding images are historical screenshots. The task is: Open the Firefox Browser to search for the best video blogs on travel vlogs. Then, go to the Setting app to turn up the brightness on your phone.\nThe historical actions are: step 1: CLICK: (603, 801)\nstep 2: CLICK: (190, 427)\nstep 3: CLICK: (834, 565)\n\nPlease predict the next action to complete the task.\nSelect from the following choices.\nA: SCROLL: LEFT\nB: SCROLL: UP\nC: SCROLL: DOWN\nD: CLICK: (31, 960)\n"
question = "The last image represents the current screenshot and the preceding images are historical screenshots. The historical actions are: step 1: CLICK: (603, 801)\nstep 2: CLICK: (190, 427)\nstep 3: CLICK: (834, 565)\nI want to Open the Firefox Browser to search for the best video blogs on travel vlogs. Then, go to the Setting app to turn up the brightness on your phone. Finally, open the YouTube app to follow the video blogs you found. Which action should I do next?"
question = context + '\n' + question
question = question + '\nPlease answer the option directly like A,B,C,D...'

file_paths = [
            "3873605806112821_0.png",
            "3873605806112821_1.png",
            "3873605806112821_2.png",
            "3873605806112821_3.png"
        ]




files = [('files', open(file_path, 'rb')) for file_path in file_paths]
data = {
    'question': question,
    'api_key': api_key
}

while True:
    try:
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("Response:", response.json().get("response", "No response key found in the JSON."))
            break  # Exit the loop if the request is successful
        else:
            print("Error:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    # Wait for a while before retrying
    time.sleep(2)


print('------------------------------')
