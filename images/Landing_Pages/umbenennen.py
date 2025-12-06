import os
import shutil

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
    "Lemsahl Mellingstedt",
    "Hamburg Allermöhe",
    "Hamburg Bergedorf",
    "Hamburg Billbrook",
    "Hamburg Billstedt",
    "Hamburg Lohbrügge",
    "Hamburg Mümmelmannsberg"
]

quelle_ordner = "Ahrensburg2"
dateien = [f for f in os.listdir(quelle_ordner) if f.endswith(".webp")]

for stadt in staedte:
    # Zielordner: Leerzeichen → _, Bindestrich bleibt
    ordnername = stadt.replace(" ", "_")
    os.makedirs(ordnername, exist_ok=True)

    for datei in dateien:
        # Ersetze "Ahrensburg" im Dateinamen durch den Stadtnamen
        neuer_dateiname = datei.replace("Ahrensburg", stadt)
        # Leerzeichen → _
        neuer_dateiname = neuer_dateiname.replace(" ", "_")

        quelle_datei = os.path.join(quelle_ordner, datei)
        ziel_datei = os.path.join(ordnername, neuer_dateiname)

        shutil.copy2(quelle_datei, ziel_datei)

print("Fertig! Dateien wurden kopiert und umbenannt.")
