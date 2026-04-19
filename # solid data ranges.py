# solid data ranges

bmi_ranges = ((0, 18.4), (18.5, 24.9), (25, 29.9), (30, 34.9), (35, 39.9), (40, float("inf")))

body_fat_men = {
    (2, 5): "Essential fat",
    (6, 13): "Athletes",
    (14, 17): "Fitness",
    (18, 24): "Average",
    (25, 29): "Overweight",
    (30, float("inf")): "Obese"
}

body_fat_women = {
    (10, 13): "Essential fat", 
    (14, 20): "Athletes",
    (21, 24): "Fitness",
    (25, 31): "Average",
    (32, 37): "Above average",
    (38, float("inf")): "Obese"
}

