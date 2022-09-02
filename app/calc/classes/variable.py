class Variable:
    def __init__(self, name, value, id_num, dim, tex_name):
        self.name = name
        self.id_num = id_num
        if value is None:
            self.value = None
        else:
            self.value = float(value)
        self.dim = dim
        self.tex_name = tex_name
        self.image_name = self.name_to_image_name()

    def name_to_image_name(self):
        name_bytes = self.name.encode("utf-8")
        return str(int.from_bytes(name_bytes, "little"))

    def name_image_to_name(self):
        name_bytes = self.name.encode("utf-8")
        int_name = int.from_bytes(name_bytes, "little")
        name_bytes = int_name.to_bytes((int_name.bit_length() + 7) // 8, "little")
        name_bytes = name_bytes.decode("utf-8")
        return name_bytes
