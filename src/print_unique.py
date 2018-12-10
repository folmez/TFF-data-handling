#import src
import src

def leagues(filename):
    df = src.read_csv_into_data_frame(filename)

    print(df['Organizasyon'].unique())

def deplasman_skor(filename):
    df = src.read_csv_into_data_frame(filename)

    print(df['Deplasman skor'].unique())
