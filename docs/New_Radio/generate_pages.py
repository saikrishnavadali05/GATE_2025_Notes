import os

# Folder structure and files mapping
structure = {
    "introduction": ["intro.html"],
    "network-elements": ["gnb.html", "ng-core-network.html", "interfaces.html"],
    "spectrum": ["fr1-sub6.html", "fr2-mmwave.html", "bandwidth-duplexing.html"],
    "protocols": ["rrc.html", "pdcp-rlc-mac-phy.html"],
    "advanced-techniques": ["beamforming.html", "massive-mimo.html", "numerology.html"],
    "performance": ["latency.html", "spectral-efficiency.html", "new-capabilities.html", "initial-access.html"],
}

# Boilerplate HTML template generator
def generate_html(title, relative_path_to_home="../../New-Radio-index.html"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title}</title>
  <link rel="stylesheet" href="../../css/styles.css">
  <script defer src="../../js/script.js"></script>
</head>
<body>

<a href="{relative_path_to_home}" class="home-button">← Back to Home</a>

<h1>{title}</h1>

<button class="accordion">What is 5G NR?</button>
<div class="panel">
  <p>
    5G NR (New Radio) is the global standard for a new air interface developed by 3GPP for the 5th generation of mobile networks. It is designed to support faster data rates, ultra-low latency, and massive device connectivity.
  </p>
</div>

<button class="accordion">Why 5G NR?</button>
<div class="panel">
  <ul>
    <li><strong>Enhanced Mobile Broadband (eMBB):</strong> High-speed internet for applications like 4K video and AR/VR.</li>
    <li><strong>Ultra-Reliable Low Latency Communications (URLLC):</strong> Real-time control for autonomous vehicles, remote surgery, etc.</li>
    <li><strong>Massive Machine-Type Communications (mMTC):</strong> Supports IoT devices in smart cities and industries.</li>
  </ul>
</div>

<button class="accordion">Key Differences from 4G</button>
<div class="panel">
  <ul>
    <li>Flexible numerology and slot structures</li>
    <li>Use of millimeter wave (mmWave) spectrum</li>
    <li>Support for network slicing</li>
    <li>Built-in support for beamforming and Massive MIMO</li>
  </ul>
</div>

<button class="accordion">Spectrum Usage</button>
<div class="panel">
  <p>
    5G operates in multiple frequency bands:
  </p>
  <ul>
    <li><strong>Sub-1 GHz:</strong> Good coverage (rural)</li>
    <li><strong>1–6 GHz:</strong> Balanced coverage and capacity</li>
    <li><strong>mmWave (24+ GHz):</strong> Very high capacity (urban, dense environments)</li>
  </ul>
</div>

<button class="accordion">Global Standardization</button>
<div class="panel">
  <p>
    5G NR is being standardized by the 3rd Generation Partnership Project (3GPP). The first official specification was part of 3GPP Release 15, with enhancements in Release 16 and 17.
  </p>
</div>

<button class="accordion">Real-world Applications</button>
<div class="panel">
  <ul>
    <li>Smart factories and automation</li>
    <li>Connected vehicles (V2X)</li>
    <li>Telemedicine and remote healthcare</li>
    <li>Cloud gaming and immersive media</li>
  </ul>
</div>

<script src="../../js/accordion.js"></script>
</body>
</html>
"""

base_dir = "topics"

for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

    for file in files:
        # Create a friendly title from filename, e.g., "gnb.html" => "gNB"
        name = file.replace(".html", "").replace("-", " ").title()
        # Special casing some titles to make them more readable
        special_titles = {
            "Intro": "Introduction to 5G New Radio (NR)",
            "Gnb": "gNB - Next Generation NodeB",
            "Ng Core Network": "NG Core Network",
            "Interfaces": "5G NR Interfaces",
            "Fr1 Sub6": "Frequency Range 1 (Sub 6 GHz)",
            "Fr2 Mmwave": "Frequency Range 2 (mmWave)",
            "Bandwidth Duplexing": "Bandwidth and Duplexing",
            "Rrc": "Radio Resource Control (RRC)",
            "Pdcp Rlc Mac Phy": "PDCP, RLC, MAC, and PHY Layers",
            "Beamforming": "Beamforming in 5G NR",
            "Massive Mimo": "Massive MIMO Technology",
            "Numerology": "Numerology & Subcarrier Spacing",
            "Latency": "Comparison of Latency",
            "Spectral Efficiency": "Spectral Efficiency",
            "New Capabilities": "New Capabilities in 5G NR",
            "Initial Access": "Initial Access Procedures",
        }
        title = special_titles.get(name, name)

        file_path = os.path.join(folder_path, file)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(generate_html(title))

print("Folder structure and HTML files created successfully.")
