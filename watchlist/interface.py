class IdentifyResult:
    record_name = ''
    id_value = ''
    id_type = ''
    result = 0

    def __init__(self, record_name, id_value, id_type, result):
        self.record_name = record_name
        self.id_value = id_value
        self.id_type = id_type
        self.result = result
