import data


class DataValues:
    def __init__(self, table_name, key_name):
        self.table_name = table_name
        self.column_name = None
        self.key_name = key_name

    def to(self, column_name):
        self.column_name = column_name
        return self

    def operate_int_value(self, key_value, value):
        current_value = self.get_value(key_value)
        new_value = current_value + value
        data.update_data(
            "UPDATE {0} SET {1} = ? WHERE {2} = ?".format(self.table_name, self.column_name, self.key_name),
            (new_value, key_value))

    def get_value(self, key_value):
        data_value = data.get_data_as_dictionary('SELECT {1} FROM {0} WHERE {2} = ?'.format(self.table_name, self.column_name, self.key_name),
                                    (key_value,))
        return data_value[0][self.column_name.lower()]

    def get_all_json_data(self):
        all_json_data = data.get_json_data('SELECT * FROM {0}'.format(self.table_name))
        return all_json_data
