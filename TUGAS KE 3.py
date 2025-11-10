class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Nama : {self.name}\nUmur : {self.age}"


class Lecturer(Person):
    def __init__(self, name, age, nidn, course):
        super().__init__(name, age)
        self.nidn = nidn
        self.course = course

    def info(self):
        return f"{super().info()}\nNIDN : {self.nidn}\nMengajar : {self.course}"


class Student(Person):
    def __init__(self, name, age, nim, major):
        super().__init__(name, age)
        self.nim = nim
        self.major = major

    def info(self):
        return f"{super().info()}\nNIM : {self.nim}\nJurusan : {self.major}"


lecturers = []
students = []

lecturers.append(Lecturer("Edy haryanto,Kom.,M.Eng", 30, "0823129103", "Pemrograman Beroriontasi Objek"))
students.append(Student("haidul mahfud", 23, "24241130", "Teknologi Informasi"))

print("=== DATA DOSEN ===")
for d in lecturers:
    print(d.info())
    print("-" * 30)

print("\n=== DATA MAHASISWA ===")
for m in students:
    print(m.info())
    print("-" * 30)