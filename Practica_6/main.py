from fuzzywuzzy import fuzz

# Простое сравнение
def standart_comparison(str_1, str_2):
    result = str_1 == str_2
    return result

# Сравнение используя пакет fuzz
def fuzzy_comparison(str_1, str_2):
    result = fuzz.ratio(str_1.lower(), str_2.lower())
    return result


str_1_good = "Apple Inc."
str_2_good = "Apple Inc."

str_1_bad = "Apple Inc."
str_2_bad = "apple Inc"

print(f"Предложения ({str_1_good} и {str_2_good}) одинаковые?\n{standart_comparison(str_1_good, str_2_good)}")
print(f"Предложения ({str_1_bad} и {str_2_bad}) одинаковые?\n{standart_comparison(str_1_bad, str_2_bad)}")

print(f"Предложения ({str_1_good} и {str_2_good}) одинаковые?\nНа {fuzzy_comparison(str_1_good, str_2_good)}%")
print(f"Предложения ({str_1_bad} и {str_2_bad}) одинаковые?\nНа {fuzzy_comparison(str_1_bad, str_2_bad)}%")