import pandas as pd
import os

print("Reading log_templates.csv and log_structured.csv\n")

# Read log_templates.csv and log_structured.csv
templates_df = pd.read_csv('label_result/log_templates.csv')
structured_df = pd.read_csv('label_result/log_structured.csv')

# Define mapping of Label values to TYPE
label_to_type = {1: 'POSITIVE', 2: 'NEUTRAL', 3: 'NEGATIVE'}

# Check if unlabelled file exists, delete it if it does
unlabelled_log = 'unlabelled/log'
if os.path.exists(unlabelled_log):
    os.remove(unlabelled_log)

template_cnt = 0
structured_data_cnt = 0

# Initialize empty lists to store the data
template_data = []
structured_data = []

# Iterate over each row in templates_df
for index, row in templates_df.iterrows():
    print(f"Labelling template >> {row['EventTemplate']}")
    if row['Label'] in [1, 2, 3]:
        # Extract corresponding records from structured_df
        corresponding_records = structured_df[structured_df['EventId'] == row['EventId']].copy()

        # Add TYPE column and map Label values
        corresponding_records['Label'] = label_to_type[row['Label']]

        # Append the template data
        template_data.append({'Label': label_to_type.get(row['Label'], 'UNKNOWN'), 'Template': row['EventTemplate']})

        # Append the structured data
        for _, record in corresponding_records.iterrows():
            structured_data.append(record.tolist())
            structured_data_cnt += 1

        template_cnt += 1
    elif pd.isnull(row['Label']):
        # continue
        # Extract corresponding records from structured_df
        corresponding_records = structured_df[structured_df['EventId'] == row['EventId']]

        # Dump only Content column into the unlabelled file
        unlabelled_file = 'unlabelled/log'
        with open(unlabelled_file, 'a') as f:
            for content in corresponding_records['Content']:
                f.write(f"{content}\n")

print("Total templates", template_cnt)
print("Processed records", structured_data_cnt)

# Save the template data to a CSV file
template_df = pd.DataFrame(template_data, columns=['Label', 'Template'])
template_df.to_csv('../result/template.csv', index=False)

# Save the structured data to a CSV file

st_columns = ['LineId', 'Content', 'EventId', 'EventTemplate', 'ParameterList', 'Label']
structured_df = pd.DataFrame(structured_data, columns=st_columns)
structured_df.to_csv('../result/structured.csv', index=False)
# structured_df = pd.DataFrame(structured_data, columns=structured_df.columns)
# structured_df.to_csv('../result/structured.csv', index=False)