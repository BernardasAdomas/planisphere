# text.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2024 Dominic Ford <https://dcford.org.uk/>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

# A list of text strings, which we can render in various languages

from typing import Dict

text: Dict[str, dict] = {
    "lt":
        {
            "title": "PLANISFERA",
            "instructions_1": "Pasukite žvaigždžių ratelį taip, kad dabartinė data ant žvaigždžių ratelio būtų tame pačiame taške, kaip dabartinė valanda ant planisferos. Dabar matysite visus žvaigždynus, kurie yra matomi danguje.",
            "instructions_2": "Atsisukite į šiaurę ir iškelkite planisferą į dangų. Žvaigždės matomos planisferos apačioje turėtų būti tos pačios, kurias matote danguje priešais save.",
            "instructions_3": """Norint pažiūrėti žvaigždes rytuose ar vakaruose pasukite visą planisferą taip, kad apačioje matytumėte žodį „East“ arba „West“ bei patys pasisukite į tą kryptį. Vėlgi, žvaigždės planisferos apačioje turėtų būti tos pačios, kurias matote prieš save.""",
            "instructions_4": (
                r"Planisfera tai paprastas prietaisas leidžiantis matyti dabartinio nakties dangaus žvaigždžių žemėlapį. Sukant ratelį galima pamatyti, kaip žvaigždės juda aplink naktinį dangų ir kaip skirtingi žvaigždynai yra matomi skirtingais metų laikais.",
                "",
                ""),
            "more_info": "\u00A9 Dominic Ford 2014\u20132024.",
            "glue_here": "GLUE HERE",
            "cut_out_instructions": (
                "Cut out this shaded area with scissors.",
                "",
                "It will become a viewing window through which to look at the star wheel behind."
            ),
            "cardinal_points": {"n": "ŠIAURĖ", "s": "PIETŪS", "w": "VAKARAI", "e": "RYTAI"},
            "months": [
                [31, "SAUSIS"],
                [28, "VASARIS"],
                [31, "KOVAS"],
                [30, "BALANDIS"],
                [31, "GEGUŽĖ"],
                [30, "BIRŽELIS"],
                [31, "LIEPA"],
                [31, "RUGPJŪTIS"],
                [30, "RUGSĖJIS"],
                [31, "SPALIS"],
                [30, "LAPKRITIS"],
                [31, "GRUODIS"]
            ],
            "constellation_translations": {
                "Andromeda": "Andromeda",
                "Antlia": "Siurblys",
                "Apus": "Rojaus_Paukštis",
                "Aquarius": "Vandenis",
                "Aquila": "Erelis",
                "Ara": "Aukuras",
                "Aries": "Avinas",
                "Auriga": "Vežėjas",
                "Boötes": "Jaučiaganis",
                "Caelum": "Skaptukas",
                "Camelopardalis": "Žirafa",
                "Cancer": "Vėžys",
                "Canes_Venatici": "Skalikai",
                "Canis_Major": "Didysis",
                "Canis_Minor": "Mažasis",
                "Capricornus": "Ožiaragis",
                "Carina": "Laivo",
                "Cassiopeia": "Kasiopėja",
                "Centaurus": "Kentauras",
                "Cepheus": "Cefėjas",
                "Cetus": "Banginis",
                "Chamaeleon": "Chameleonas",
                "Circinus": "Skriestuvas",
                "Columba": "Balandis",
                "Coma_Berenices": "Berenikės_Garbanos",
                "Corona_Australis": "Pietų_vainikas",
                "Corona_Borealis": "Šiaurės_Vainikas",
                "Corvus": "Varnas",
                "Crater": "Taurė",
                "Crux": "Pietų_Kryžius",
                "Cygnus": "Gulbė",
                "Delphinus": "Delfinas",
                "Dorado": "Aukso_Žuvis",
                "Draco": "Slibinas",
                "Equuleus": "Žirgelis",
                "Eridanus": "Eridanas",
                "Fornax": "Krosnis",
                "Gemini": "Dvyniai",
                "Grus": "Gervė",
                "Hercules": "Heraklis",
                "Horologium": "Laikrodis",
                "Hydra": "Hidra",
                "Hydrus": "Pietų",
                "Indus": "Indėnas",
                "Lacerta": "Driežas",
                "Leo": "Liūtas",
                "Leo_Minor": "Mažasis_Liūtas",
                "Lepus": "Kiškis",
                "Libra": "Svarstyklės",
                "Lupus": "Vilkas",
                "Lynx": "Lūšis",
                "Lyra": "Lyra",
                "Mensa": "Stalkalnis",
                "Microscopium": "Mikroskopas",
                "Monoceros": "Vienaragis",
                "Musca": "Musė",
                "Norma": "Matuoklė",
                "Octans": "Oktantas",
                "Ophiuchus": "Gyvatnešis",
                "Orion": "Orionas",
                "Pavo": "Povas",
                "Pegasus": "Pegasas",
                "Perseus": "Persėjas",
                "Phoenix": "Feniksas",
                "Pictor": "Tapytojas",
                "Pisces": "Žuvys",
                "Piscis_Austrinus": "Pietų_Žuvis",
                "Puppis": "Laivagalis",
                "Pyxis": "Kompasas",
                "Reticulum": "Tinklelis",
                "Sagitta": "Strėlė",
                "Sagittarius": "Šaulys",
                "Scorpius": "Skorpionas",
                "Sculptor": "Skulptorius",
                "Scutum": "Skydas",
                "Serpens": "Gyvatė",
                "Sextans": "Gyvatė",
                "Taurus": "Sekstantas",
                "Telescopium": "Tauras",
                "Triangulum": "Teleskopas",
                "Triangulum_Australe": "Trikampis",
                "Tucana": "Pietų_Trikampis",
                "Ursa_Major": "Tukanas",
                "Ursa_Minor": "Didieji_Grįžulo_Ratai",
                "Vela": "Mažieji_Grįžulo_Ratai",
                "Virgo": "Burės",
                "Volans": "Mergelė",
                "Vulpecula": "Skraidanti_Žuvis",
            }
        }
}
