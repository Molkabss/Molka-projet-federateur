from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Plante"]
collection = db["plantes"]

# Delete old documents
collection.drop()

plantes = [
    # 🍅 TOMATO
    {
        "plant": "Tomato",
        "disease": "Bacterial_spot",
        "description": "Bacterial disease caused by Xanthomonas spp. affecting leaves and fruits.",
        "symptoms": [
            "Small dark spots with yellow halo",
            "Rough lesions on fruits",
            "Premature leaf drop"
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove infected plants",
            "Preventive treatment with Bordeaux mixture at first symptoms"
        ],
        "prevention": [
            "Use certified seeds",
            "Crop rotation every 3 years",
            "Avoid overhead irrigation",
            "Space plants for good ventilation"
        ],
        "causes": "Bacterium Xanthomonas campestris transmitted through infected seeds, water splashes and insects.",
        "risk_conditions": ["high_humidity", "warm_temp", "rain"],
        "source": "University agricultural extension"
    },
    {
        "plant": "Tomato",
        "disease": "Early_blight",
        "description": "Fungal disease caused by Alternaria solani mainly affecting lower leaves.",
        "symptoms": [
            "Concentric brown target-like spots",
            "Yellowing of lower leaves",
            "Progressive defoliation from bottom to top",
            "Dark spots on stems and fruits"
        ],
        "treatment": [
            "Fungicide based on chlorothalonil or mancozeb",
            "Immediately remove affected leaves",
            "Apply every 7-10 days in humid weather",
            "Organic treatment: Bordeaux mixture or baking soda"
        ],
        "prevention": [
            "Mandatory crop rotation",
            "Adequate plant spacing",
            "Water only at the base",
            "Mulching to avoid soil splashing"
        ],
        "causes": "Fungus Alternaria solani that survives in plant debris and spreads through wind and splashing.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Phytopathology guide"
    },
    {
        "plant": "Tomato",
        "disease": "Late_blight",
        "description": "Serious and devastating disease caused by Phytophthora infestans, responsible for the Irish Great Famine.",
        "symptoms": [
            "Irregular watery brown spots on leaves",
            "White fuzz under leaves in humid weather",
            "Rapid fruit rot",
            "Blackening of stems"
        ],
        "treatment": [
            "Systemic fungicide (Metalaxyl, Cymoxanil) urgently",
            "Bordeaux mixture as preventive treatment",
            "Immediate destruction of heavily infected plants",
            "Do not compost diseased plants"
        ],
        "prevention": [
            "Strict humidity control",
            "Resistant varieties (e.g., Mountain Magic)",
            "Preventive copper treatment before humid periods",
            "Weather monitoring and treatment before rainy episodes"
        ],
        "causes": "Oomycete Phytophthora infestans spreading through airborne spores in cool and humid weather (15-20°C, humidity > 90%).",
        "risk_conditions": ["high_humidity", "low_temp", "rain"],
        "source": "FAO"
    },
    {
        "plant": "Tomato",
        "disease": "Leaf_Mold",
        "description": "Fungal disease due to Passalora fulva, common in greenhouses.",
        "symptoms": [
            "Pale yellow spots on upper leaf surface",
            "Olive to brown mold under leaves",
            "Progressive yellowing and drying"
        ],
        "treatment": [
            "Fungicide based on mancozeb or chlorothalonil",
            "Immediate improvement of ventilation",
            "Reduction of humidity below 85%"
        ],
        "prevention": [
            "Reduce ambient humidity",
            "Avoid condensation on leaves",
            "Adequate greenhouse ventilation",
            "Plant spacing"
        ],
        "causes": "Fungus Passalora fulva favored by high relative humidity (> 85%) and temperatures of 20-25°C.",
        "risk_conditions": ["high_humidity"],
        "source": "Horticultural manual"
    },
    {
        "plant": "Tomato",
        "disease": "Septoria_leaf_spot",
        "description": "Fungal infection caused by Septoria lycopersici, very common on tomatoes.",
        "symptoms": [
            "Small circular beige spots with dark brown border",
            "Black dots (pycnidia) in the center of lesions",
            "Yellowing around spots",
            "Severe defoliation in advanced infection"
        ],
        "treatment": [
            "Protective fungicide (chlorothalonil, mancozeb)",
            "Removal of diseased leaves",
            "Application every 7-14 days"
        ],
        "prevention": [
            "Crop rotation",
            "Ground watering only",
            "Removal of plant debris",
            "Tool disinfection"
        ],
        "causes": "Fungus Septoria lycopersici surviving in plant debris and spreading through water splashes and wind.",
        "risk_conditions": ["high_humidity", "rain"],
        "source": "Agricultural university"
    },
    {
        "plant": "Tomato",
        "disease": "Spider_mites-Two-spotted_spider_mite",
        "description": "Infestation by Tetranychus urticae mites causing significant damage in hot and dry weather.",
        "symptoms": [
            "Tiny yellow or white dots on leaves",
            "Fine webs between leaves and stems",
            "Bronze then dried leaves",
            "Premature leaf drop"
        ],
        "treatment": [
            "Specific acaricide (Abamectin, Bifenazate)",
            "Strong water spray under leaves",
            "Neem oil as organic treatment",
            "Insecticidal soap"
        ],
        "prevention": [
            "Regular monitoring especially in hot weather",
            "Maintain moderate humidity",
            "Avoid excess nitrogen",
            "Encourage natural predators (predatory mites)"
        ],
        "causes": "Mite Tetranychus urticae favored by hot and dry weather (> 30°C), low humidity and excess nitrogen.",
        "risk_conditions": ["high_temp", "low_humidity", "dry"],
        "source": "Agricultural pest guide"
    },
    {
        "plant": "Tomato",
        "disease": "Target_Spot",
        "description": "Fungal disease caused by Corynespora cassiicola affecting leaves, stems and fruits.",
        "symptoms": [
            "Brown spots with concentric rings (target appearance)",
            "Progressive defoliation",
            "Lesions on stems and fruits"
        ],
        "treatment": [
            "Preventive fungicide (mancozeb, chlorothalonil)",
            "Remove infected plant debris",
            "Improve air circulation"
        ],
        "prevention": [
            "Good aeration between plants",
            "Crop rotation",
            "Base watering",
            "Avoid injuries to plants"
        ],
        "causes": "Fungus Corynespora cassiicola favored by high heat and humidity.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Agricultural extension"
    },
    {
        "plant": "Tomato",
        "disease": "Tomato_mosaic_virus",
        "description": "Highly contagious viral disease affecting growth and fruit quality.",
        "symptoms": [
            "Light and dark green color mosaic on leaves",
            "Deformed and blistered leaves",
            "Deformed and spotted fruits",
            "Stunted growth"
        ],
        "treatment": [
            "No curative treatment available",
            "Immediately remove infected plants",
            "Disinfect all tools with bleach",
            "Wash hands after handling"
        ],
        "prevention": [
            "Strict garden hygiene",
            "Certified and healthy seeds",
            "Vector insect control",
            "Do not smoke near plants (tobacco can transmit the virus)"
        ],
        "causes": "TMV (Tobacco Mosaic Virus) transmitted through direct contact, contaminated tools and sometimes infected seeds.",
        "risk_conditions": ["high_temp"],
        "source": "Phytosanitary institute"
    },
    {
        "plant": "Tomato",
        "disease": "Tomato_Yellow_Leaf_Curl_Virus",
        "description": "Serious virus transmitted by whitefly (Bemisia tabaci), very devastating.",
        "symptoms": [
            "Yellowed leaves curling upward",
            "Reduction in leaf size",
            "Stunted plant growth",
            "Absence of fruits"
        ],
        "treatment": [
            "Immediate whitefly control (insecticide)",
            "Remove heavily infected plants",
            "Use yellow sticky traps"
        ],
        "prevention": [
            "Fine mesh insect nets",
            "TYLCV resistant varieties",
            "Preventive whitefly control",
            "Eliminate host weeds"
        ],
        "causes": "TYLCV virus transmitted exclusively by the whitefly Bemisia tabaci. Spreads rapidly in hot and dry weather.",
        "risk_conditions": ["high_temp", "dry"],
        "source": "Agricultural center"
    },
    # 🍎 APPLE
    {
        "plant": "Apple",
        "disease": "Apple_scab",
        "description": "Most common fungal disease of apple trees caused by Venturia inaequalis.",
        "symptoms": [
            "Velvety olive-brown spots on leaves",
            "Deformation and cracking of fruits",
            "Premature leaf fall",
            "Reduced market quality"
        ],
        "treatment": [
            "Preventive fungicide (Captan, Myclobutanil)",
            "Treatment from bud swell",
            "Renew after each rain",
            "Bordeaux mixture for organic"
        ],
        "prevention": [
            "Pruning to improve aeration",
            "Collection and destruction of fallen leaves",
            "Resistant varieties",
            "Early spring treatment"
        ],
        "causes": "Fungus Venturia inaequalis that overwinters in dead leaves and releases spores in spring during rains.",
        "risk_conditions": ["high_humidity", "rain"],
        "source": "Arboricultural guide"
    },
    {
        "plant": "Apple",
        "disease": "Black_rot",
        "description": "Disease caused by Botryosphaeria obtusa attacking fruits, leaves and branches.",
        "symptoms": [
            "Circular purple spots on leaves",
            "Brown-black rot of fruits",
            "Mummified fruits remaining on the tree",
            "Cankers on branches"
        ],
        "treatment": [
            "Remove all affected fruits and branches",
            "Fungicide (Captan, Thiophanate-methyl)",
            "Prune cankers on branches"
        ],
        "prevention": [
            "Thorough orchard cleaning",
            "Remove mummified fruits in winter",
            "Regular sanitary pruning",
            "Avoid injuries to trees"
        ],
        "causes": "Fungus Botryosphaeria obtusa entering through wounds and damaged fruits. Favored by heat and humidity.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Agricultural extension"
    },
    {
        "plant": "Apple",
        "disease": "Cedar_apple_rust",
        "description": "Fungal disease requiring juniper as secondary host to complete its cycle.",
        "symptoms": [
            "Bright orange spots on leaves",
            "Orange tubes under leaves",
            "Fruit deformation",
            "Premature leaf drop"
        ],
        "treatment": [
            "Specific fungicide (Myclobutanil, Trifloxystrobin)",
            "Treatment at first symptoms",
            "Repeated applications every 7-10 days"
        ],
        "prevention": [
            "Keep junipers away from apple trees (> 300m)",
            "Rust resistant varieties",
            "Preventive spring treatments"
        ],
        "causes": "Fungus Gymnosporangium juniperi-virginianae with life cycle between apple trees and junipers. Spores released in humid spring weather.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Horticultural university"
    },
    # 🌽 CORN
    {
        "plant": "Corn",
        "disease": "Cercospora_leaf_spot",
        "description": "Fungal disease caused by Cercospora zeae-maydis causing leaf lesions.",
        "symptoms": [
            "Elongated grayish rectangular lesions",
            "Edges parallel to veins",
            "Reduced photosynthesis",
            "Reduced grain yield"
        ],
        "treatment": [
            "Foliar fungicide (Azoxystrobin, Propiconazole)",
            "Early application before V6 stage",
            "Aerial treatment for large areas"
        ],
        "prevention": [
            "Crop rotation with legumes",
            "Resistant hybrids",
            "Deep plowing to bury residues"
        ],
        "causes": "Fungus Cercospora zeae-maydis surviving in corn residues. Favored by prolonged humidity and temperatures of 22-30°C.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Corn manual"
    },
    {
        "plant": "Corn",
        "disease": "Common_rust",
        "description": "Fungal infection by Puccinia sorghi producing characteristic pustules on leaves.",
        "symptoms": [
            "Rust-brown pustules on both sides of leaves",
            "Yellowing around pustules",
            "Reduced photosynthesis",
            "In severe cases: entirely yellowed leaves"
        ],
        "treatment": [
            "Triazole fungicide (Propiconazole, Tebuconazole)",
            "Application at first pustule appearance",
            "Repeated treatment if necessary"
        ],
        "prevention": [
            "Rust-resistant hybrids",
            "Early planting to avoid risk periods",
            "Crop rotation"
        ],
        "causes": "Fungus Puccinia sorghi whose spores are wind-transported. Favored by cool and humid weather (16-23°C, humidity > 95%).",
        "risk_conditions": ["high_humidity", "low_temp"],
        "source": "Corn guide"
    },
    {
        "plant": "Corn",
        "disease": "Northern_Leaf_Blight",
        "description": "Serious fungal disease caused by Exserohilum turcicum that can reduce yield by 30-50%.",
        "symptoms": [
            "Elongated gray-green cigar-shaped lesions (5-15cm)",
            "Black sporulation on lesions in humid weather",
            "Rapid leaf drying",
            "Upper leaf infection in severe cases"
        ],
        "treatment": [
            "Fungicide (Azoxystrobin, Propiconazole, Trifloxystrobin)",
            "Application at V6-V8 stage preventively",
            "Curative treatment at first lesions"
        ],
        "prevention": [
            "Resistant hybrids (Ht1, Ht2 gene)",
            "Mandatory crop rotation",
            "Plowing to bury infected residues"
        ],
        "causes": "Fungus Exserohilum turcicum surviving in residues. Spores dispersed by wind during humid and warm periods.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Agricultural university"
    },
    # 🍇 GRAPE
    {
        "plant": "Grape",
        "disease": "Black_rot",
        "description": "Serious fungal disease caused by Guignardia bidwellii destroying fruits and leaves.",
        "symptoms": [
            "Circular brown spots with dark border on leaves",
            "Berries that brown and mummify",
            "Black dots (pycnidia) on lesions",
            "Complete bunch destruction in severe cases"
        ],
        "treatment": [
            "Fungicide (Myclobutanil, Captan, Tebuconazole)",
            "Start from bud break",
            "Renew after each rain",
            "Remove all mummies from the vine"
        ],
        "prevention": [
            "Eliminate all infected debris at end of season",
            "Severe pruning to aerate foliage",
            "Preventive treatment from leaf emergence",
            "Resistant varieties"
        ],
        "causes": "Fungus Guignardia bidwellii overwintering in mummies and cankers. Spreads through rain and wind in warm and humid weather.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Viticultural guide"
    },
    {
        "plant": "Grape",
        "disease": "Esca_(Black_Measles)",
        "description": "Wood disease complex caused by several fungi (Phaeomoniella, Phaeoacremonium).",
        "symptoms": [
            "Leaves with yellow-red burned margins (tiger pattern)",
            "Discolored brown-gray wood inside",
            "Sudden apoplexy in summer (rapid vine death)",
            "Gum exudate on trunk"
        ],
        "treatment": [
            "Severe sanitary pruning (remove infected wood)",
            "Protect pruning wounds with fungicidal mastic",
            "No effective curative treatment once established",
            "Uproot and replant heavily affected vines"
        ],
        "prevention": [
            "Systematic disinfection of pruning tools",
            "Protection of pruning wounds",
            "Avoid pruning in humid weather",
            "Use certified healthy plant material"
        ],
        "causes": "Complex of wood pathogenic fungi entering through pruning wounds. Favored by water stress and high temperatures.",
        "risk_conditions": ["high_temp", "dry"],
        "source": "Viticultural institute"
    },
    {
        "plant": "Grape",
        "disease": "Leaf_blight_(Isariopsis_Leaf_Spot)",
        "description": "Fungal disease caused by Isariopsis clavispora causing angular leaf spots.",
        "symptoms": [
            "Angular brown to reddish spots",
            "Premature leaf fall",
            "General vine weakening",
            "Reduced grape quality"
        ],
        "treatment": [
            "Adapted foliar fungicide",
            "Improved ventilation through pruning",
            "Removal of infected leaves"
        ],
        "prevention": [
            "Good foliage aeration",
            "Avoid excess nitrogen",
            "Preventive treatment in humid periods"
        ],
        "causes": "Fungus Isariopsis clavispora favored by humidity and moderate temperatures. Spreads through airborne spores.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Viticultural extension"
    },
    # 🥔 POTATO
    {
        "plant": "Potato",
        "disease": "Early_blight",
        "description": "Fungal disease due to Alternaria solani affecting leaves and tubers.",
        "symptoms": [
            "Concentric brown rings on leaves (target appearance)",
            "Yellowing around spots",
            "Dark lesions on tubers",
            "Premature defoliation"
        ],
        "treatment": [
            "Fungicide (Mancozeb, Chlorothalonil, Azoxystrobin)",
            "Regular applications every 10-14 days",
            "Improve potassium nutrition of soil"
        ],
        "prevention": [
            "Crop rotation (3-4 years)",
            "Use certified seeds",
            "Remove plant debris",
            "Balanced fertilization"
        ],
        "causes": "Fungus Alternaria solani surviving in debris and soil. Favored by humidity/drought alternation and stressed plants.",
        "risk_conditions": ["high_humidity", "warm_temp"],
        "source": "Potato guide"
    },
    {
        "plant": "Potato",
        "disease": "Late_blight",
        "description": "Most destructive potato disease caused by Phytophthora infestans.",
        "symptoms": [
            "Irregular brown spots on leaves and stems",
            "White fuzz under leaves in humid weather",
            "Brown rot of tubers",
            "Characteristic smell of rot"
        ],
        "treatment": [
            "Emergency systemic fungicide (Metalaxyl, Cymoxanil)",
            "Contact fungicide (Mancozeb, Bordeaux mixture)",
            "Destroy heavily infected plants",
            "Do not store suspicious tubers"
        ],
        "prevention": [
            "Strict humidity control",
            "Resistant varieties (Sarpo Mira, Cara)",
            "Preventive treatment before humid periods",
            "Hill plants to protect tubers"
        ],
        "causes": "Oomycete Phytophthora infestans favored by cool weather (10-20°C) and humidity > 90%. Spores dispersed by wind and rain.",
        "risk_conditions": ["high_humidity", "low_temp", "rain"],
        "source": "FAO"
    }
]

result = collection.insert_many(plantes)
print(f"✅ {len(result.inserted_ids)} documents inserted into 'plantes'")