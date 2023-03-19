import pandas as pd
import json
from pathlib import Path

def json_to_csv(json_path):

    path = Path(json_path)
    with open(path, "r") as file:
        content = json.load(file)

    # Iterar sobre a lista de dicionários e extrair os valores relevantes
    rows = []
    for index, data_text in enumerate(content):
        if content[index]["total_annotations"] == 1:
            text = data_text['data']['text']

            values = []
            for annotation in data_text['annotations']:
                for result in annotation['result']:
                    values.append(result['value']['text'])

            value = ' '.join(values)
            rows.append({'text': text, 'value': value})

    # Criar o dataframe
    df = pd.DataFrame(rows)
    df.to_csv("./data.csv", index=False)