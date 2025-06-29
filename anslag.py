"""Summary

Attributes:
    calibers (TYPE):        List of calibers for each cartridge
    cartridges (TYPE):      List of dictionaries describing cartrigdes and their essential parameters 
    color_map (TYPE):       Description
    colors (TYPE):          Description
    energies (TYPE):        List of energies of bullets at 100 meters
    expansion (TYPE):       Whether the bullet is expanding or not
    forskriftstekst (TYPE): Description
    labels (TYPE):          List of labels describing the brand and make of the cartridge
    marker_sizes (TYPE):    List of marker sizes indicating bullet weight
    markers (TYPE):         List of markers indicating X-panding bullets
    velocities (TYPE):      List of bullet muzzle velocities
    weights (TYPE):         List of bullet weights
"""
import matplotlib.pyplot as plt

# Define data for cartridges as a list
cartridges = [
    {"label": "Norma ECO Power-22 grs",     "weight":1.55,  "grains":"22",   "cal":".22LR",     "muzzle_velocity":520,   "exp":"no",   "lead_free": None,  "energy_100m": 76},
    {"label": "Norma 17grs V-Max",          "weight":1.1,   "grains":"17",   "cal":".17HMR",    "muzzle_velocity":777,   "exp":"yes",  "lead_free": None,  "energy_100m": 177.6},
    {"label": "S&B 223Rem 55 SP",           "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 1006, "exp": "yes", "lead_free": None,  "energy_100m": 1370},
    {"label": "Sako Gamehead 55grs",        "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 970,  "exp": "yes", "lead_free": None,  "energy_100m": 1226},
    {"label": "Norma Oryx",                 "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 950,  "exp": "yes", "lead_free": None,  "energy_100m": 1087},
    {"label": "Norma Jaktmatch",            "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 990,  "exp": "no",  "lead_free": None,  "energy_100m": 1256},
    {"label": "GECO Target FMJ",            "weight": 4.1,  "grains": "63",  "cal": ".223",     "muzzle_velocity": 950,  "exp": "no",  "lead_free": None,  "energy_100m": 1516},
    {"label": "GECO Express",               "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 1010, "exp": "yes", "lead_free": None,  "energy_100m": 1294},
    {"label": "RWS Soft Point",             "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 1000, "exp": "yes", "lead_free": None,  "energy_100m": 1276},
    {"label": "S&B 55grs FMJ",              "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 1006, "exp": "no",  "lead_free": None,  "energy_100m": 1464},
    {"label": "Sierra BlitzKing",           "weight": 3.6,  "grains": "55",  "cal": ".223",     "muzzle_velocity": 930,  "exp": "yes", "lead_free": None,  "energy_100m": 1190},
    {"label": "Lapua Naturalis",            "weight": 3.2,  "grains": "50",  "cal": ".223",     "muzzle_velocity": 1015, "exp": "yes", "lead_free": None,  "energy_100m": 1155},
    {"label": "S&B 140grs FMJ",             "weight": 9.1,  "grains": "140", "cal": "6.5x55",   "muzzle_velocity": 787,  "exp": "no",  "lead_free": None,  "energy_100m": 2451},
    {"label": "S&B 124grs FMJ",             "weight": 8.0,  "grains": "124", "cal": "6.5x55",   "muzzle_velocity": 834,  "exp": "no",  "lead_free": None,  "energy_100m": 2316},
    {"label": "S&B 124grs FMJ",             "weight": 8.0,  "grains": "124", "cal": "6.5x55",   "muzzle_velocity": 834,  "exp": "no",  "lead_free": None,  "energy_100m": 2316},
    {"label": "S&B 124grs FMJ",             "weight": 8.0,  "grains": "124", "cal": ".308W",    "muzzle_velocity": 905,  "exp": "no",  "lead_free": None,  "energy_100m": 2663},
    {"label": "S&B 147grs FMJ",             "weight": 9.55, "grains": "147", "cal": ".308W",    "muzzle_velocity": 850,  "exp": "no",  "lead_free": None,  "energy_100m": 2846},
    {"label": "S&B 180grs FMJ",             "weight": 11.7, "grains": "180", "cal": ".308W",    "muzzle_velocity": 735,  "exp": "no",  "lead_free": None,  "energy_100m": 2697},
    {"label": "Lapua Mega blyspiss 150",    "weight": 9.7,  "grains": "150", "cal": ".308W",    "muzzle_velocity": 850,  "exp": "yes", "lead_free": None,  "energy_100m": 2795},
    {"label": "Lapua Mega blyspiss 185",    "weight": 12.0, "grains": "185", "cal": ".308W",    "muzzle_velocity": 765,  "exp": "yes", "lead_free": None,  "energy_100m": 2750},
    {"label": "Norma 150 Jaktmatch FMJ",    "weight": 9.7,  "grains": "150", "cal": ".308W",    "muzzle_velocity": 810,  "exp": "no",  "lead_free": None,  "energy_100m": 2664},
    {"label": "Norma Bondstrike 180 HP",    "weight": 11.7, "grains": "180", "cal": ".308W",    "muzzle_velocity": 786,  "exp": "yes", "lead_free": None,  "energy_100m": 3338},
    {"label": "Norma Vulkan 180grs ",       "weight": 11.7, "grains": "180", "cal": ".308W",    "muzzle_velocity": 796,  "exp": "yes", "lead_free": None,  "energy_100m": 2908},
    {"label": "Blaser 165 CDB",             "weight": 10.7, "grains": "165", "cal": ".308W",    "muzzle_velocity": 744,  "exp": "yes", "lead_free": None,  "energy_100m": 2961},
    {"label": "Lapua Naturalis 170grs",     "weight": 11.0, "grains": "170", "cal": ".308W",    "muzzle_velocity": 800,  "exp": "yes", "lead_free": None,  "energy_100m": 2829},
    {"label": "S&B 180grs FMJ",             "weight": 11.7, "grains": "180", "cal": ".30-06",   "muzzle_velocity": 815,  "exp": "no",  "lead_free": None,  "energy_100m": 3308},
    {"label": "Lapua Mega 200grs",          "weight": 13.0, "grains": "200", "cal": ".30-06",   "muzzle_velocity": 775,  "exp": "yes", "lead_free": "yes", "energy_100m": 3892},
    {"label": "Lapua Naturalis 170grs",     "weight": 11.0, "grains": "170", "cal": ".30-06",   "muzzle_velocity": 830,  "exp": "yes", "lead_free": "yes", "energy_100m": 3060},
    {"label": "S&B 124grs FMJ",             "weight": 8.0,  "grains": "124", "cal": ".30-06",   "muzzle_velocity": 858,  "exp": "no",  "lead_free": None,  "energy_100m": 2945},
    # Add other entries here...
]


# Extract data for plotting
labels      = [c["label"] for c in cartridges]
weights     = [c["weight"] for c in cartridges]
velocities  = [c["muzzle_velocity"] for c in cartridges]
energies    = [c["energy_100m"] for c in cartridges]
calibers    = [c["cal"] for c in cartridges]
expansion   = [c["exp"] for c in cartridges]

# Marker sizes based on bullet weight
marker_sizes = [w * 30 for w in weights]

# Define colors based on caliber
color_map = {
    ".30-06": "brown",
    ".308W": "limegreen",
    ".17HMR": "orange",
    ".223": "green",
    "6.5x55": "blue",
    ".22LR": "pink"}

colors = [color_map[cal] for cal in calibers]

# Define markers based on expansion
markers = ['X' if exp == "yes" else 'o' for exp in expansion]

# Create scatter plot
plt.figure(figsize=(10, 8))

for i in range(len(cartridges)):
    plt.scatter(
        velocities[i], energies[i],
        s=marker_sizes[i],
        c=colors[i],
        marker=markers[i],
        edgecolor='black',
        alpha=0.7
    )

# Add text labels, with red color for low-weight bullets
for i, label in enumerate(labels):
    text_color = 'red' if weights[i] < 9 else 'black'
    plt.text(
        velocities[i], energies[i],
        f"{label}\n{weights[i]} g",
        fontsize=9, ha='right', va='bottom', color=text_color
    )

# Add titles and axes labels
# plt.title("Muzzle Velocity vs. Energy at 100 Meters by Caliber and Expansion")
# plt.xlabel("Muzzle Velocity (m/s)")
# plt.ylabel("Energy at 100 Meters (Joules)")

plt.title("Munningshastighet vs Energi på 100 meter etter kaliber og ekspansjon")
plt.xlabel("Munningshastighet (m/s)")
plt.ylabel("Energi på 100 Meter (Joules)")

# Reference lines
plt.axhline(y=980, color='seagreen', linestyle='-.', linewidth=1, label="980 J")
plt.axhline(y=2200, color='orange', linestyle='--', linewidth=1, label="2200 J")

# Legend for calibers and expansion
for cal, color in color_map.items():
    plt.scatter([], [], color=color, label=f"{cal}", s=100, edgecolor='black')

# plt.scatter([], [], color='black', marker='X', s=100, label='Expanding')
# plt.scatter([], [], color='black', marker='o', s=100, label='Non-Expanding')
plt.scatter([], [], color='black', marker='X', s=100, label='Ekspanderende')
plt.scatter([], [], color='black', marker='o', s=100, label='Ikke-ekspanderende')
# plt.legend(title="Caliber and Expansion")
plt.legend(title="Kaliber og ekspansjon")

# skriver ut forskriftsteksten til konsoll
forskriftstekst = """
Forskrift om utøvelse av jakt, felling og fangst
Dato    FOR-2002-03-22-313

...

Kapittel 5. Våpen og ammunisjon
§ 15.Våpen under jakt og felling

Under ordinær jakt og felling kan det bare brukes rifle og haglevåpen med ladning av krutt. Under jakt og felling er det ikke tillatt å bruke pistol, revolver, halvautomatiske våpen av militær karakter eller helautomatiske skytevåpen.

Under jakt på elg, hjort, dåhjort, villrein, muflon, moskusfe eller felling av bjørn og ulv er det kun tillatt å bruke rifle. Det samme gjelder jakt på råbukk i særskilt bukkejaktperiode.

Under jakt på elg, hjort og rådyr er det ikke tillatt å bruke halvautomatisk rifle med mer enn tre skudd i magasinet og ett skudd i kammeret. Under jakt på eller felling av øvrige viltarter hvor det brukes halvautomatisk rifle er det ikke tillatt å bruke mer enn to skudd i magasinet og ett skudd i kammeret.

Salongrifle (salonggevær) kaliber 22 LR kan bare brukes under jakt på viltarter opp til en hares størrelse, men ikke til hare.

Til jakt og felling er bruk av hagle for mer enn to skudd forbudt.



§ 16.Krav til rifleammunisjon

Under jakt på elg, hjort, dåhjort, villrein, villsvin eller muflon, og ved felling av ulv og bjørn skal det brukes ammunisjon med ekspanderende prosjektil. I tillegg skal følgende krav være oppfylt:
a.  Minste tillatte kaliber er 6,5 (.264″/6,71 mm).
b.  Minste tillatte kulevekt er 9 gram (138,9 grain) for kuler med mantel og blykjerne og 7,8 gram (120 grain) for blyfrie kuler.
c.  Minste tillatte anslagsenergi på 100 meter (E100) er 2200 joule.

Under jakt med rifle på rådyr, bever og gaupe eller felling av jerv og gaupe skal det brukes ammunisjon med ekspanderende prosjektil og anslagsenergien skal være minst 980 joule (100 kgm) målt på 100 meters avstand, E100.

Under jakt på storvilt er det ikke tillatt å benytte kuler og ammunisjon som er laget for trenings- og konkurranseskyting.



§ 17.Krav til hagleammunisjon

Det er forbudt å skyte med og bære blyhagl i forbindelse med jakt i våtmark, slik det fremgår i REACH-forordningen vedlegg XVII post 63 nr. 11, jf. forskrift 30. mai 2008 nr. 516 om registrering, vurdering, godkjenning og begrensning av kjemikalier (REACH-forskriften) § 1. Norsk oversettelse kan finnes som vedheng til REACH-forskriften.

Det er tillatt å bruke fyllingskule/slugs til jakt på rådyr. Til jakt på villsvin er det når haglegevær benyttes kun tillatt å benytte fyllingskule/slugs.

...

"""

print(forskriftstekst)


# Show plot
plt.tight_layout()
plt.show()
