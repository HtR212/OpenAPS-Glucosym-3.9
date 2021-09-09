import json
import csv

with open("enact/all_suggested.json") as read_all_suggested:
	loaded_all_suggested_data = json.load(read_all_suggested)



#bg = []
#eventualBG = []
#insulinReq = []
#IOB = []
#rate = []

parsed_all_suggested = []


for _ in range(len(loaded_all_suggested_data)):
	#if 'bg' not in loaded_all_suggested_data[_]:
	#	continue
	#if all(i in loaded_all_suggested_data[_] for i in ("bg","eventualBG","loaded_glucose","IOB", "rate")):
	if True:
		#print("they are all there")
		parsed_element = {"bg":0,"eq_BG":0,"CGM_glucose": 0, "IOB":0, "rate":0, "running_temp":0,"unsafe_action_reason": "Null"}
		parsed_element["bg"] = loaded_all_suggested_data[_]['bg']
		parsed_element["CGM_glucose"] = loaded_all_suggested_data[_]["loaded_glucose"]
		parsed_element["eq_BG"] = loaded_all_suggested_data[_]["eventualBG"]
		#parsed_element["insulinReq"] = loaded_all_suggested_data[_]["insulinReq"]
		parsed_element["IOB"] = loaded_all_suggested_data[_]["IOB"]
		parsed_element["rate"] = loaded_all_suggested_data[_]["rate"] if "rate" in loaded_all_suggested_data[_] else 0
		parsed_element["running_temp"] = loaded_all_suggested_data[_]["running_temp"]
		#parsed_element["running_temp"] = loaded_all_suggested_data[_]["running_temp"]["rate"]
		#parsed_element["duration"] = loaded_all_suggested_data[_]["duration"]
		#parsed_element["short_avgdelta"] = loaded_all_suggested_data[_]["short_avgdelta"]
		#parsed_element["long_avgdelta"] = loaded_all_suggested_data[_]["long_avgdelta"]
		#parsed_element["deviation"] = loaded_all_suggested_data[_]["deviation"]
		#parsed_element["minDelta"] = loaded_all_suggested_data[_]["minDelta"]
		#parsed_element["delta"] = loaded_all_suggested_data[_]["delta"]
		#parsed_element["minAvgDelta"] = loaded_all_suggested_data[_]["minAvgDelta"]
		#parsed_element["bgi"] = loaded_all_suggested_data[_]["bgi"]
		#parsed_element["expectedDelta"] = loaded_all_suggested_data[_]["expectedDelta"]
		if "fault_reason" in loaded_all_suggested_data[_]:
			parsed_element["unsafe_action_reason"] = loaded_all_suggested_data[_]["fault_reason"]
		parsed_all_suggested.insert(0,parsed_element)
		#print(parsed_all_suggested)


keys = parsed_all_suggested[0].keys()
#print(parsed_all_suggested)

with open('data.csv','w') as output_file:
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writeheader()
	dict_writer.writerows(parsed_all_suggested)
