import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

class PlantDiseaseClassifier:
    def __init__(self):
        # Aturan untuk klasifikasi penyakit
        self.rules = {
            'Rust': self.is_rust,
            'Powdery Mildew': self.is_powdery_mildew
        }

    def is_rust(self, symptoms):
        """
        Menentukan apakah tanaman terinfeksi penyakit karat (Rust).
        """

        if 'oranye' in symptoms['warna_daun'] or \
           'merah kecoklatan' in symptoms['warna_daun'] or \
           'coklat kemerahan' in symptoms['warna_daun']:
            if 'lembap' in symptoms['lingkungan'] and \
               'sirkulasi udara buruk' in symptoms['lingkungan']:
                return True
        return False

    def is_powdery_mildew(self, symptoms):
        """
        Menentukan apakah tanaman terinfeksi penyakit embun tepung (Powdery Mildew).
        """

        if 'putih' in symptoms['warna_daun'] or \
           'keabu-abuan' in symptoms['warna_daun']:
            if 'kelembapan tinggi' in symptoms['lingkungan'] and\
               'suhu dingin' in symptoms['lingkungan']:
                return True
        return False

    def classify_disease(self, symptoms):
        """
        Mengklasifikasikan penyakit berdasarkan gejala (symptoms).
        """
        for disease, rule in self.rules.items():
            if rule(symptoms):
                return disease
        return 'Tidak Teridentifikasi'


def parse_file(file_path):
    """
    Membaca file .txt yang berisi data tanaman.
    """
    plants_data = []
    try:
        with open(file_path, 'r') as file:
            data = file.read().strip().split("\n\n")

            for plant_data in data:
                lines = plant_data.split("\n")
                plant_name = lines[0].strip()
                symptoms = {}

                for line in lines[1:]:
                    key, value = line.split(":")
                    key = key.strip().lower().replace(" ", "_")
                    value = value.strip().split(",")
                    symptoms[key] = [v.strip() for v in value]

                plants_data.append({'name': plant_name, 'symptoms': symptoms})

    except Exception as e:
        print(f"Error reading file: {e}")

    return plants_data


def plot_graph(disease_counts):
    """
    Menampilkan grafik berdasarkan jumlah penyakit.
    """
    diseases = list(disease_counts.keys())
    counts = list(disease_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(diseases, counts, color=['orange', 'lightblue', 'gray'])
    plt.title('Jumlah Tanaman Berdasarkan Jenis Penyakit')
    plt.xlabel('Jenis Penyakit')
    plt.ylabel('Jumlah Tanaman')
    plt.show()



classifier = PlantDiseaseClassifier()


file_path = '/content/drive/My Drive/Colab Notebooks/tanaman_data.txt'
plants = parse_file(file_path)

# Menyimpan hasil klasifikasi
disease_counts = {
    'Rust': 0,
    'Powdery Mildew': 0,
    'Tidak Teridentifikasi': 0
}

# Proses klasifikasi
for plant in plants:
    print(f"Memproses {plant['name']}...")
    symptoms = plant['symptoms']

    # Menentukan jenis penyakit berdasarkan gejala yang dimasukkan
    result = classifier.classify_disease(symptoms)
    print(f"Jenis Penyakit: {result}")

    # Update count berdasarkan hasil klasifikasi
    if result in disease_counts:
        disease_counts[result] += 1
    else:
        disease_counts['Tidak Teridentifikasi'] += 1

    print("-" * 40)


plot_graph(disease_counts)
