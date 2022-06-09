from typing import Dict, List


def format_data(data: List[str], range: int) -> List[Dict]:
    formated_data: List[Dict] = [
        {"index": index, "type": value, "accessible": 0}
        for index, value in enumerate(data)
    ]

    for index, value in enumerate(formated_data):
        accessible_oposite_values: List[Dict] = get_accessible_oposite_values(
            index, range, formated_data
        )
        value.update({"accessible": len(accessible_oposite_values)})

    return formated_data


def get_accessible_oposite_values(
    index: int, range: int, data: List[Dict]
) -> List[Dict]:
    start: int = max(0, index - range)
    end: int = min(len(data), index + range + 1)
    accessible_values: List[Dict] = data[start:end]
    return list(
        filter(
            lambda accessible_value: accessible_value.get("type")
            != data[index].get("type"),
            accessible_values,
        )
    )


def get_num_possible_catches(data: List[Dict], range: int) -> int:
    polices: List[Dict] = get_selected_types("P", data)
    got_a_catch: List[Dict] = []
    catched: List[Dict] = []
    for police in polices:
        accessible_thiefs: List[Dict] = get_accessible_oposite_values(
            data.index(police), range, data
        )

        if len(accessible_thiefs) > 0:
            accessible_thiefs.sort(key=lambda iten: iten.get("accessible"))
            wanted_thief: Dict = accessible_thiefs[0]
            data = list(
                filter(
                    lambda inten: inten.get("index") != wanted_thief.get("index"),
                    data,
                )
            )

            catched.append(wanted_thief)
            got_a_catch.append(police)

    return len(got_a_catch)


def get_selected_types(wanted_type: str, data: List[Dict]) -> List[Dict]:
    selected_types: List[Dict] = list(
        filter(lambda iten: iten.get("type").upper() == wanted_type.upper(), data)
    )
    selected_types.sort(key=lambda iten: iten.get("accessible"))
    return selected_types

k = 2
input = ["T", "T", "P", "P", "T", "P"]
formated_data = format_data(input, k)
num_possible_catches = get_num_possible_catches(formated_data, k)
print(num_possible_catches)
