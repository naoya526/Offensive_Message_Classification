import pandas as pd

def convert_textfile_to_csv(input_file='raw_data.txt', output_file='dataset.csv'):
    data = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ':' in line:
                label, text = line.split(':', 1)
                label = label.strip()
                text = text.strip()
                if label and text:
                    data.append({'label': label, 'text': text})

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Saved to {output_file}")

# 実行
convert_textfile_to_csv(input_file='250618-toxic-language/test.txt',output_file='toxic-language-csv/test.csv')
convert_textfile_to_csv(input_file='250618-toxic-language/train.txt',output_file='toxic-language-csv/train.csv')
