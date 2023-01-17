inputbox = Element("search")
output = Element("table")
template = Element("list-template").select(".data", from_content=True)

from pyodide import open_url
with open_url("https://raw.githubusercontent.com/loczylevi/Kemiai_Elemek/main/tablazat.txt") as file:
    search_data = []
    for line in file:
        search_data.append(line.strip().split(";"))
    search_data.pop(0)

output_ids = []
for line in search_data:
    data = {
        "id": line[3],
        "name": line[1],
        "other": "Year: " + line[0] + "  | Symbol: " + line[2] + "  | Atomic number: " + line[3] + "  | Discovered by: " + line[4] + "  | Atomic weight: " + line[5] + "  | Negativity: " + line[6]
    }
    if data["id"] not in output_ids:
        output_ids.append(data["id"])
        output_set = template.clone(data["id"])
        output_set.select("h3").element.innerText = data["name"]
        output_set.select("a").element.innerText = data["other"]
        output.element.appendChild(output_set.element)

def onSubmit(*args, **kwargs):
    for _ in range(output.element.childElementCount):
        output.element.removeChild(output.element.firstChild)
    output_ids = []
    if inputbox.value != "":
        for line in search_data:
            for pieces in line:
                if str(inputbox.value).lower() in pieces.lower():
                    data = {
                        "id": line[3],
                        "name": line[1],
                        "other": "Year: " + line[0] + "  | Symbol: " + line[2] + "  | Atomic number: " + line[3] + "  | Discovered by: " + line[4] + "  | Atomic weight: " + line[5] + "  | Negativity: " + line[6]
                    }
                    if data["id"] not in output_ids:
                        output_ids.append(data["id"])
                        output_set = template.clone(data["id"])
                        output_set.select("h3").element.innerText = data["name"]
                        output_set.select("a").element.innerText = data["other"]
                        output.element.appendChild(output_set.element)
    else:
        for line in search_data:
            data = {
                "id": line[3],
                "name": line[1],
                "other": "Year: " + line[0] + "  | Symbol: " + line[2] + "  | Discovered by: " + line[3] + "  | Atomic weight: " + line[4] + "  | Negativity: " + line[5]
            }
            if data["id"] not in output_ids:
                output_ids.append(data["id"])
                output_set = template.clone(data["id"])
                output_set.select("h3").element.innerText = data["name"]
                output_set.select("a").element.innerText = data["other"]
                output.element.appendChild(output_set.element)
