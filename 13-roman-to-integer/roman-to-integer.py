class Solution:
 def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Sağdan sola dolaş
        for ch in reversed(s):
            value = roman_map[ch]
            
            if value < prev_value:
                total -= value   # çıkarma kuralı
            else:
                total += value   # toplama kuralı
            
            prev_value = value
        
        return total

