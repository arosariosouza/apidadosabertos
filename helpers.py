def data_to_string(value):
    delimiter = ';'

    def __prepare_csv_value(value):
        return ''.join(('"', value.replace(delimiter,''), '"')) if type(value) is str else str(value) if value is not None else ''

    def __instance_to_list(_data):
        columns = []
        rows = []
        columns.append([__prepare_csv_value(column) for column in list(_data.keys())])
        rows.append([__prepare_csv_value(_data[key]) for key in list(_data.keys())])

        return columns + rows

    def __collection_to_list(_data):
        items = _data[list(_data.keys())[0]]
        columns = list(items[0].keys())

        header = [[__prepare_csv_value(column) for column in columns]]
        rows = [[__prepare_csv_value(dict_item[key])  for key in dict_item.keys()] for dict_item in [item for item in items]]

        return header + rows

    def __to_string(_data):
        return '\r\n'.join([delimiter.join(i) for i in _data])

    if type(value) is dict:
        qty_keys = len(value.keys())
        if qty_keys > 1:
            return __to_string(__instance_to_list(value))
        elif qty_keys == 1:
            return __to_string(__collection_to_list(value))
           
    return None