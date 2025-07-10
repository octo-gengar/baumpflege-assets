import os
import shutil

# Liste der Städte (wie von dir vorgegeben)
staedte = [
    "Ahrensburg",
    "Ammersbek",
    "Aumühle",
    "Bargteheide",
    "Bad Oldesloe",
    "Barsbüttel",
    "Escheburg",
    "Geesthacht",
    "Großhansdorf",
    "Glinde",
    "Oststeinbek",
    "Reinbek",
    "Reinfeld",
    "Schwarzenbek",
    "Stapelfeld",
    "Trittau",
    "Hamburg Bergstedt",
    "Hamburg Poppenbüttel",
    "Hamburg Sasel",
    "Hamburg Volksdorf",
    "Hamburg Nord",
    "Hamburg Bramfeld",
    "Hamburg Barmbek",
    "Hamburg Farmsen",
    "Hamburg Wandsbek",
    "Hamburg Rahlstedt",
    "Hamburg Meiendorf",
    "Hamburg Jenfeld",
    "Hamburg Marienthal",
    "Hamburg Horn",
    "Hamburg Hamm",
    "Lemsahl - Mellingstedt",
    "Hamburg Allermöhe",
    "Hamburg Bergedorf",
    "Hamburg Billbrook",
    "Hamburg Billstedt",
    "Hamburg Lohbrügge",
    "Hamburg Mümmelmannsberg"
]

# Pfad zum Quellordner mit den .webp Dateien
quelle_ordner = "Ahrensburg2"

# Alle Dateien im Quelleordner auflisten
dateien = [f for f in os.listdir(quelle_ordner) if f.endswith(".webp")]

for stadt in staedte:
    ziel_ordner = stadt
    os.makedirs(ziel_ordner, exist_ok=True)
    
    for datei in dateien:
        # Neuer Dateiname mit Stadtnamen ersetzt
        neuer_dateiname = datei.replace("Ahrensburg", stadt)
        quelle_datei = os.path.join(quelle_ordner, datei)
        ziel_datei = os.path.join(ziel_ordner, neuer_dateiname)
        
        shutil.copy2(quelle_datei, ziel_datei)

print("Fertig! Dateien wurden kopiert und umbenannt.")
