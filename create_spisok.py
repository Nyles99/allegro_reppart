import json


with open('modelu.json', encoding="utf-8") as file:
    model_need_list = json.load(file)
modelu_new = {}           
for model, marka in model_need_list.items():
    #print(model)
    if "Land-Rover" not in model:
        model = str(model).lower()
        model = model[model.find("-")+1 : ].replace(" ","-").replace("/","-")
        print(model)
        modelu_new[model] = marka
    else:
        model = str(model).lower()
        model = model[11 : ].replace(" ","-").replace("/","-")
        print(model)
        modelu_new[model] = marka

with open("modelu_new.json", "a", encoding="utf-8") as file:
    json.dump(modelu_new, file, indent=4, ensure_ascii=False)