# dataProcessing
cd dataPreprocessing
Clone : https://github.com/logpai/logparser

## extraction: extract the message_text field
This script extracts only the message_text field from the whole set of logs and extracted.csv file is generated
```
cd extraction
python3 extract.py
```
The extracted log is also stored in "customParser/data/log"

## customParser: Parsing the logs to generate template and structured data 
In customParser/main_logparser.py, change the values of st and depth 
st = 0.6  # Similarity threshold
depth = 8  # Depth of all leaf nodes
```
cd customParser
export PYTHONPATH="${PYTHONPATH}:/home/nimish/go/src/github.com/KzannaInc/dataProcessing/logparser"
python3 main_logparser.py
```
This script spit out 2 files log_template.csv and log_structured.csv stored in customParser/processing/label_result