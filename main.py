from configuration import get_target_config 
from attacks import select_attack
from target_client import send_prompt
from verification import verify_response
import json
from datetime import datetime

import os

targetdata=get_target_config()
selected_attack=select_attack()
print(targetdata["model_name"]);
print(targetdata["api_endpoint"]);
print("selected attack : ",selected_attack)

results=[]


if selected_attack == "prompt_injection":
    file_path = "test_data/prompts/prompt_injection.json"

elif selected_attack == "jailbreak":
    file_path = "test_data/prompts/jailbreak.json"


elif selected_attack == "system_prompt_exposure":
    file_path = "test_data/prompts/system_prompt_exposure.json"

elif selected_attack == "cross_user_data_access":
    file_path = "test_data/prompts/cross_user_data_access.json"
    
elif selected_attack == "excessive_agency":
    file_path = "test_data/prompts/excessive_agency.json"
else:
    raise ValueError(f"Unsupported attack type: {selected_attack}")

file = open(file_path, "r")
data = json.load(file)
file.close()


for i in data:
        print(i["test_id"])
        print(i["prompt"])
        llm_response=send_prompt(targetdata,i["prompt"])
        print(llm_response)
    
        verified_response = verify_response(i, llm_response, selected_attack )
        print(verified_response["test_id"])
        print(verified_response["status"])
        results.append(verified_response)

        


os.makedirs("results", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"results/{selected_attack}_results_{timestamp}.json"
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)

print(f"Results saved to: {file_name}")


fail_count = 0
pass_count = 0
inconclusive_count = 0

total_tests = len(results)

for result in results:
    if result["status"].lower() == "fail":
        fail_count += 1
    elif result["status"].lower() == "pass":
        pass_count += 1
    else:
        inconclusive_count += 1

summary = {
    "total_tests": total_tests,
    "pass": pass_count,
    "fail": fail_count,
    "inconclusive": inconclusive_count
}

report = {
    "summary": summary,
    "results": results
}

with open(file_name, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("Summary:", summary)
print(f"Results saved to: {file_name}")


print("Total:", total_tests)
print("Fail:", fail_count)
print("Pass:", pass_count)
print("Inconclusive:", inconclusive_count)

